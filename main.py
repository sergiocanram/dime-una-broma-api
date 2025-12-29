from dotenv import load_dotenv
load_dotenv()

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI


app = FastAPI()

@app.get("/")
def root():
    return {"msg": "API viva y con ganas de bromear"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://sergiodatos.com",
        "https://www.sergiodatos.com",
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class Req(BaseModel):
    w1: str
    w2: str
    w3: str

@app.post("/joke")
def joke(r: Req):
    prompt = f"Haz una broma corta y blanca en español usando: {r.w1}, {r.w2}, {r.w3}."
    out = client.responses.create(model="gpt-5-mini", input=prompt)
    return {"joke": out.output_text}
