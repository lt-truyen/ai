from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from rag_pipeline import run_rag
import warnings

warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Medical RAG Assistant is running."}

@app.post("/query")
async def query_rag(request: Request):
    body = await request.json()
    question = body.get("question", "")
    print("Câu hỏi nhận được:", question)
    try:
        answer = run_rag(question)
        print("Câu trả lời:", answer)
        return {"answer": answer}
    except Exception as e:
        print("Lỗi khi xử lý RAG:", e)
        return {"error": str(e)}