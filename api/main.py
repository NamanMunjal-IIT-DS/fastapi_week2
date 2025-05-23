from fastapi import FastAPI,Query
import json
from pathlib import Path
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://exam.sanand.workers.dev"],  # Use specific domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app = FastAPI()

DATA_FILE = Path(__file__).parent / "q-vercel-python.json"
f=open(DATA_FILE, "r")
data = json.load(f)
f.close()
    
global d
d=data

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI"}

@app.get("/api")
def get_marks(name: List[str] = Query(...)):
    global d
    marks=[]
    for n in name:
        for i in d:
            if n == i["name"]:
                marks.append(i["marks"])
    return {"marks":marks}