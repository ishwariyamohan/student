from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi import Form
from fastapi import File
app = FastAPI()
templates = Jinja2Templates(directory="templates")
results = Jinja2Templates(directory="results")

@app.get("/Page", response_class=HTMLResponse)#http://127.0.0.1:8000/registerPage/
def show_service_page(request: Request):
    return templates.TemplateResponse("register.html", context={"request": request})


@app.get("/registerPage", response_class=HTMLResponse)#http://127.0.0.1:8000/registerPage/
def show_service_page(request: Request):
    return templates.TemplateResponse("register.html", context={"request": request})


@app.post("/register") #http://127.0.0.1:8000/register/
def user(name: str = Form(), email: str = Form(),mobile: str = Form(),dob: str = Form(),Password: str = Form()):
    """This service takes details from client and return a greeting msg"""
    
    file1 = open("response.txt","a")
    file1.write(name +" , "+ email+" , "+ str(mobile)+" , "+ str(dob)+" , "+Password+" , ")
    file1.write("\n")
    file1.close()

    return "Successfully Registered"

