from fastapi import FastAPI
from pydantic import BaseModel
from env import DataCleaningEnv

# Pydantic model for POST data
class Action(BaseModel):
    action: dict

app = FastAPI(title="Smart Data Cleaning API")
env = DataCleaningEnv()

# Root route for quick check
@app.get("/")
def root():
    return {"message": "Smart Data Cleaning API is running"}

# Reset environment
@app.get("/reset")
def reset():
    return env.reset()

# Step through environment
@app.post("/step")
def step(action: Action):
    return env.step(action.action)

# Get current state
@app.get("/state")
def state():
    return env.state()
