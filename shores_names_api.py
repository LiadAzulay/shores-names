import pymongo
from fastapi import FastAPI
import re
from fastapi.middleware.cors import CORSMiddleware

# Connecting to DB 
mydb = pymongo.MongoClient('mongodb+srv://user:user@beachme.c5sbvhv.mongodb.net/?retryWrites=true&w=majority')["beachme-1"]
# Fetching "Shores"
shore_db = mydb.shores_names
# Creating api
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Get all shores on db
@app.get("/get_shores_names/{shore_starts}")
async def root(shore_starts):
    pat = re.compile(shore_starts, re.I)

    shores = list(shore_db.find({ "shore_name": {'$regex': pat}}))
    for shore in shores:
        del shore['_id']
    print(shores)
    return shores
