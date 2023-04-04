# from fastapi import FastAPI,HTTPException
# from starlette.middleware.cors import CORSMiddleware

# from dataSchema import Application
# from src.main import ModelMain

# from databaseCont import (
#     createApplication,
#     getAllApplications,
#     getJobs

# )

# app = FastAPI()

# origins = ['http://127.0.0.1:5173','http://127.0.0.1:5174']


# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"]
# )

# # post controller



# @app.post("/api/application")
# async def post_application(application: Application):
#     Model = ModelMain()
#     print(application)
#     application.prediction = Model.runnerClass(application.answers[0])
#     response = await createApplication(application.dict())
#     if response:
#         return application.prediction

#     else:
#         raise HTTPException(404, "Something went wrong when adding")

# @app.get("/api/admin")
# async def get_applications():
#     response = await getAllApplications()
#     return response


# @app.get("/api/jobs")
# async def get_jobs():
#     respone = await getJobs()
#     return respone
