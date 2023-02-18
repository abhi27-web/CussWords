from fastapi import FastAPI
from better_profanity import profanity
from flask import jsonify
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Scoringitem(BaseModel):
    Text: str

@app.post('/')
async def scoring_endpoint(item:Scoringitem):
    output = profanity.censor(item.Text)
    return output


if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, reload=True, debug=True, workers=3)
