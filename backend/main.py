from fastapi import FastAPI
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from query import Calculate_Sum

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
    return {"Data": Calculate_Sum()}