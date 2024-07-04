import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


from mylib.bot import scrape

app = FastAPI()

class Wiki(BaseModel):
    name: str
    length: int

@app.get("/")
async def root():
    return {"message": "Welcome to the Wikipedia API!"}

@app.post("/wiki/")
async def fetch_item(wiki: Wiki):
    result = scrape(wiki.name, wiki.length)
    payload = {"wikipage": result}
    return JSONResponse(content=jsonable_encoder(payload))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

