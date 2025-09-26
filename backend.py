from fastapi import FastAPI, Body, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from summarizer import agent  # Your LangGraph / summarizer agent
import asyncio

app = FastAPI(
    title="Host JSON Summarizer API",
    description="Accepts host dataset JSON as a string and returns concise summaries per host",
    version="1.0.0",
)

# Enable CORS for all domains (adjust origins in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Host JSON Summarizer API is running."}

@app.post("/summarize")
async def summarize(data: dict = Body(...)):
    initial_state = {"host_data": data}
    loop = asyncio.get_running_loop()
    final_state = await loop.run_in_executor(None, agent.invoke, initial_state)
    return {"summary": final_state['summary']}

