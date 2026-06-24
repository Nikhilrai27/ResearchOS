from fastapi import FastAPI
from app.api.upload import router as upload_router

app = FastAPI(
    title="ResearchOS",
    version="0.1.0",
    description="AI-Powered Research Operating System",
)

app.include_router(upload_router)


@app.get("/")
def root():
    return {"status": "healthy"}