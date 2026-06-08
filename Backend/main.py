from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from dotenv import load_dotenv
import os

#from utils import get_rag_chain

load_dotenv()

# IMPORTANT: use relative path for production
# PDF_PATH = os.path.join(os.path.dirname(__file__), "NationalAIPolicy.pdf")

# rag_chain = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global rag_chain

    print("🚀 Starting AI Policy Assistant...")

    # try:
    #     rag_chain = get_rag_chain(PDF_PATH)
    #     print("✅ RAG Chain Loaded Successfully")
    # except Exception as e:
    #     print(f"❌ Failed to load RAG: {e}")
    #     rag_chain = None

    yield


app = FastAPI(lifespan=lifespan)


# (Optional safety)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ========================
# 🌐 FRONTEND ROUTE
# ========================
@app.get("/")
async def serve_frontend():
    return FileResponse("../frontend/original_index.html")


# ========================
# RAG API ENDPOINT
# ========================
# @app.post("/ask/")
# async def ask_question(question: str):
#     global rag_chain

#     if rag_chain is None:
#         raise HTTPException(status_code=500, detail="RAG not initialized")

#     try:
#         print(f"📩 Question: {question}")

#         response = rag_chain.invoke({"input": question})

#         return JSONResponse(content={
#             "answer": response["answer"]
#         })

#     except Exception as e:
#         print(f"❌ Error: {e}")
#         raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)