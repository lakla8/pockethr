from fastapi import FastAPI
from openai_moment import analysis, statistics, goal

app = FastAPI(docs_url='/')



@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/strategy")
async def calc():
    return {"ans": analysis()}


@app.post("/analytics")
async def future(stats: dict) -> dict:
    result = statistics(stats)
    return {
        "predicted points": result[0],
        "small commentary": result[1]
    }


@app.post("/goal")
async def maybe(information: dict) -> dict:
    result = goal(information)
    return {'ans': result}



