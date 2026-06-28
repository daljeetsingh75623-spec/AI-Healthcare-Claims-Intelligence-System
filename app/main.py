from fastapi import FastAPI

from app.core.config import settings

from app.api.routes import router as chat_router
from app.api.upload import router as upload_router
from app.api.search import router as search_router

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    description="AI Healthcare Claims Intelligence System"
)

# Register Routes
app.include_router(chat_router)
app.include_router(upload_router)
app.include_router(search_router)


@app.get("/", tags=["Health"])
def home():
    return {
        "status": "running",
        "application": settings.APP_NAME,
        "version": "1.0.0",
        "message": "🚀 AI Healthcare Claims Intelligence System is running successfully."
    }


@app.get("/health", tags=["Health"])
def health():
    return {
        "status": "healthy"
    }