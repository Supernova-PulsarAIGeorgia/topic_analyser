from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from classifier import Classification

app = FastAPI()
topic_classifier = Classification('./model')
# transliterator = Transliterator()

class ClassifyBody(BaseModel):
    sentences: List[str]

@app.get("/hello")
async def root():
    return {"message": "Hello World!"}

@app.post("/classifier")
async def classifer(body:ClassifyBody):
    print(f'got sent {body.sentences}')
    sent = body.sentences
    print(sent)
    classifier_sent = topic_classifier.classify(sent)
    print(f'classify : {classifier_sent}')
    return {"classifier" : classifier_sent}