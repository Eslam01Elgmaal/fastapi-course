from fastapi import FastAPI
from pydantic import  BaseModel
app = FastAPI()

@app.get("/")
async def rade_me():
    return {"massage": "hello Eslam"}

items = [
    {"id":1 , "name":"book" , "price":15 , "stock": True},
    {"id":2 , "name":"game" , "price":50 , "stock": True},
    {"id":3 , "name":"cd" , "price":30 , "stock": True},
    {"id":4 , "name":"magazine" , "price":10 , "stock": False},
    {"id":5 , "name":"book" , "price":10 , "stock": True},
    {"id":6 , "name":"game" , "price":10 , "stock": True}
]

@app.get("/items")
async def find_by_id_in_query1(
        start : int = 0,
        end : int = 10,
        id : int = None,
        name : str = None,
        price : int = None

):

    if id:
        item = next((item for item in items if item ["id"]== id),None)
        if item :
            return item
        else :
            return {"massage":"no item found "}
    if name :
        filtered = []
        for item in items :
            if item["name"] == name:
                filtered.append(item)

        return filtered
    if price :
        get_price = []
        for item in items :
            if item["price"] == price:
                get_price.append(item)

        return get_price


    return items[start : start+end]


@app.get("/items/price")
async def sort_price(range : int = None):
    sorted_price = sorted(items , key= lambda  x:x["price"], reverse= True)

    if range :
        price_range = [item for item in sorted_price if item["price"] <= range]
        return price_range

    else :
        return sorted_price


@app.get("/items/in_stock")
async def stock_items(in_stock: bool =True):
    if not in_stock :
        item = [item for item in items if item["stock"]== False]

        return item

    else:
        item = [item for item in items if item["stock"] == True]
        return item



class Items(BaseModel):
    name : str
    description : str | None = None
    price : float
    tax : float | None = None

@app.post("/create")
async def create_item(item:Items):
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax = item.price * (item.price*item.tax)
        item_dict.update({"total price": price_with_tax})

    return item_dict








# @app.get("/items")
# async def find_by_id_in_query2(id : int):
#     items_to_return = []
#     for item in items:
#         if item.get("id").casefold() == id.casefold():
#             items_to_return.append(item)
#
#     return items_to_return


