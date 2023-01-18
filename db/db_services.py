import pymongo
from global_env import *
from global_methods import superPrint
from bson.objectid import *


myclient = pymongo.MongoClient(f"mongodb+srv://{dbUserName}:{dbPassword}@cluster0.qag8tm8.mongodb.net/test")
pmb = myclient.pmb
userCollection = pmb['users']
projectCollection = pmb['projects']
pageCollection = pmb['pages']
taskCollection = pmb['tasks']


#users
def createUserDB(userModel):
    objId = userCollection.insert_one(dict(userModel))
    return objId

def getUsersDB(filter):
    return userCollection.find({},filter)


#projects
def createProjectDB(projectModel):
    objId = projectCollection.insert_one(dict(projectModel))
    return objId

def getProjectsDB():
    return projectCollection.find()

def deleteProjectDB(projectId : str):
    return projectCollection.delete_one({"_id":ObjectId(projectId)})


#pages
def createPageDB(pageModel):
    objId = pageCollection.insert_one(dict(pageModel))
    return objId

def getPagesDB():
    return pageCollection.find()

def deletePageDB(pageId : str):
    return pageCollection.delete_one({"_id":ObjectId(pageId)})

#tasks
def createTaskDB(taskModel):
    objId = taskCollection.insert_one(dict(taskModel))
    return objId

def getTasksDB(filter):
    return taskCollection.find(filter)

def deleteTaskDB(taskId : str):
    return taskCollection.delete_one({"_id":ObjectId(taskId)})

def updateTaskDB(taskId : str ,taskModel):
    return taskCollection.find_one_and_update(
        {"_id":ObjectId(taskId)},
        {"$set" : dict(taskModel)}
    )

