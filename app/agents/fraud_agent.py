import json

from app.prompts.fraud_prompt import FRAUD_PROMPT
from app.services.ai_service import AIService


def detect_fraud(context: str):

    prompt = FRAUD_PROMPT.format(
        context=context
    )

    response = AIService.generate(prompt)

    try:
        return json.loads(response)

    except Exception:

        return {
            "risk": "Unknown",
            "score": 0,
            "reasons": [response],
            "confidence": 0
        }