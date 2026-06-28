from pydantic import BaseModel

class DocumentResponse(BaseModel):
    filename: str
    pages: int
    extracted_text: str