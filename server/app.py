from fastapi import FastAPI
from pydantic import BaseModel
from env import DataCleaningEnv, Action as EnvAction

# ----------- Input Model -----------
class ActionInput(BaseModel):
    data: str  # cleaned data from agent

# ----------- App Init -----------
app = FastAPI(title="Smart Data Cleaning API")
env = DataCleaningEnv()

# ----------- Root -----------
@app.get("/")
def root():
    return {"message": "Smart Data Cleaning API is running"}

# ----------- Reset Endpoint -----------
@app.post("/reset")
def reset():
    """Reset the environment and return initial observation"""
    obs = env.reset()
    return {
        "observation": obs,  # Already a dict from env.reset()
        "info": {},
    }

# ----------- Step Endpoint -----------
@app.post("/step")
def step(action: ActionInput):
    """Take action in the environment and return result"""
    try:
        env_action = EnvAction(cleaned_data=action.data)
        obs, reward, done, info = env.step(env_action)
        return {
            "observation": obs,  # Already a dict
            "reward": float(reward),
            "done": bool(done),
            "info": info,
        }
    except Exception as e:
        return {
            "observation": {},
            "reward": 0.0,
            "done": True,
            "info": {"error": str(e)},
        }

# ----------- State Endpoint -----------
@app.get("/state")
def state():
    """Return current environment state"""
    return {
        "state": env.state(),  # Already a dict
    }
def main():
    return app

if __name__ == "__main__":
    main()
