<p align="center">
  <img src="static/banner.gif" alt="Banner TrueEye" width="100%">
</p>

# 🧿 TrueEye — Sistema Inteligente de Alfabetización Mediática

**TrueEye** es una herramienta de inteligencia artificial diseñada para analizar artículos de noticias y contenido web, con el objetivo de detectar sesgos narrativos, identificar la audiencia objetivo y revelar intencionalidades ocultas o estructuras de manipulación simbólica.
En otras palabras, **no solo detecta noticias falsas**, sino que también examina **para quiénes fue escrito un contenido y con qué propósito**.
El sistema produce un informe detallado que ayuda a la alfabetización mediática, señalando indicios sutiles presentes en el texto.

---

## 🚀 Demo

* 🌐 [Probar TrueEye en Hugging Face Spaces](https://huggingface.co/spaces/DeepRat/TrueEye_Reports)
* 🖥️ [Sitio oficial del proyecto](https://trueeye.deeprat.tech)

> Nota: La demo en Hugging Face requiere acceso a internet y puede necesitar iniciar sesión.

---

## 🧩 ¿Qué hace TrueEye?

Al ingresar una URL de un artículo de noticias, **TrueEye** realiza **tres análisis consecutivos**:

### 📊 Sesgos y Matices

* Detecta la polaridad narrativa (positiva, negativa o neutral).
* Identifica estrategias retóricas (miedo, manipulación, ironía, etc.).
* Resume el artículo y marca afirmaciones cuestionables.

### 🎯 Segmentación de Audiencia

* Infiere el perfil demográfico y emocional del lector objetivo.
* Detecta valores explotados, sesgos reafirmados y momento de consumo esperado.

### ⚠️ Intencionalidad y Peligrosidad

* Evalúa manipulación simbólica, agendas ocultas y beneficiarios.
* Estima nivel de sofisticación narrativa y riesgo de impacto social.

> Cada informe incluye enlaces a fuentes confiables para verificación.

---

## ⚙️ Arquitectura del Proyecto

**TrueEye** consta de tres capas principales:

* 🧱 **Frontend**: Web estática en HTML + TailwindCSS + JS (`static/index.html`)
* 🧠 **Backend**: API REST en Python (`main.py`) con FastAPI
* 🔁 **Orquestación IA**: Flujo de LangFlow (`TrueEyeBeta.json`) con agentes Claude (Opus / Sonnet)

> El análisis lo realizan modelos de lenguaje ejecutados vía LangFlow + APIs externas.

---

## 📁 Estructura del Repositorio

```
TrueEye_v1/
├── static/
│   ├── index.html        # Interfaz frontend
│   └── te.png            # Logo del proyecto
├── main.py               # Backend FastAPI
├── requirements.txt      # Dependencias Python
├── Dockerfile            # Despliegue (HuggingFace)
├── TrueEyeBeta.json      # Flujo IA de LangFlow
```

---

## 💻 Cómo Ejecutarlo Localmente

### 🔧 Requisitos mínimos

* ✅ Python **3.10+**
* ✅ Acceso a internet (para conectarse con los modelos de IA)
* ✅ Clave API de **Claude** o modelo compatible
* ✅ LangFlow instalado (`pip install langflow`)

> 💡 No se requiere GPU ni hardware especializado. Todo el procesamiento se delega a los modelos externos.

### 🧪 Pasos para correrlo:

```bash
# 1. Clonar el repositorio
git clone https://github.com/DeepRatAI/TrueEye_v1.git
cd TrueEye_v1

# 2. Instalar dependencias del backend
pip install -r requirements.txt

# 3. Definir la URL del flujo LangFlow
export FLOW_API_URL="http://localhost:7860/predict"  # Reemplazar según tu instancia

# 4. Lanzar el backend
uvicorn main:app --reload
```

Luego, abrí el archivo `static/index.html` en tu navegador.
Introducí una URL, presioná "Analizar", y obtendrás el informe generado por IA en segundos.

> 📌 Asegurate de que LangFlow esté corriendo y tenga cargado el flujo `TrueEyeBeta.json`. La clave API debe estar configurada según el proveedor (ej. Anthropic).

---

## 📌 Roadmap

| Versión  | Estado        | Descripción                                                  |
| -------- | ------------- | ------------------------------------------------------------ |
| ✅ v1.0   | En producción | Análisis textual completo por URL con IA explicativa         |
| 🔄 v2.0  | En diseño     | TrueEye Chat: versión conversacional con memoria persistente |
| 🖼️ v3.0 | Planificada   | Razonamiento multimodal sobre texto + imágenes/audio/video   |
| 🧪 v4.0  | Planificada   | Detección de deepfakes y contenido sintético                 |

---

## 📚 Tecnologías Utilizadas

* **FastAPI** — Backend API REST en Python
* **LangFlow** — Orquestación de flujos LLM con agentes, memoria y lógica condicional
* **Claude (Opus / Sonnet)** — Modelos de lenguaje vía API de Anthropic
* **TailwindCSS & JS** — Interfaz frontend simple y moderna
* **Docker** — Para despliegue reproducible (Hugging Face Spaces)

---

## ✍️ Autor

**Gonzalo Romero (DeepRat)**
Ingeniero en IA, Software y Sistemas · Prompt Engineer · Full-stack Developer

🔗 [Web](https://deeprat.tech) | [Hugging Face](https://huggingface.co/DeepRat) | [GitHub](https://github.com/DeepRatAI) | [LinkedIn](https://www.linkedin.com/in/deeprat) | [Medium](https://medium.com/@deeprat)

---

## 🧠 Licencia

Este proyecto está licenciado bajo **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**.
Podés copiar, modificar y distribuir el código siempre que menciones al autor (**DeepRat**) y no lo utilices con fines comerciales sin autorización previa.

> 📩 Para solicitudes comerciales, contactá a: [info@deeprat.tech](mailto:info@deeprat.tech)

---


