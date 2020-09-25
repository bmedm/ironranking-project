from src.app import app
from flask import request, Response
from src.helpers.json_response import asJsonResponse
import re
from src.database import db
from bson.json_util import dumps
import numpy as np
from datetime import datetime

@app.route("/lab/create/", defaults = {"labname": None})
@app.route("/lab/create/<labname>")
def createlab(labname):
    if labname == None:
        return {
            "status": "Error HTTP 400 (Bad Request)",
            "message": "Para crear un estudiante,please specify one"
        }
    else:
        res=db.pull.insert_one({"Lab": labname}).inserted_id
        return f'Se ha creado un nuevo registro --> "Lab": {labname}'

@app.route("/lab/<lab_id>/meme")
def randommeme(lab_id):
    lab=db.pull.find({"Lab":f"{lab_id}"})
    #lab=dumps(lab)
    if len(list(lab)) != 0:
       
        res=db.pull.aggregate([
            { "$match":  {"Lab":f'{lab_id}'} },
            { "$sample": {"size": 1} }, 
            { "$project" : { "Meme" : 1, "Teacher": 1,"_id":0}}
        ])
        return dumps(res)
    
    return {"Error":"No existe el Lab nombrado, introduce uno correcto por favor! :)"}



@app.route("/lab/<labname>/search")
def allStatistics(labname):
    lab=db.pull.find({"Lab":f"{labname}"})
    #lab=dumps(lab)
    if len(list(lab)) != 0:
        opened_pr = db.pull.find({"$and": [{"Lab":f"{labname}"},{"State": "open"}]}).count()
        closed_pr = db.pull.find({"$and": [{"Lab":f"{labname}"},{"State": "closed"}]}).count()
        meme=db.pull.find({"Lab":f"{labname}"}).distinct("Meme")
        grade_time = db.pull.find({"Lab":labname},{'Update':1,'Closed':1})
        grade_time_list=[]
        for i in grade_time:
            op = datetime.fromisoformat(i['Update'].replace('Z',''))
            cl = datetime.fromisoformat(i['Closed'].replace('Z',''))
            grade_time_list.append((cl-op).total_seconds())
   
        res = {'Open_pr': opened_pr,
               'Closed_pr': closed_pr,
               'percent_cl':f' {round(closed_pr/(opened_pr+closed_pr)*100,2)} %',
               'percent_op': f'{round(opened_pr/(opened_pr+closed_pr)*100,2)}%',
               'unique_memes':meme,
               'Timemax_correct': (f'{str(round(max(grade_time_list)/3600,2))}h'),
               'Timemin_correct': (f'{str(round(min(grade_time_list)/3600,2))}h'),
               'Timemean_correct': (f'{str(round(np.mean(grade_time_list)/3600,2))}h')
            }
        return res
    
    return {"Error":"No existe el Lab nombrado, introduce uno correcto por favor! :)"}






