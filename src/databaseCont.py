# from dataSchema import Application
# from dataSchema import Job

import motor.motor_asyncio

from pydantic import BaseModel
class Application(BaseModel):
    id:int
    name: str
    address : str
    position: str
    cv: str
    answers: list
    prediction:list

class Job(BaseModel):
    jobrole: str
    company:str
    location:str
    worktype:str
    fullorparttime:str
    salary:str


client = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://courseDeveloper:test1234@cluster0.rm2r8il.mongodb.net/recruitment')

database = client.recruitment
collection = database.applications
jobCollection = database.jobs

async def createApplication(application):
    print(application)
    document = application
    result= await collection.insert_one(document)
    return result

async def getAllApplications():
    allApplications = []
    result = collection.find()
    print(result)
    async for application in result:
        allApplications.append(Application(**application))

    return allApplications


async def getJobs():
    allJobs = []
    result = jobCollection.find()
    print(result)
    async for jobs in result:
        allJobs.append(Job(**jobs))

    return allJobs

async def createJob(jobs):
    document = jobs
    result = await jobCollection.insert_one(document)
    return result


