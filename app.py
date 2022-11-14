from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, Text
from datetime import datetime


app = FastAPI()
posts =[]
#Model post 
class Post(BaseModel):
    Id:Optional[str]
    Title:str
    Author:str
    Content:Text
    Created_at: datetime = datetime.now()
    Published_at:Optional[datetime]
    Published: bool = False
    
@app.get('/')
def Root():
    return {"Welcome": "Api with fastapi"}
@app.get('/post')
def get_post():
    return posts
@app.post('/post')
def getsave(post:Post):
    posts.append(post.dict())
    return "success post save"
        
