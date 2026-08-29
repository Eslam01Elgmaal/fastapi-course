from fastapi import FastAPI, Request, status
from .models import Base
from .database import engine
from TodoApp.routers import auth, todos, admin, users
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from pathlib import Path

app = FastAPI()

Base.metadata.create_all(bind=engine)

BASE_DIR = Path(__file__).resolve().parent

app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static"
)
@app.get("/")
def main_rout(request: Request):
    return RedirectResponse(url="/todos/todo-page", status_code=status.HTTP_302_FOUND)



app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)




