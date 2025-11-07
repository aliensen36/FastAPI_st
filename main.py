from fastapi import FastAPI

app = FastAPI()

item_id = 'foo'

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}