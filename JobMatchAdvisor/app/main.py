from fastapi import FastAPI, UploadFile, File, Body
from app.utils import extract_text_from_pdf
from app.storage import save_resume, save_job, get_resume, get_job
from app.match_graph import run_match

app = FastAPI()

@app.post("/resume")
async def upload_resume(file: UploadFile = File(...)):
    contents = await file.read()
    text = extract_text_from_pdf(contents)
    save_resume(text)
    return {"message": "Resume uploaded"}

@app.post("/job")
async def upload_job(file: UploadFile = File(...)):
    contents = await file.read()
    text = extract_text_from_pdf(contents)
    save_job(text)
    return {"message": "Job description uploaded"}

@app.post("/match")
def match():
    resume = get_resume()
    job = get_job()
    if not resume or not job:
       return {"error": "Resume and Job must be uploaded first"}
    
    result = run_match(resume, job)
    return {"message": "Match completed", "match_summary": result}