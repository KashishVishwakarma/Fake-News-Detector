import pandas as pd
import numpy as np
import re
import string
import joblib
import nltk

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Download stopwords (only needed first time)
nltk.download("stopwords")

# Initialize stemmer and stopwords
stemmer = PorterStemmer()
stop_words = set(stopwords.words("english"))

# ---------------------------
# Load Dataset
# ---------------------------
fake = pd.read_csv("dataset/Fake.csv")
true = pd.read_csv("dataset/True.csv")

fake["label"] = 0
true["label"] = 1

df = pd.concat([fake, true], ignore_index=True)

# Shuffle dataset
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Keep only required columns
df = df[["text", "label"]]

# ---------------------------
# Text Cleaning Function
# ---------------------------
def clean_text(text):
    text = text.lower()

    text = re.sub(r"http\\S+", "", text)
    text = re.sub(r"www\\S+", "", text)
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

print("Cleaning text...")

df["text"] = df["text"].apply(clean_text)

# ---------------------------
# TF-IDF Vectorization
# ---------------------------
vectorizer = TfidfVectorizer(max_features=10000)

X = vectorizer.fit_transform(df["text"])
y = df["label"]

# ---------------------------
# Train/Test Split
# ---------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ---------------------------
# Train Model
# ---------------------------
model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

# ---------------------------
# Evaluation
# ---------------------------
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\nModel Accuracy:", round(accuracy * 100, 2), "%\n")

print(classification_report(y_test, predictions))

# ---------------------------
# Save Model
# ---------------------------
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("\nModel saved successfully!")
print("Generated files:")
print("✔ model.pkl")
print("✔ vectorizer.pkl")
