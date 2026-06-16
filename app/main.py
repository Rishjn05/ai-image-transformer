from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.prompt import router as prompt_router
from app.api.generate import router

app = FastAPI(
    title="AI Image Transformer",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/")
def home():

    return {
        "status": "running",
        "message": "AI Image Transformer API"
    }

app.include_router(prompt_router)