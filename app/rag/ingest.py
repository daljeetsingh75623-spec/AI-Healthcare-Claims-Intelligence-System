from app.rag.chunking import split_text
from app.rag.vector_store import create_vector_store


def ingest_document(text: str, filename: str):

    chunks = split_text(text)

    metadata = []

    for index, _ in enumerate(chunks):
        metadata.append(
            {
                "source": filename,
                "chunk": index
            }
        )

    create_vector_store(
        chunks,
        metadata
    )

    return {
        "status": "indexed",
        "chunks": len(chunks)
    }