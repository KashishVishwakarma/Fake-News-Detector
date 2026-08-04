# Fake-News-Detector
# 📰 AI Fake News Detector

An AI-powered Fake News Detection web application built using **Flask**, **Scikit-learn**, **NLTK**, and **Logistic Regression**. Users can paste a news article, and the application predicts whether it is **Real** or **Fake** with a confidence score.

---

## 🚀 Features

- Fake vs Real News Detection
- TF-IDF Vectorization
- Logistic Regression Model
- Confidence Score
- Responsive Web Interface
- Render Deployment Ready

---

## 🛠️ Technologies Used

- Python 3.11
- Flask
- Scikit-learn
- Pandas
- NumPy
- NLTK
- Joblib
- HTML
- CSS
- JavaScript
- Gunicorn

---

## 📂 Project Structure

```
fake-news-detector/
│
├── app.py
├── train_model.py
├── requirements.txt
├── Procfile
├── render.yaml
├── runtime.txt
├── README.md
├── model.pkl
├── vectorizer.pkl
│
├── dataset/
│   ├── Fake.csv
│   └── True.csv
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

---

## 📥 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/fake-news-detector.git
```

Go to the project folder:

```bash
cd fake-news-detector
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Train the model:

```bash
python train_model.py
```

Run the Flask application:

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

## 🚀 Deploy on Render

1. Push the project to GitHub.
2. Log in to Render.
3. Create a **New Web Service**.
4. Connect your GitHub repository.
5. Render will automatically detect the `render.yaml` file.
6. Deploy the application.
7. Your app will be available at a Render URL.

---

## 📊 Machine Learning Pipeline

1. Load Dataset
2. Clean Text
3. Remove Stopwords
4. Apply Stemming
5. Convert Text using TF-IDF
6. Train Logistic Regression
7. Predict Fake or Real News

---

## 📈 Model

- Algorithm: Logistic Regression
- Feature Extraction: TF-IDF
- Evaluation Metrics:
  - Accuracy
  - Precision
  - Recall
  - F1-Score

---

## 📄 License

This project is created for educational and learning purposes.
