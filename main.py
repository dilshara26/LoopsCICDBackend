from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.dataSchema import Application
from src.dataSchema import Job
from src.main import ModelMain

from src.databaseCont import (
    createApplication,
    getAllApplications,
    getJobs,
    createJob

)

import nltk
nltk.download('punkt')

nltk.download('stopwords')


nltk.download('wordnet')

app = FastAPI()

origins = ['http://127.0.0.1:5173','http://127.0.0.1:5174','https://eclectic-cocada-9a268d.netlify.app','https://eclectic-cocada-9a268d.netlify.app']


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# post controller



@app.post("/api/application")
async def post_application(application: Application):
    Model = ModelMain()
    print(application)
    application.prediction = Model.runnerClass(application.answers[0])
    response = await createApplication(application.dict())
    if response:
        return application.prediction

@app.get("/api/admin")
async def get_applications():
    response = await getAllApplications()
    return response


@app.get("/api/jobs")
async def get_jobs():
    respone = await getJobs()
    return respone
# post jobs

@app.post("/api/jobs")
async def post_jobs(jobs:Job):
    response = await createJob(jobs.dict())
    if response:
        return response




