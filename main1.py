from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
from fastapi import Form
from typing import List
from fastapi.encoders import jsonable_encoder

app = FastAPI()

uri = "mongodb+srv://demo:Demo_123@cluster0.fh8rxgk.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client.school
rb = client.login

class Result(BaseModel):
   
    Roll_no: int
    Name:str
    Course :str
    Total_mark : int
    Percentage:int
    Status: str

@app.get("/api/result/findAll", response_model=List[Result])
def list_results():
    results = list(db["results"].find(limit=100))
    return results

@app.post("/api/result/create", response_model=List[Result])
def create_result(result: Result):
    result = jsonable_encoder(result)
    object_id = db["results"].insert_one(result)
    results = list(db["results"].find(limit=100))
    return results


@app.get("/api/result/findOne", response_model=Result)
def find_one(Roll_no: int):
    results = db["results"].find_one({"Roll_no": Roll_no})
    return results


@app.put("/api/result/update")
def update_result(Roll_no: int, results:Result ):
    result = jsonable_encoder(result)
    update_result = db["result"].update_one(
        {"Roll_no": Roll_no}, {"$set": result})
    return f"{Roll_no} updated successfully"


@app.delete("/api/result/delete")
def delete_result(Roll_no: int):
    delete_result = db["results"].delete_one({"Roll_no": Roll_no})
    return f"{Roll_no} deleted successfully"

class User(BaseModel):
    user_name:str
    password: int

@app.post("/processLogin")#http://127.0.0.1:8000/processLogin/
def check_user(request: Request, user_name: str = Form(), password: str = Form()):
    '''
    checking username and password
    '''
    user = rb["users"].find_one({"username": user_name})
    if user_name == user["users"] and password == user["password"] :
        return home.TemplateResponse("index1.html", context={"request": request})
    else:
        return "Unsuccessful sign_in"


