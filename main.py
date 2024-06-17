from fastapi import FastAPI
from models import User
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/analytics")
async def calc(user: User):
    return {"ans": "True"}
