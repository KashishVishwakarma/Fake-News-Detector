from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import TextAnalysisRequest, TextAnalysisResponse
from app.model import classifier_engine
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("api")

app = FastAPI(
    title="Fake News Detection Microservice",
    description="High-performance REST API for automated text credibility assessment.",
    version="1.0.0"
)

# Enable CORS cross-origin access for web browser extension requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    """Health check endpoint to verify model readiness."""
    return {
        "status": "online",
        "model_loaded": classifier_engine.is_ready,
        "device": classifier_engine.device
    }

@app.post(
    "/predict",
    response_model=TextAnalysisResponse,
    status_code=status.HTTP_200_OK
)
async def analyze_news_content(payload: TextAnalysisRequest):
    """
    Main endpoint for analyzing article text. Accepts extracted page contents
    and returns classification scores along with risk indicators.
    """
    if not payload.text or len(payload.text.strip()) < 10:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Provided text payload is too short for meaningful analysis."
        )

    try:
        result = classifier_engine.predict(title=payload.title or "", text=payload.text)
        return result
    except Exception as e:
        logger.error(f"Inference error encountered: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Inference process failed: {str(e)}"
        )
