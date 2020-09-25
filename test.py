import re
import requests
import json
import os
from dotenv import load_dotenv
import pandas as pd
load_dotenv()
#obtenemos apiKey para GitHub
apiKey = os.getenv("ApiKeyGit")
print("WE HAVE APIKEY") if apiKey else print("NO APIKEY FOUND")
#Definimos las diferentes funciones para obtener información de la api de GitHub

def meme(comment):
    """
    Limpia de la api el comentario para obtener solamente la URL 
    del meme
    """
    try:
        meme=[]
        for i in comment:
            meme.append(re.findall(r"https:.*png|.*jpg" ,i["body"]))
        
        for i in meme:
            for x in i:
                x=x.split("]")
                if len(x)>1:
                    x=x[1].strip("(")
                else:
                    x=x[0]
        return x
    except:
        return None
def shared(comment):
    """
    Limpia de la api el comentario para obtener solamente el usuario
    con el que ha trabajado el estudiante
    """
    try:
        share=[]
        for i in comment:
            share.append(re.findall(r"@\w*-?\w+" ,i["body"]))
        return share
    except:
        return None 

def teacher(comment):
    """
    Obtiene el nombre de usuario del profesor que corrige cada pull request
    """
    teacher=[]
    try:
        for i in comment:
            teacher.append(i["user"]["login"])
        return teacher[0]
    except:
        return None

def get_issues(x, apiKey=os.getenv("ApiKeyGit")):
    """
    Hace la llamada a la api, concretamente al comentario de la pull request
    """
    url = f"https://api.github.com/repos/ironhack-datalabs/datamad0820/issues/{x}/comments"
    headers = {"Authorization": f"token {apiKey}"}
    res = requests.get(url, headers=headers)
    comment = res.json()
    print(res.url)
    return comment

def get_lastpull(endpoint, apiKey=os.getenv("ApiKeyGit"), query_params={}):
    """
    LLama a la api de GitHub
    """
    baseUrl = "https://api.github.com"
    url = f"{baseUrl}{endpoint}"
    headers = {"Authorization": f"token {apiKey}"}
    res = requests.get(url,params=query_params,headers=headers)
    data = res.json()
    return data

def get_gh_data(i, apiKey=os.getenv("ApiKeyGit")):
    """
    LLama a la api e iteramos por ella para obtener todas los datos
    para nuestra base de datos
    """
    
    url = f"https://api.github.com/repos/ironhack-datalabs/datamad0820/pulls/{i}"
    headers = {"Authorization": f"token {apiKey}"}
    res = requests.get(url, headers=headers)
    data = res.json()
    print(res.url)
    comment= get_issues(i)
    try:
        return{
            'Lab_id':data['id'],
            'Lab_number':data['number'],
            'Username':data['user']['login'],
            'User_id':data['user']['id'],
            'Lab':data['title'].replace(" ","").split("]")[0].strip("["),
            'State':data['state'],
            'Update':data['created_at'],
            'Closed':data['closed_at'],
            'Comment_url':data['comments_url'],
            'Teacher':teacher(comment),
            'Meme':meme(comment),
            'Collaborator':shared(comment)
            
            }
    except:
        return {"Lab_id": None}

lastdata=get_lastpull("/repos/ironhack-datalabs/datamad0820/pulls",query_params={"per_page":2})
last=lastdata[0]["number"]
int(last)
        
data = [get_gh_data(i) for i in range(1,(last+1))]


