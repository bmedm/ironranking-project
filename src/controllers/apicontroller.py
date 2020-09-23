from src.app import app
from flask import request, Response
from src.helpers.json_response import asJsonResponse
import re
from src.database import db
from bson.json_util import dumps


 
@app.route('/') 
def welcome():
    return {
        "status": "OK",
        "message": "Welcome to Ironranking"
    }

@app.route("/student/create/<studentname>")
def createStudent(studentname):
    res=db.pull.insert_one({"Username": studentname}).inserted_id
    return dumps(res)

@app.route("/student/all")
@asJsonResponse
def liststudent():
    res= db.pull.distinct("Username")
    return dumps(res)

