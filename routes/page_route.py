from fastapi import APIRouter, HTTPException
from bson import ObjectId
from db.db_services import *
from global_methods import *
from models.base_model import *
from datetime import *

page = APIRouter() 


@page.get("/page/getAllPages")
async def getAllPages():
        pages = dbToList(getPagesDB())
        return pages

@page.post("/page/create")
async def pageCreate(pageModel: PageModel):
        projects = dbToList(getProjectsDB())
        projectIds = []

        for eachProject in projects:
            projectIds.append(eachProject['_id'])
        
        if(pageModel.projectId in projectIds):
            createPageDB(pageModel)
            return {"message" : "Okay"}
        else:
            raise HTTPException(status_code=400, detail="Invalid Project ID") 

@page.delete("/page/delete/{id}")
async def delete(id :str):
    result = deletePageDB(id)
    if(result.raw_result['n'] == 1):
        return {"message" : "Page Deleted Successfully"}
    else:
        raise HTTPException(status_code=400, detail="Error Deleting Page")

