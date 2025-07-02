from fastapi import FastAPI, Request, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from chatbot import generate_response
from rag_utils import ingest_text
import pdfplumber

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def index():
    return FileResponse("static/index.html")

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    msg = data.get("message", "").strip()
    if not msg:
        return {"response": "Please enter a message."}
    return {"response": generate_response(msg)}

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    content = await file.read()
    text = ""

    if file.filename.endswith(".txt"):
        text = content.decode("utf-8")
    elif file.filename.endswith(".pdf"):
        try:
            with pdfplumber.open(file.file) as pdf:
                text = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
        except Exception as e:
            return {"status": f"Error processing PDF: {e}"}
    else:
        return {"status": "Unsupported file type"}

    try:
        ingest_text(text, doc_id=file.filename)
        return {"status": "File ingested successfully"}
    except Exception as e:
        # Handle potential errors from ChromaDB (e.g., duplicate ID)
        return {"status": f"Error ingesting file: {e}"}