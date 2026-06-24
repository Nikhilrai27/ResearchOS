from fastapi import FastAPI

app = FastAPI(
    title="ResearchOS",
    version="0.1.0",
    description="AI-Powered Research Operating System",
)


@app.get("/")
def root():
    return {"status": "healthy"}