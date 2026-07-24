from fastapi import FastAPI , Path, Query
from pydantic import EmailStr, BaseModel

app = FastAPI()
@app.get("/")
async def root():
    return {"massage":"string validation"}


@app.get("/items")
async def validate_items(name: str = Query(... , min_length=3 , max_length=30 ,pattern=r"^[A-Za-z ]+$"),
                         email: EmailStr = Query(..., max_length=70),
                           ):
    return {"Name": name , "Email": email}



@app.get("/items/price")
async def get_price(
            min_price: float = Query(..., ge= 1, description="the price must greater than 0"),
            max_price: float = Query(..., le=200, description="the price must be less than 200 ")
        ):
    return {"minimum price":min_price, "maximum price":max_price}



@app.get("/items/{item_id}")
async def get_id(item_id: int = Path(..., ge= 1, le=1000,)):   #this is for all intagers greater than 0
    return {"item id":item_id}

class Item (BaseModel):
    name : str
    description : str
    price : float

class User (BaseModel):
    username : str
    full_name : str
    age : int

@app.put("/item/{item_id}")
async def item_update(
        *,
        item_id : int = Path(..., title="this is id", ge=0, le=100),
        query :str | None = None,
        item : Item | None = None,
        user : User | None = None

):
    result = {"item_id": item_id}
    if query:
        result.update({"query": query})
    if item:
        result.update({"item":item})

    if user:
        result.update({"user":user})

    return result
