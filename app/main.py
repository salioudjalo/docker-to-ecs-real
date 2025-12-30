from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def root():
    return {
        "service": "docker-to-ecs-real",
        "version": os.getenv("APP_VERSION", "dev")
    }