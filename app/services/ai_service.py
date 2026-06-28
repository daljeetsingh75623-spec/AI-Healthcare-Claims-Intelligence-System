from app.llm.client import ask_llm


class AIService:
    """
    Centralized service for interacting with the LLM.
    """

    @staticmethod
    def generate(prompt: str):

        response = ask_llm(prompt)

        return response.strip()