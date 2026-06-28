import os
import shutil

from fastapi import APIRouter, UploadFile, File, HTTPException

from app.models.document import DocumentResponse
from app.services.pdf_service import extract_text
from app.rag.ingest import ingest_document

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload", response_model=DocumentResponse)
async def upload_pdf(file: UploadFile = File(...)):
    """
    Upload a healthcare claim or policy PDF,
    extract its text,
    chunk it,
    generate embeddings,
    and store it in the FAISS vector database.
    """

    # Validate file type
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    # Save uploaded file
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text from PDF
    result = extract_text(file_path)

    # Build FAISS vector database
    ingest_document(
        text=result["text"],
        filename=file.filename
    )

    return DocumentResponse(
        filename=file.filename,
        pages=result["pages"],
        status="Document indexed successfully."
    )