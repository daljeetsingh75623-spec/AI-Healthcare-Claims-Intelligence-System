from fastapi import FastAPI
from app.api.routes import router
from app.core.config import settings
from app.api.upload import router as upload_router

app = FastAPI(
    title=settings.APP_NAME
)

app.include_router(router)
app.include_router(upload_router)


@app.get("/")
def home():
    return {"message": "Healthcare Claims AI Running 🚀"}