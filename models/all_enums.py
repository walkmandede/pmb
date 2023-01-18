from enum import Enum

class TaskStatus(str,Enum):
    ToDo = 'ToDo'
    WaitingFor = 'WaitingFor'
    Doing = 'Doing'
    Done = 'Done'

    