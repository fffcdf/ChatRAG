from fastapi import FastAPI
from pydantic import BaseModel
from main import chain

app=FastAPI(title='Company RAG')

class QueryRequest(BaseModel):
    query:str

@app.post("/ask/")
async def ask_question(request:QueryRequest):
    answer=chain.invoke({'question':request.query})
    return answer
