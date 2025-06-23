_resume_text = None
_job_text = None

def save_resume(text: str):
    global _resume_text
    _resume_text = text

def save_job(text: str):
    global _job_text
    _job_text = text

def get_resume():
    return _resume_text

def get_job():
    return _job_text