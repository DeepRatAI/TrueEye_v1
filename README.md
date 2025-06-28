# 🧿 TrueEye — Intelligent Media Literacy System

**TrueEye** es una herramienta de inteligencia artificial diseñada para analizar artículos de noticias y contenido web, con el objetivo de detectar **sesgos narrativos**, identificar la **audiencia objetivo**, y revelar **intencionalidades ocultas** o estructuras de manipulación simbólica.

> “TrueEye no sólo detecta fake news, sino también para quiénes fueron escritas y por qué.”

---

## 🚀 Demo

* 🎯 [Abrir TrueEye en Hugging Face Spaces](https://huggingface.co/spaces/DeepRat/TrueEye_Reports)
* 🌐 [Sitio oficial del proyecto](https://trueeye.deeprat.tech)

---

## 🧩 ¿Qué hace TrueEye?

Cuando ingresás una URL, TrueEye realiza tres análisis consecutivos:

1. **📊 Sesgo y Matices**

   * Detecta la polaridad narrativa (positiva, negativa o neutral)
   * Identifica matices como polarización, miedo, desconfianza
   * Resume el contenido y señala afirmaciones engañosas o débiles

2. **🎯 Segmentación de Audiencia**

   * Infiere perfil demográfico y psicográfico del lector objetivo
   * Analiza valores, creencias, emociones y sesgos explotados
   * Detecta timing, contexto de consumo y estrategias de targeting

3. **⚠️ Intencionalidad y Peligrosidad**

   * Evalúa la presencia de manipulación o violencia simbólica
   * Identifica agendas políticas, actores beneficiados y omisiones críticas
   * Asigna nivel de sofisticación y daño potencial

🔍 Además, el informe incluye enlaces a fuentes externas confiables para fact-checking.

---

## ⚙️ Arquitectura

* **Frontend**: HTML + TailwindCSS + JS
* **Backend**: FastAPI (Python) + Requests
* **Orquestación IA**: LangFlow + agentes Claude (Opus / Sonnet)
* **Despliegue**: Docker en Hugging Face Spaces

---

## 💻 Perfil técnico del autor

Este proyecto fue desarrollado por **Gonzalo Romero**, estudiante de Ingeniería en Sistemas, **Ingeniero en Inteligencia Artificial** certificado por IBM, y **practicante profesional de Ingeniería de Software**, con foco en aplicaciones IA explicables y de impacto social.

---

## 📁 Estructura del repositorio

```
📦 trueeye
├── static/
│   ├── index.html        # Interfaz visual
│   └── te.png            # Logo del proyecto
├── main.py               # Backend FastAPI que conecta al flujo LangFlow
├── requirements.txt      # Dependencias del backend
├── Dockerfile            # Imagen para Hugging Face Spaces
├── TrueEyeBeta.json      # Flujo LangFlow con agentes y lógica IA
```

---


## 📌 Roadmap

| Versión  | Estado        | Descripción                                            |
| -------- | ------------- | ------------------------------------------------------ |
| ✅ v1.0   | En producción | Análisis textual completo con IA explicativa           |
| 🔄 v2.0  | En diseño     | “TrueEye Chat”: interacción conversacional con memoria |
| 🖼️ v3.0 | Planificada   | Análisis multimodal: texto + imágenes/audio/video      |
| 🧪 v4.0  | Planificada   | Detección de deepfakes y contenido sintético           |

---

## 👨‍💻 Cómo ejecutarlo localmente

```bash
# Clonar el proyecto
git clone https://github.com/DeepRat/trueeye.git
cd trueeye

# Instalar dependencias
pip install -r requirements.txt

# Iniciar servidor backend
uvicorn main:app --reload
```

Luego abrí `static/index.html` en tu navegador. El frontend interactúa con `localhost:8000/analyze`.

---

## 📚 Tecnologías utilizadas

* `FastAPI` · `LangFlow` · `Claude Opus/Sonnet` · `Docker`
* `TailwindCSS` · `JavaScript` · `Marked.js`

---

## ✍️ Autor

**Gonzalo Romero (HermesIA)**
AI Engineer · Software Engineer · Systems Engineering Student
🔗 [deeprat.tech](https://deeprat.tech) · [GitHub](https://github.com/DeepRat) · [Hugging Face](https://huggingface.co/DeepRat) · [LinkedIn](https://www.linkedin.com/in/gonzaloromerodeeprat) · [Medium](https://medium.com/@gonzaloromerodeeprat)

---

## 🧠 Licencia

MIT License — uso libre y adaptaciones permitidas. El crédito es bienvenido.

---
