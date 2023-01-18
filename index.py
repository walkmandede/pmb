from fastapi import FastAPI
from routes.user_route import * 
from routes.project_route import *
from routes.page_route import *
from routes.task_route import *

app = FastAPI()
app.include_router(user)
app.include_router(project)
app.include_router(page)
app.include_router(task)
