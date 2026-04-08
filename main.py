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
    try:
        result = env.reset()
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}

# Step (FIXED)
@app.post("/step")
def step(action: Action):
    try:
        # Try string input first
        try:
            result = env.step(action.data)
        except:
            # If env expects dict
            result = env.step({"data": action.data})

        return {"result": result}

    except Exception as e:
        return {
            "error": str(e),
            "input_received": action.data
        }

# State
@app.get("/state")
def state():
    try:
        result = env.state()
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}
