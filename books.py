from fastapi import FastAPI

app = FastAPI()
from enum import Enum
BOOKS =[]

@app.get("/books/")
async def read_all_books():
    return {"massage":"Hello world i'm Eslam Elgmaal"}

@app.post("/post/") #deprecated= True "for stoping the operation "

async def post():
    return {"massage":"Hello world i'm Eslam Elgmaal"}

@app.put("/put/")  #, description="" (to add an description for the operation)
async def put():
    return {"massage":"this is Eslam Elgmaal put endpoint"}

@app.delete("/")
async def delete():
    return {"massage":"remove to the trash "}

@app.get("/user/1")
async def admin_path():
    return {"massage": "this is the admin wep "} # this is a static path we can use it for standard page like admin

@app.get("/user/{user_id}")
async def user_id(user_id : int):  # int for uneqc num for ID's
    return {"user_id":user_id}


@app.get("/users/{user_id}")
async def user_id(user_id : str): # str for string type only
    return {"user_id":user_id}

class User_list( str , Enum):
    admin = 1
    manager = 2
    user = 3

@app.get("/{user_type}/{user_id}")
async def get_user_id(user_type : User_list, user_id ):
    return {"user":{user_type.name, user_id}}