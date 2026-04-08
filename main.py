from fastapi import FastAPI
from pydantic import BaseModel
from env import DataCleaningEnv

# Input model
class Action(BaseModel):
    data: str

app = FastAPI(title="Smart Data Cleaning API")
env = DataCleaningEnv()

# Root
@app.get("/")
def root():
    return {"message": "Smart Data Cleaning API is running"}

# Reset
@app.get("/reset")
def reset():
    return {"result": str(env.reset())}

# Step
@app.post("/step")
def step(action: Action):
    return {"result": str(env.step(action.data))}

# State
@app.get("/state")
def state():
    return {"result": str(env.state())}
