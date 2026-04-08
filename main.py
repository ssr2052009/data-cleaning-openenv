from fastapi import FastAPI
from pydantic import BaseModel
from env import DataCleaningEnv, Action as EnvAction

# API input model
class ActionInput(BaseModel):
    data: str

app = FastAPI(title="Smart Data Cleaning API")
env = DataCleaningEnv()

# Root
@app.get("/")
def root():
    return {"message": "Smart Data Cleaning API is running"}

# Reset
@app.post("/reset")
def reset():
    obs = env.reset()
    return obs.dict()

# Step (FIXED PROPERLY)
@app.post("/step")
def step(action: ActionInput):
    try:
        # Convert to Env Action
        env_action = EnvAction(cleaned_data=action.data)

        obs, reward, done, info = env.step(env_action)

        return {
            "observation": obs.dict(),
            "reward": reward,
            "done": done,
            "info": info
        }

    except Exception as e:
        return {"error": str(e)}

# State
@app.get("/state")
def state():
    return env.state()
