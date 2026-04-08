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
from fastapi import FastAPI
from pydantic import BaseModel
from env import DataCleaningEnv

# Simple input model
class Action(BaseModel):
    data: str

app = FastAPI(title="Smart Data Cleaning API")
env = DataCleaningEnv()

# Root route
@app.get("/")
def root():
    return {"message": "Smart Data Cleaning API is running"}

# Reset
@app.get("/reset")
def reset():
    try:
        result = env.reset()
        return {"result": str(result)}
    except Exception as e:
        return {"error": str(e)}

# Step
@app.post("/step")
def step(action: Action):
    try:
        result = env.step(action.data)
        return {"result": str(result)}
    except Exception as e:
        return {"error": str(e)}

# State
@app.get("/state")
def state():
    try:
        result = env.state()
        return {"result": str(result)}
    except Exception as e:
        return {"error": str(e)}    return env.state()
