from fastapi import APIRouter, HTTPException
from bson import ObjectId
from db.db_services import *
from global_methods import *
from models.base_model import *
from datetime import *

task = APIRouter() 


@task.get("/task/getAll")
async def getAll():
        data = dbToList(getTasksDB({}))
        return data

@task.get("/task/thatProjectTasks/{projectId}")
async def getThatTask(projectId):
        data = dbToList(getTasksDB({"projectId":projectId}))
        return data

@task.post("/task/create")
async def create(taskModel: TaskModel):
        projects = dbToList(getProjectsDB())
        projectIds = []

        for eachProject in projects:
            projectIds.append(eachProject['_id'])
        
        if(taskModel.projectId in projectIds):
            createTaskDB(taskModel)
            return {"message" : "Okay"}
        else:
            raise HTTPException(status_code=400, detail="Invalid Project ID") 

@task.delete("/task/delete/{id}")
async def delete(id :str):
    result = deleteTaskDB(id)
    if(result.raw_result['n'] == 1):
        return {"message" : "Page Deleted Successfully"}
    else:
        raise HTTPException(status_code=400, detail="Error Deleting Page")

@task.put("/task/update/{id}")
async def update(id,taskModel: TaskModel):
        projects = dbToList(getProjectsDB())
        projectIds = []
        users = dbToList(getUsersDB({}))
        userIds = []
        for eachProject in projects:
            projectIds.append(eachProject['_id'])
        for eachData in users:
            userIds.append(eachData['_id'])
        

        superPrint(taskModel.deployedTo)
        if(taskModel.projectId not in projectIds):
            raise HTTPException(status_code=400, detail="Invalid Project ID")
        elif(taskModel.deployedTo != '' and taskModel.deployedTo not in userIds):
            raise HTTPException(status_code=400, detail="Invalid User ID")
        else:
            result = updateTaskDB(id,taskModel)
            return {"message" : "Okay","result" : dbToDict(result)}

