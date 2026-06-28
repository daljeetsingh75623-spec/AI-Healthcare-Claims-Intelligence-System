from openai import OpenAI

from app.core.config import settings


client = OpenAI(
    api_key=settings.NVIDIA_API_KEY,
    base_url=settings.BASE_URL
)


def ask_llm(prompt: str):

    response = client.chat.completions.create(
        model=settings.MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": "You are an expert healthcare insurance assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_tokens=500
    )

    return response.choices[0].message.content