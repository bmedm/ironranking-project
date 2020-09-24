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


@app.route("/lab/<labname>/search")
def allOpenClose(labname):
    
    opened_pr = db.pull.find({"$and": [{"Lab":f"{labname}"},{"State": "open"}]}).count()
    closed_pr = db.pull.find({"$and": [{"Lab":f"{labname}"},{"State": "closed"}]}).count()
    meme=db.pull.find({"Lab":f"{labname}"}).distinct("Meme")
    timestamp=db.pull.find({"Lab":f"{labname}"})
        
    #db.collection.update( {}, {"$set": {"Correcion":{"$subtract":["$ISODate('Closed')","$ISODate('Update')"]}}}, {"upsert":False}, {"multi":True})
    #timestamp=db.pull.find({"Lab":f'{labname}'},{"Lab":1,"Correccion":1,"_id":0})

    res = {'-El numero de PR abiertas es:': opened_pr,
           '-El numero de PR cerradas es:': closed_pr,
           '-El porcentaje closed es:':f' {round(closed_pr/(opened_pr+closed_pr)*100,2)} %',
           '-El porcentaje open es:': f'{round(opened_pr/(opened_pr+closed_pr)*100,2)}%',
           '-La lista de memes únicos es:':meme
           }
    return dumps(res)










