from datetime import *

def superPrint(text):
    print(' - - - - - - - - - - - - -')
    print(text)
    print(' - - - - - - - - - - - - -')


def dbToDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

def dbToList(entity) -> list:
    return [dbToDict(a) for a in entity]

def validateDateTime(dateTimeString) -> bool:
    result = True
    try:
        datetime.strptime(dateTimeString, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        try:
            date = datetime.strptime(dateTimeString, '%Y-%m-%d %H:%M:%S.%f')
        except ValueError:
            result = False
    
    return result


