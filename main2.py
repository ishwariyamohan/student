from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
from typing import List
from fastapi.encoders import jsonable_encoder

app = FastAPI()

uri = "mongodb+srv://demo:Demo_123@cluster0.fh8rxgk.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client.school


class Student(BaseModel):
   
    roll_no: int
    sub1:int
    sub2 :int
    sub3 : int
    sub4:int
    sub5: int
    sub6:int
    Total_mark:int
    status:str

@app.get("/api/student/findAll", response_model=List[Student])
def list_students():
    students = list(db["students"].find(limit=100))
    return students

@app.post("/api/student/create", response_model=List[Student])
def create_student(result: Student):
    student = jsonable_encoder(student)
    object_id = db["students"].insert_one(student)
    students = list(db["students"].find(limit=100))
    return students


@app.get("/api/student/findOne", response_model=Student)
def find_one(roll_no: int):
    students = db["students"].find_one({"roll_no": roll_no})
    return students


@app.put("/api/student/update")
def update_student(roll_no: int, results:Result ):
    student = jsonable_encoder(student)
    update_student = db["student"].update_one(
        {"roll_no": roll_no}, {"$set": student})
    return f"{roll_no} updated successfully"


@app.delete("/api/student/delete")
def delete_student(roll_no: int):
    delete_student = db["students"].delete_one({"roll_no": roll_no})
    return f"{roll_no} deleted successfully"




