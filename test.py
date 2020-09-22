import re
import requests
import json
import os
from dotenv import load_dotenv
import pandas as pd
load_dotenv()

apiKey = os.getenv("ApiKeyGit")
print("WE HAVE APIKEY") if apiKey else print("NO APIKEY FOUND")

def get_lastpull(endpoint, apiKey=os.getenv("ApiKeyGit"), query_params={}):
    baseUrl = "https://api.github.com"
    url = f"{baseUrl}{endpoint}"
    headers = {"Authorization": f"token {apiKey}"}
    res = requests.get(url,params=query_params,headers=headers)
    data = res.json()
    return data



def get_gh_data(i, apiKey=os.getenv("ApiKeyGit")):
    
    url = f"https://api.github.com/repos/ironhack-datalabs/datamad0820/pulls/{i}"
    headers = {"Authorization": f"token {apiKey}"}
    res = requests.get(url, headers=headers)
    data = res.json()
    print(res.url)
    try:
        return{
            'Lab_id':data['id'],
            'Username':data['user']['login'],
            'User_id':data['user']['id'],
            'Lab':data['title'].replace(" ","").split("]")[0].strip("["),
            'State':data['state'],
            'Update':data['created_at'],
            'Closed':data['closed_at'],
            'Comment_url':data['comments_url']
        }
    except:
        return {"Lab_id": None}
        
lastdata=get_lastpull("/repos/ironhack-datalabs/datamad0820/pulls",query_params={"per_page":2})
last=lastdata[0]["number"]
int(last)

data = [get_gh_data(i) for i in range(1,3)]

def shared(comment):
    share=[]
    for i in comment:
        return share.append(re.findall(r"@\w*-?\w+" ,i["body"]))
    
def meme(comment):
    try:
        try:
            z = re.findall(r'https:.*jpg|.*png|.*jpeg',comment[0]['body'])
            z = str(z).split('(')
            z = z[1].split("'")
            return z[0]
        except: 
            z = re.findall(r'https:.*jpg|.*png|.*jpeg',comment[0]['body'])
            z = str(z).split('(')
            return z[0]
    except:
        return None
    
def union(datos1, datos2):
    for i in datos1:
        for x in datos2:
            i.update(x)
    return datos1
def teacher(comment):
    try:
        return comment[0]["user"]["login"]
    except:
        return None

def get_issues(x, apiKey=os.getenv("ApiKeyGit")):  
    url = f"https://api.github.com/repos/ironhack-datalabs/datamad0820/issues/{x}/comments"
    headers = {"Authorization": f"token {apiKey}"}
    res = requests.get(url, headers=headers)
    comment = res.json()
    print(res.url)
    return {"Teacher":teacher(comment),
            "Meme":meme(comment),
            "Collaborator":shared(comment)
            }

data2=[get_issues(i) for i in range(1,3)]

data=union(data,data2)


jsn=pd.DataFrame(data)
jsn.to_json('pulls.json',orient="records")

