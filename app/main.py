from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

from app.bigram_model import BigramModel
from app.spacy_service import embed_word   # 👈 新增这一行

app = FastAPI()

corpus = [
    "The Count of Monte Cristo is a novel written by Alexandre Dumas.",
    "This is another example sentence",
    "We are generating text based on bigram probabilities",
    "Bigram models are simple but effective"
]
bigram_model = BigramModel(corpus)

class TextGenerationRequest(BaseModel):
    start_word: str
    length: int

class EmbeddingRequest(BaseModel):
    word: str

class EmbeddingResponse(BaseModel):
    word: str
    dim: int
    vector: List[float]

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Assignment 1 API is running"}

@app.post("/generate")
def generate_text(request: TextGenerationRequest):
    if request.length < 1:
        raise HTTPException(status_code=400, detail="length must be >= 1")
    generated_text = bigram_model.generate_text(request.start_word, request.length)
    return {"generated_text": generated_text}

# 👇 新增 embedding 接口
@app.post("/embed", response_model=EmbeddingResponse)
def get_embedding(req: EmbeddingRequest):
    vec = embed_word(req.word)
    return EmbeddingResponse(word=req.word, dim=len(vec), vector=vec)