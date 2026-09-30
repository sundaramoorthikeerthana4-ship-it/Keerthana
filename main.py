#keerthana project-main file
from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def home():
  return{"message":"Hello skillWallet! project is working!"}
@app.get("/team")
def team_info():
  return{
    "team":"keerthana",
    "members":["keerthana","sundaramoorth"],
    "status":"Active"
  }


def main():
    import uvicorn
    print("project Runing Successfully!")
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__=="__main__":
    main()
