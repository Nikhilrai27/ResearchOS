from fastapi import FastAPI
from app.api.v1.papers import router as papers_router
from app.core.database import Base,engine
from app.models.paper import Paper

app = FastAPI(
    title="ResearchOS",
    version="0.1.0",
    description="AI-Powered Research Operating System",
)
Base.metadata.create_all(bind=engine)

app.include_router(
    papers_router,
    prefix="/api/v1",
)


@app.get("/")
def root():
    return {"status": "healthy"}