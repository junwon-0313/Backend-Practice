from fastapi import FastAPI
import uvicorn

app = FastAPI()

fake_items_db = [{"items_name": "Foo"},{"items_name": "Bar"},{"items_name": "Baz"}]

# http://0.0.0.0:8000/items?skip=0&limit=1
@app.get("/items")
def read_item(skip: int=0, limit:int =10):
    return  fake_items_db[skip: skip +limit]

if __name__=='__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)