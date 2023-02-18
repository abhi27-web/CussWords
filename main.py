from fastapi import FastAPI
from flask import jsonify
from pydantic import BaseModel
from profanity_filter import ProfanityFilter


app = FastAPI()

class Scoringitem(BaseModel):
    Text: str

@app.post('/')
async def scoring_endpoint(item:Scoringitem):
    pf = ProfanityFilter()
    output = pf.censor(item.Text)
    return output
