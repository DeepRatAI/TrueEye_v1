# main.py
import os
import logging
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, Response
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import requests
from typing import Optional

# -------------------------------
# CONFIGURACIÓN DE LOGGING
# -------------------------------
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# -------------------------------
# CARGA DEL FLOW_API_URL DESDE SECRETS
# -------------------------------
FLOW_API_URL = os.getenv("FLOW_API_URL")
if FLOW_API_URL is None:
    raise RuntimeError("❌ FLOW_API_URL no está definido. Agregalo en los Secrets de Hugging Face.")

# Log para verificar la URL (sin mostrar la URL completa por seguridad)
logger.info(f"✅ FLOW_API_URL configurado: {FLOW_API_URL[:30]}...")

# -------------------------------
# INICIALIZACIÓN DE LA APP
# -------------------------------
app = FastAPI()

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montar carpeta estática
app.mount("/static", StaticFiles(directory="static"), name="static")

# Ruta principal: servir index.html
@app.get("/")
async def serve_index():
    return FileResponse("static/index.html")

# -------------------------------
# LOGO FALLBACK HANDLER
# -------------------------------
@app.get("/static/te.png")
async def serve_logo():
    """Sirve el logo te.png si existe, o un SVG placeholder si no"""
    logo_path = "static/te.png"
    
    if os.path.exists(logo_path):
        # Si existe el logo, servirlo normalmente
        return FileResponse(logo_path)
    else:
        # Si no existe, devolver un SVG placeholder
        svg_content = '''<svg width="40" height="40" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg">
  <!-- Fondo circular -->
  <circle cx="20" cy="20" r="18" fill="#f6ae2d"/>
  
  <!-- Ojo estilizado -->
  <g transform="translate(20, 20)">
    <!-- Forma del ojo -->
    <path d="M -12 0 Q -6 -6 0 -6 Q 6 -6 12 0 Q 6 6 0 6 Q -6 6 -12 0" 
          fill="#420909" 
          stroke="none"/>
    
    <!-- Iris -->
    <circle cx="0" cy="0" r="5" fill="#f6ae2d"/>
    
    <!-- Pupila -->
    <circle cx="0" cy="0" r="3" fill="#420909"/>
    
    <!-- Brillo -->
    <circle cx="-1" cy="-1" r="1" fill="white" opacity="0.8"/>
  </g>
  
  <!-- Texto TE -->
  <text x="20" y="35" font-family="Arial, sans-serif" font-size="8" font-weight="bold" 
        text-anchor="middle" fill="#420909">TE</text>
</svg>'''
        
        return Response(
            content=svg_content,
            media_type="image/svg+xml",
            headers={
                "Cache-Control": "public, max-age=3600",
                "Content-Type": "image/svg+xml"
            }
        )

# -------------------------------
# MODELO DE ENTRADA
# -------------------------------
class AnalyzeRequest(BaseModel):
    url: str

class AnalyzeResponse(BaseModel):
    result: str
    success: bool = True
    error: Optional[str] = None

