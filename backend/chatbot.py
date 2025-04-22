
from fastapi import APIRouter
from pydantic import BaseModel
from transformers import pipeline

router = APIRouter()

qa_pipeline = pipeline("text-generation", model="gpt2")

class ChatRequest(BaseModel):
    message: str

@router.post("/")
def chat(request: ChatRequest):
    response = qa_pipeline(request.message, max_length=100, do_sample=True)[0]['generated_text']
    return {"response": response}
