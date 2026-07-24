from fastapi import FastAPI , Path, Query, Body
from pydantic import EmailStr, BaseModel, Field

app = FastAPI()
@app.get("/")
async def read():
    return {"massage": "Hello Feilds"}


class Item(BaseModel):
    name : str
    description : str |None = Field(..., title="item feilds", description="this is a main topic for program", max_length= 190)
    price : float = Field(... , description="The price must be greater than 0", ge= 0)
    tax : float = Field(...)

@app.put("/items/{item_id}")
async def get_id(
        item_id : int ,
        item : Item = Body(..., embed=True)
):
    result = {"item_id": item_id, "item": item}
    return result