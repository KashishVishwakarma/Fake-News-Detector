# Fake-News-Detector


# 🛡️ Fake News Detector API

A lightweight, high-performance REST API built with **Python** and **FastAPI** that uses AI transformer models to detect whether news article text is **REAL** or **FAKE**.


## 🌟 Features

* ⚡ **Fast Predictions**: Offloads text classification to high-accuracy transformer models.
* 📊 **Detailed Metrics**: Returns real/fake probabilities, confidence scores, and risk level indicators.
* 🚀 **Cloud Ready**: Optimized to run with minimal RAM (< 50 MB) on free cloud hosting services like Render or Railway.
* 🛠️ **OpenAPI Documentation**: Automatically generated interactive API documentation via Swagger UI.

---

## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/KashishVishwakarma/Fake-News-Detector.git
cd Fake-News-Detector

```

### 2. Set Up Virtual Environment

```bash
python -m venv venv

# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

### 4. Start the Server

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

```

Once running, visit `http://localhost:8000/docs` in your browser to test the API directly!

---

## 🌐 Live API Endpoints

The API is deployed and live on Render:

* **Base URL:** `[https://fake-news-detector-2-1jco.onrender.com](https://fake-news-detector-2-1jco.onrender.com)`
* **Interactive Docs:** `[https://fake-news-detector-2-1jco.onrender.com/docs](https://fake-news-detector-2-1jco.onrender.com/docs)`
* **Health Check:** `[https://fake-news-detector-2-1jco.onrender.com/health](https://fake-news-detector-2-1jco.onrender.com/health)`

---

## 📡 API Usage Example

### Request (`POST /predict`)

```json
{
  "title": "Breaking News Headline",
  "text": "The article body text goes here..."
}

```

### Response

```json
{
  "verdict": "REAL",
  "label_id": 1,
  "metrics": {
    "fake_probability": 0.05,
    "real_probability": 0.95,
    "confidence_score": 95.0
  },
  "processed_char_length": 34,
  "risk_level": "Low Risk / Credible"
}

```

---

## 🛠️ Tech Stack

* **Framework:** Python 3.11, FastAPI, Uvicorn, Pydantic
* **AI Model:** Hugging Face Serverless Inference API (RoBERTa Model)
* **Deployment:** Render (Docker container)
---
🌐Live Demo
Base url:
https://fake-news-detector-2-1jco.onrender.com
---
Interactive Docs:
https://fake-news-detector-2-1jco.onrender.com/docs
---
Health Check:
https://fake-news-detector-2-1jco.onrender.com/health
---
✍️Author:
----
Kashish Vishwakarma


