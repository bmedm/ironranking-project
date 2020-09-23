from src.app import app
from flask import request, Response
from src.helpers.json_response import asJsonResponse
import re
from src.database import db
from bson.json_util import dumps
import numpy as np

@app.route("/lab/create/<labname>")
def createlab(labname):
    res=db.pull.insert_one({"Lab": labname}).inserted_id
    return dumps(res)

@app.route("/lab/<lab_id>/meme")
def randommeme(lab_id):
    res=db.pull.aggregate([
        { "$match":  {"Lab":f'{lab_id}'} },
        { "$sample": {"size": 1} }, 
        { "$project" : { "Meme" : 1, "Teacher": 1,"_id":0}}
      ])
    return dumps(res)
