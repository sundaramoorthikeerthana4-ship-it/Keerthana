#keerthana project-main file
from fastapi import FastAPI
app=FastAPI()
@app.get("/team")
def home():
  return{"message":"Hello skillWallet! project is working!"}
@app.get("/team")
def team_info():
  return{
    "team":"keerthana",
    "members":["keerthana","sundaramoorth"],
    "status":"Active"
  }


if__name__=="__main__":
  print("project Runing Successfully!")
