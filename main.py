from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from pipeline import run_pipeline
import uvicorn

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.get("/", response_class=HTMLResponse)
def home():
    with open("templates/index.html", encoding="utf-8") as f:
        return f.read()

@app.post("/generate")
def generate(request: PromptRequest):
    result = run_pipeline(request.prompt)
    return result

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)