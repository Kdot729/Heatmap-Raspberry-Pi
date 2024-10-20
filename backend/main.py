from fastapi import FastAPI
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
Router = APIRouter()

@app.get("/")
def table():
        with open('data.json') as File:
            Data = json.load(File)

        return Data