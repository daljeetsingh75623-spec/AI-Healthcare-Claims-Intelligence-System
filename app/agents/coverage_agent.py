import json

from app.services.ai_service import AIService
from app.prompts.coverage_prompt import COVERAGE_PROMPT


def check_coverage(context: str, question: str):

    prompt = COVERAGE_PROMPT.format(
        context=context,
        question=question
    )

    response = AIService.generate(prompt)

    try:
        return json.loads(response)

    except Exception:

        return {
            "covered": None,
            "coverage_type": None,
            "waiting_period": None,
            "max_limit": None,
            "deductible": None,
            "exclusions": [],
            "reason": response,
            "confidence": 0
        }