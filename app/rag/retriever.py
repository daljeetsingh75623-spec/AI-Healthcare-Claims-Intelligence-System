from app.rag.vector_store import load_vector_store


def retrieve_documents(
    question: str,
    k: int = 3
):

    db = load_vector_store()

    documents = db.similarity_search(
        question,
        k=k
    )

    return documents