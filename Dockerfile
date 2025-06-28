# Imagen base ligera de Python
FROM python:3.10-slim

# Configurar variables de entorno para Python
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Crear directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar dependencias primero para aprovechar el cache de Docker
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Crear directorio estático
RUN mkdir -p /app/static

# Copiar el resto de la aplicación
COPY main.py .
COPY static/ ./static/
# Copiar script de debug si existe (opcional)
COPY debug_config.py* ./

# Crear un usuario no-root para seguridad
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Exponer el puerto que usa HF Spaces
EXPOSE 7860

# Healthcheck para verificar que el servicio está activo
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
  CMD python -c "import requests; requests.get('http://localhost:7860/health')"

# Comando para lanzar la app FastAPI con mejor configuración
CMD ["uvicorn", "main:app", \
     "--host", "0.0.0.0", \
     "--port", "7860", \
     "--log-level", "info", \
     "--access-log", \
     "--workers", "1"]