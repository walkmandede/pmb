from fastapi import APIRouter, HTTPException
from bson import ObjectId
from db.db_services import *
from global_methods import *
from models.base_model import *
from datetime import *

project = APIRouter() 


@project.get("/project/getAllProjects")
async def getAllProjects():
        projects = dbToList(getProjectsDB())
        return projects

@project.post("/project/create")
async def register(projectModel: ProjectModel):
        dt = datetime.now()
        xValidDateTime = validateDateTime(projectModel.dateTime)

        if(xValidDateTime != True):
            raise HTTPException(status_code=400, detail="Invalid Date Format") 
        else:
            objId = createProjectDB(projectModel)
            return {"message" : "Project Created Successfully"}

@project.delete("/project/delete/{id}")
async def delete(id :str):
    result = deleteProjectDB(id)
    if(result.raw_result['n'] == 1):
        return {"message" : "Project Deleted Successfully"}
    else:
        raise HTTPException(status_code=400, detail="Error Deleting Project")

