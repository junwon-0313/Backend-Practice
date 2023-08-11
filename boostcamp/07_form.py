from fastapi import FastAPI, Form,Request
from fastapi.templating import Jinja2Templates

import uvicorn

app =FastAPI()
templates = Jinja2Templates(directory='./')
#url로 접근 시에는 get방식!!
@app.get("/login/")
def get_login_form(request: Request):
    return templates.TemplateResponse('login_form.html', context={'request':request})
#제출 버튼을 눌러 post요청을 함. 
@app.post("/login/")
def login(username: str = Form(...), password:str = Form(...)):
    return {"user_name":username, "password": password}

if __name__=='__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)