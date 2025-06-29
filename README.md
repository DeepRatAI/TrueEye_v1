---
license: creativeml-openrail-m
title: TrueEye Reports
sdk: docker
---
<p align="center">
  <img src="static/banner.gif" alt="Banner TrueEye" width="100%">
</p>

# 🧿 TrueEye — Intelligent Media Literacy System

**TrueEye** is an AI-powered tool designed to analyze news articles and web content to detect narrative bias, identify the target audience, and reveal hidden intentions or manipulative rhetorical structures.
In other words, **it doesn’t just detect fake news** — it analyzes **who the content is written for and why**.
The system generates a detailed report to support media literacy, highlighting subtle signals embedded in the text.

---

## 🚀 Demo

* 🌐 [Try TrueEye on Hugging Face Spaces](https://huggingface.co/spaces/DeepRat/TrueEye_Reports)
* 🖥️ [Official project site](https://trueeye.deeprat.tech)

> Note: The demo requires internet access and may prompt you to log in to Hugging Face.

---

## 🧩 What Does TrueEye Do?

When given a news article URL, **TrueEye** performs **three consecutive analyses**:

### 📊 Bias & Narrative Tone

* Detects narrative polarity (positive, negative, neutral).
* Identifies rhetorical strategies (fear, polarization, irony).
* Summarizes the content and flags questionable claims.

### 🎯 Audience Profiling

* Infers demographic and emotional profile of the target reader.
* Identifies values, beliefs, or cognitive biases being exploited.

### ⚠️ Intent & Risk Evaluation

* Detects manipulative discourse or symbolic violence.
* Highlights hidden agendas, information gaps, and potential societal risk.

> The report includes links to trustworthy sources for fact-checking.

---

## ⚙️ Architecture Overview

**TrueEye** consists of three main components:

* 🧱 **Frontend**: Static web interface built with HTML, TailwindCSS, and JavaScript (`static/index.html`).
* 🧠 **Backend**: REST API written in Python using FastAPI (`main.py`).
* 🔁 **AI Orchestration**: LangFlow flow (`TrueEyeBeta.json`) powered by Claude models (Opus / Sonnet).

> The heavy analysis is performed by external LLMs through LangFlow API calls.

---

## 📁 Project Structure

```
TrueEye_v1/
├── static/
│   ├── index.html        # Frontend UI
│   └── te.png            # Project logo
├── main.py               # FastAPI backend
├── requirements.txt      # Python dependencies
├── Dockerfile            # Deployment config (Hugging Face Spaces)
├── TrueEyeBeta.json      # LangFlow pipeline (AI logic)
```

---

## 💻 How to Run It Locally

### 🔧 Requirements

* ✅ Python **3.10+**
* ✅ Internet access (to connect with AI APIs)
* ✅ Claude API key or other compatible LLM provider
* ✅ LangFlow installed (`pip install langflow`)

> 💡 No GPU or specialized hardware needed — all heavy lifting is done remotely.

### 🧪 Installation Steps:

```bash
# 1. Clone the repository
git clone https://github.com/DeepRatAI/TrueEye_v1.git
cd TrueEye_v1

# 2. Install backend dependencies
pip install -r requirements.txt

# 3. Set the LangFlow API URL
export FLOW_API_URL="http://localhost:7860/predict"  # Adjust to your LangFlow instance

# 4. Start the FastAPI backend
uvicorn main:app --reload
```

Once the server is running, open the file `static/index.html` in your browser.
Paste a news article URL, click "Analyze", and you'll receive an AI-generated report.

---

## 📌 Roadmap

| Version  | Status     | Description                                                     |
| -------- | ---------- | --------------------------------------------------------------- |
| ✅ v1.0   | Production | Full text analysis with explainable AI (current version)        |
| 🔄 v2.0  | In design  | "TrueEye Chat": interactive conversation with persistent memory |
| 🖼️ v3.0 | Planned    | Multimodal reasoning (text + images/audio/video)                |
| 🧪 v4.0  | Planned    | Deepfake and synthetic content detection                        |

---

## 📚 Technologies Used

* **FastAPI** — Python web framework for REST APIs.
* **LangFlow** — Flow-based orchestration of LLMs and tools.
* **Claude (Opus / Sonnet)** — Large language models via Anthropic API.
* **TailwindCSS & JS** — Frontend interface styling and logic.
* **Docker** — Deployment (e.g. Hugging Face Spaces using provided Dockerfile).

---

## ✍️ Author

**Gonzalo Romero (DeepRat)**
AI, Software & Systems Engineer · Prompt Engineer · Full-Stack Developer

🔗 [Web](https://deeprat.tech) | [Hugging Face](https://huggingface.co/DeepRat) | [GitHub](https://github.com/DeepRatAI) | [LinkedIn](https://www.linkedin.com/in/deeprat) | [Medium](https://medium.com/@deeprat)

---

## 🧠 License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)** license.
You are free to share and adapt the code **as long as you credit the author (DeepRat)** and **do not use it for commercial purposes without permission**.

> For commercial use or extended licensing, please contact: [info@deeprat.tech](mailto:info@deeprat.tech)

---
