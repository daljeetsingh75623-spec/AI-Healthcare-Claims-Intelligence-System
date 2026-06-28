from app.rag.retriever import retrieve_documents
from app.llm.client import ask_llm


def ask_rag(question: str):

    docs = retrieve_documents(question)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = f"""
You are an expert Healthcare Claims AI Assistant.

Rules:
- Answer ONLY using the provided context.
- Never invent information.
- If the answer is not present in the context, clearly say:
  "The uploaded document does not contain this information."
- Be concise and professional.

Context:
{context}

Question:
{question}

Answer:
"""

    return ask_llm(prompt)