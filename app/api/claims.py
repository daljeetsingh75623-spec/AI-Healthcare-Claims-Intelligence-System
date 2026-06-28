from fastapi import APIRouter
from pydantic import BaseModel

from app.agents.claims_workflow import analyze_claim


router = APIRouter(
    prefix="/claims",
    tags=["Claims Intelligence"]
)


class ClaimAnalysisRequest(BaseModel):
    question: str


@router.post("/analyze")
def analyze(request: ClaimAnalysisRequest):
    """
    Analyze uploaded healthcare claim documents using
    multiple AI agents.
    """

    result = analyze_claim(request.question)

    return result