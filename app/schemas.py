from pydantic import BaseModel, Field
from typing import Optional

class TextAnalysisRequest(BaseModel):
    title: Optional[str] = Field(default="", description="Headline or title of the news article.")
    text: str = Field(..., min_length=10, description="Main text body of the article.")
    url: Optional[str] = Field(default=None, description="Canonical URL of the source page.")

class CredibilityMetrics(BaseModel):
    fake_probability: float = Field(..., ge=0.0, le=1.0)
    real_probability: float = Field(..., ge=0.0, le=1.0)
    confidence_score: float = Field(..., ge=0.0, le=100.0)

class TextAnalysisResponse(BaseModel):
    verdict: str = Field(..., description="Classification output: 'REAL' or 'FAKE'")
    label_id: int = Field(..., description="Numeric class label: 0 for Fake, 1 for Real")
    metrics: CredibilityMetrics
    processed_char_length: int
    risk_level: str = Field(..., description="Categorical risk rating: Low, Moderate, High")
