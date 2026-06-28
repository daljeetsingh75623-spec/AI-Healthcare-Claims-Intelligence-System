import os

from langchain_community.vectorstores import FAISS

from app.rag.embedding_service import get_embedding_model

VECTOR_DB_PATH = "vector_db"


def create_vector_store(chunks, metadata):

    embedding_model = get_embedding_model()

    db = FAISS.from_texts(
        texts=chunks,
        embedding=embedding_model,
        metadatas=metadata
    )

    os.makedirs(VECTOR_DB_PATH, exist_ok=True)

    db.save_local(VECTOR_DB_PATH)

    return db


def load_vector_store():

    embedding_model = get_embedding_model()

    return FAISS.load_local(
        VECTOR_DB_PATH,
        embedding_model,
        allow_dangerous_deserialization=True
    )