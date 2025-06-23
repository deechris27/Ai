from fastapi import FastAPI, UploadFile, File, Body
from app.graph import run_graph
from app.storage import get_summary, update_summary, delete_key, save_summary
from app.chat import chat_over_summary

app = FastAPI()

@app.post("/upload")
async def upload_file(file: UploadFile=File(...)):
    contents = await file.read()
    result = run_graph(file.filename, contents)
    if result:
        save_summary(result)
    return {"message": "Processed", "summary": result}

@app.get("/summary")
def read_summary():
    return get_summary()

@app.put("/summary")
def update(key: str, val:str):
    return update_summary(key, val)

@app.delete("/summary")
def delete(key: str):
    return delete_key(key)

@app.post("/chat")
def chat(query: str = Body(..., embed=True)):
    summary = get_summary()
    if not summary:
        return "Error: No summary found. Upload a document first"
    answer = chat_over_summary(query, summary)
    return {"question": query, "answer": answer}

