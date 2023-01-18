from pydantic import BaseModel
from models.all_enums import *

class UserModel(BaseModel):
    id : str
    email : str
    password : str

class LoginModel(BaseModel):
    email : str
    password : str

class ProjectModel(BaseModel):
    name : str
    dateTime : str

class PageModel(BaseModel):
    name : str
    group : str
    projectId : str
    remark : str

class TaskModel(BaseModel):
    projectId : str
    title : str
    description : str
    deployedTo : str
    remark : str
    dateTime : str
    status : TaskStatus