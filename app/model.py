import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import logging

logger = logging.getLogger("fake_news_detector")

class NewsClassifierEngine:
    """
    Production wrapper for Transformer-based text classification.
    Loads fine-tuned sequence classification models for real-time inference.
    """
    def __init__(self, model_name: str = "hamzab/roberta-fake-news-classification"):
        self.model_name = model_name
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        logger.info(f"Initializing inference engine on device: {self.device}")
        
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            self.model = AutoModelForSequenceClassification.from_pretrained(self.model_name)
            self.model.to(self.device)
            self.model.eval()
            self.is_ready = True
        except Exception as e:
            logger.error(f"Failed to load Transformer model {self.model_name}: {str(e)}")
            self.is_ready = False

    def predict(self, title: str, text: str) -> dict:
        if not self.is_ready:
            raise RuntimeError("Model pipeline is not properly initialized.")

        # Combine title and article body for complete context evaluation
        combined_text = f"{title.strip()} {text.strip()}".strip()
        
        # Tokenize payload with truncation matching standard model context limits
        inputs = self.tokenizer(
            combined_text,
            max_length=512,
            padding="max_length",
            truncation=True,
            return_tensors="pt"
        ).to(self.device)

        with torch.no_grad():
            outputs = self.model(**inputs)
            logits = outputs.logits
            probabilities = torch.softmax(logits, dim=-1).squeeze().tolist()

        if isinstance(probabilities, float):
            fake_prob = 1.0 - probabilities
            real_prob = probabilities
        else:
            fake_prob = float(probabilities[0])
            real_prob = float(probabilities[1])

        label_id = 1 if real_prob >= 0.50 else 0
        verdict = "REAL" if label_id == 1 else "FAKE"
        confidence = max(fake_prob, real_prob) * 100.0

        if fake_prob >= 0.75:
            risk_level = "High Misinformation Risk"
        elif fake_prob >= 0.45:
            risk_level = "Moderate Uncertainty"
        else:
            risk_level = "Low Risk / Credible"

        return {
            "verdict": verdict,
            "label_id": label_id,
            "metrics": {
                "fake_probability": round(fake_prob, 4),
                "real_probability": round(real_prob, 4),
                "confidence_score": round(confidence, 2)
            },
            "processed_char_length": len(combined_text),
            "risk_level": risk_level
        }

classifier_engine = NewsClassifierEngine()
