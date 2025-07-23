from fastapi import FastAPI, HTTPException, UploadFile, File, Request
from pydantic import BaseModel

app = FastAPI()

items = {1: {"name": "Apple"}, 2: {"name": "Banana"}}

class Item(BaseModel):
    name: str
    description: str = None

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

@app.get("/search/")
def search_item(q: str = None):
    return {"query": q}

@app.post("/items/")
async def create_item(item: Item):
    return {"item": item}

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}
