from fastapi import FastAPI
import uvicorn

#FastAPI 객체 생성
app = FastAPI()

# "/"로 접근하면 return을 보여줌
@app.get("/")
def read_root():
    return {"Hello":"Junwon"}

@app.get("/users/{user_id}")
def get_user(user_id):
    return {"user_id": user_id}

if __name__=='__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)