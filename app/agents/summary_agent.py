import json

from app.services.ai_service import AIService
from app.prompts.summary_prompt import SUMMARY_PROMPT


def summarize_claim(context: str):

    prompt = SUMMARY_PROMPT.format(
        context=context
    )

    response = AIService.generate(prompt)

    try:
        return json.loads(response)

    except Exception:

        return {
            "summary": response
        }