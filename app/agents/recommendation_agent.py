import json

from app.prompts.recommendation_prompt import RECOMMENDATION_PROMPT
from app.services.ai_service import AIService


def recommend_claim(
    context: str,
    coverage: dict,
    fraud: dict,
    missing_documents: dict
):

    prompt = RECOMMENDATION_PROMPT.format(
        context=context,
        coverage=json.dumps(coverage, indent=2),
        fraud=json.dumps(fraud, indent=2),
        missing_documents=json.dumps(
            missing_documents,
            indent=2
        )
    )

    response = AIService.generate(prompt)

    try:
        return json.loads(response)

    except Exception:

        return {
            "decision": "Manual Review",
            "confidence": 0,
            "reason": response
        }