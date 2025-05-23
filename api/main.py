from fastapi import FastAPI,Query
import json
from pathlib import Path
from typing import List

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

@app.get("/marks")
def get_marks(name: List[str] = Query(...)):
    global d
    marks=[]
    for n in name:
        for i in d:
            if n == i["n"]:
                marks.append(i["marks"])
    return {"marks":marks}