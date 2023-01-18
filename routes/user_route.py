from fastapi import APIRouter, HTTPException
from bson import ObjectId
from db.db_services import *
from global_methods import *
from models.base_model import *

user = APIRouter() 


@user.post("/users/register")
async def register(userModel: UserModel):
        objId = createUserDB(userModel)
        return {"message" : "Account Created Successfully"}

@user.post("/users/login")
async def login(loginModel: LoginModel):
    users = dbToList(getUsersDB({}))
    result = {}
    xSuccess = False
    for user in users:
        if(user['email'] == loginModel.email and user['password'] == loginModel.password):
            xSuccess = True
            result['id'] = user['_id']
            result['email'] = user['email']
            break
    if(xSuccess):
        return {
            "message" : "Login Successfully",
            "profile" : result
            }
    else:
        raise HTTPException(status_code=400, detail="Invalid Login") 

@user.get("/user/getAllUsers")
async def getAllUsers():
    users = dbToList(getUsersDB({"password":0}))
    return users

# @user.get('/{id}')
# async def find_one_user(id):
#     return serializeDict(conn.local.user.find_one({"_id":ObjectId(id)}))

# @user.post('/')
# async def create_user(user: User):
#     conn.local.user.insert_one(dict(user))
#     return serializeList(conn.local.user.find())
  
# @user.put('/{id}')
# async def update_user(id,user: User):
#     conn.local.user.find_one_and_update({"_id":ObjectId(id)},{
#         "$set":dict(user)
#     })
#     return serializeDict(conn.local.user.find_one({"_id":ObjectId(id)}))

# @user.delete('/{id}')
# async def delete_user(id,user: User):
#     return serializeDict(conn.local.user.find_one_and_delete({"_id":ObjectId(id)}))