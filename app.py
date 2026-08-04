from flask import Flask, render_template, request
import joblib
import re
import string
import nltk

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download stopwords if not already present
nltk.download("stopwords")

app = Flask(__name__)

# Load trained model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Initialize stemmer and stopwords
stemmer = PorterStemmer()
stop_words = set(stopwords.words("english"))

# -----------------------------
# Text Cleaning Function
# -----------------------------
def clean_text(text):
    text = text.lower()

    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"www\S+", "", text)
    text = re.sub(r"<.*?>", "", text)

    text = re.sub("[%s]" % re.escape(string.punctuation), " ", text)
    text = re.sub(r"\d+", "", text)

    words = text.split()

    words = [
        stemmer.stem(word)
        for word in words
        if word not in stop_words
    ]

    return " ".join(words)

# -----------------------------
# Home Page
# -----------------------------
@app.route("/")
def home():
    return render_template(
        "index.html",
        prediction=None,
        confidence=None
    )

# -----------------------------
# Prediction Route
# -----------------------------
@app.route("/predict", methods=["POST"])
def predict():

    news = request.form.get("news", "").strip()

    if news == "":
        return render_template(
            "index.html",
            prediction="Please enter some news text.",
            confidence=None
        )

    cleaned = clean_text(news)

    vector = vectorizer.transform([cleaned])

    prediction = model.predict(vector)[0]

    probability = model.predict_proba(vector)[0]

    confidence = round(max(probability) * 100, 2)

    if prediction == 1:
        result = "🟢 Real News"
    else:
        result = "🔴 Fake News"

    return render_template(
        "index.html",
        prediction=result,
        confidence=confidence
    )

# -----------------------------
# Run Flask
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