# -------------------------------
# ENDPOINT DE ANÁLISIS
# -------------------------------
@app.post("/analyze", response_model=AnalyzeResponse)
async def analyze(request: AnalyzeRequest):
    logger.info(f"📥 Recibida solicitud de análisis para URL: {request.url}")
    
    try:
        # IMPORTANTE: El flow espera un mensaje de chat que contenga la URL,
        # no la URL directamente. El ChatInput procesará el mensaje y 
        # el URLComponent extraerá la URL del texto.
        payload = {
            "input_value": request.url,  # El ChatInput recibirá esto como mensaje
            "output_type": "chat",
            "input_type": "chat",
            "tweaks": {}  # Agregar tweaks vacío por si acaso
        }
        
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "TrueEye-HuggingFace-Space/1.0"
        }
        
        logger.info(f"📤 Enviando petición a Langflow...")
        logger.debug(f"Payload: {payload}")
        
        # Hacer la petición con timeout de 300 segundos (5 minutos)
        # dado que el flow tiene múltiples llamadas a modelos LLM
        response = requests.post(
            FLOW_API_URL, 
            json=payload, 
            headers=headers,
            timeout=300  # 5 minutos de timeout
        )
        
        logger.info(f"📨 Respuesta recibida. Status: {response.status_code}")
        
        # Verificar el status de la respuesta
        response.raise_for_status()
        
        # Parsear la respuesta
        data = response.json()
        logger.debug(f"Respuesta JSON: {data}")
        
        # El formato de respuesta de Langflow puede variar
        # Intentar extraer el resultado de diferentes formas
        result_text = None
        
        # Opción 1: Respuesta directa en 'result'
        if isinstance(data, dict) and "result" in data:
            result_text = data["result"]
        
        # Opción 2: Respuesta en formato de outputs
        elif isinstance(data, dict) and "outputs" in data:
            outputs = data["outputs"]
            if isinstance(outputs, list) and len(outputs) > 0:
                output = outputs[0]
                if "outputs" in output:
                    # Buscar el ChatOutput
                    for node_output in output["outputs"]:
                        if "message" in node_output:
                            if isinstance(node_output["message"], dict):
                                result_text = node_output["message"].get("text", "")
                            else:
                                result_text = str(node_output["message"])
                            break
        
        # Opción 3: Intentar extraer de cualquier estructura
        if not result_text and isinstance(data, dict):
            # Buscar recursivamente cualquier campo 'text' o 'message'
            result_text = _extract_text_from_response(data)
        
        if not result_text:
            logger.warning("⚠️ No se pudo extraer texto de la respuesta")
            result_text = "⚠️ Se procesó la solicitud pero no se pudo extraer el resultado. Respuesta recibida: " + str(data)[:200]
        
        logger.info("✅ Análisis completado exitosamente")
        return AnalyzeResponse(result=result_text)
        
    except requests.exceptions.Timeout:
        logger.error("⏱️ Timeout en la petición a Langflow")
        return AnalyzeResponse(
            result="❌ Error: La solicitud tardó demasiado tiempo. El análisis puede ser muy complejo o el servicio está sobrecargado.",
            success=False,
            error="timeout"
        )
    except requests.exceptions.ConnectionError as e:
        logger.error(f"🔌 Error de conexión: {e}")
        return AnalyzeResponse(
            result="❌ Error: No se pudo conectar con el servicio de análisis. Verifica que el FLOW_API_URL esté correctamente configurado.",
            success=False,
            error="connection"
        )
    except requests.exceptions.HTTPError as e:
        logger.error(f"🚫 Error HTTP: {e}")
        logger.error(f"Respuesta del servidor: {e.response.text if e.response else 'No hay respuesta'}")
        return AnalyzeResponse(
            result=f"❌ Error del servidor: {e}. Verifica que el flow esté activo y funcionando.",
            success=False,
            error=f"http_{e.response.status_code if e.response else 'unknown'}"
        )
    except Exception as e:
        logger.exception(f"💥 Error inesperado: {e}")
        return AnalyzeResponse(
            result=f"❌ Error inesperado: {str(e)}",
            success=False,
            error="unknown"
        )

def _extract_text_from_response(data):
    """Función auxiliar para extraer texto de una respuesta compleja"""
    if isinstance(data, str):
        return data
    
    if isinstance(data, dict):
        # Buscar campos comunes
        for key in ['text', 'message', 'result', 'output', 'content']:
            if key in data:
                value = data[key]
                if isinstance(value, str):
                    return value
                elif isinstance(value, dict) or isinstance(value, list):
                    result = _extract_text_from_response(value)
                    if result:
                        return result
        
        # Si no encontramos campos conocidos, buscar en todos los valores
        for value in data.values():
            if isinstance(value, (dict, list)):
                result = _extract_text_from_response(value)
                if result:
                    return result
    
    elif isinstance(data, list):
        for item in data:
            result = _extract_text_from_response(item)
            if result:
                return result
    
    return None

# -------------------------------
# ENDPOINT DE SALUD
# -------------------------------
@app.get("/health")
async def health_check():
    """Endpoint para verificar que el servicio está funcionando"""
    return {
        "status": "healthy",
        "flow_configured": bool(FLOW_API_URL),
        "service": "TrueEye Reports"
    }