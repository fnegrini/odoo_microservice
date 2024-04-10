from fastapi import BackgroundTasks, FastAPI

app = FastAPI()


def run_python_code():
    #Add log file: process started at
    #Run python code (try/catch)
    #Add log file: process finished at
    #Return result to Odoo sender
    pass
    

@app.post("/run/")
async def run_process(url:str, task_uid:str, code:str):
    return {"message": "Notification sent in the background"}