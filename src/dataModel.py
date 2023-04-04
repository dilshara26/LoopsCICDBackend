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
