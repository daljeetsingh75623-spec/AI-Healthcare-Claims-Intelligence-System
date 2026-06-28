import json

from app.services.ai_service import AIService
from app.prompts.missing_prompt import MISSING_DOCUMENTS_PROMPT


def find_missing_documents(context: str):

    prompt = MISSING_DOCUMENTS_PROMPT.format(
        context=context
    )

    response = AIService.generate(prompt)

    try:
        return json.loads(response)

    except Exception:

        return {
            "missing_documents": [],
            "reason": response,
            "confidence": 0
        }