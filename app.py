from fastapi import FastAPI
from pydantic import BaseModel
from env import DataCleaningEnv, Action as EnvAction

# ----------- Input Model -----------
class ActionInput(BaseModel):
    data: str


# ----------- App Init -----------
app = FastAPI(title="Smart Data Cleaning API")
env = DataCleaningEnv()


# ----------- Root -----------
@app.get("/")
def root():
    return {"message": "Smart Data Cleaning API is running"}


# ----------- Reset (IMPORTANT FIX) -----------
@app.post("/reset")
def reset():
    obs = env.reset()

    return {
        "observation": obs.dict() if hasattr(obs, "dict") else obs,
        "info": {},
    }


# ----------- Step (IMPORTANT FIX) -----------
@app.post("/step")
def step(action: ActionInput):
    try:
        # Convert input → Env Action
        env_action = EnvAction(cleaned_data=action.data)

        obs, reward, done, info = env.step(env_action)

        return {
            "observation": obs.dict() if hasattr(obs, "dict") else obs,
            "reward": float(reward),
            "done": bool(done),
            "info": info if isinstance(info, dict) else {},
        }

    except Exception as e:
        return {
            "observation": {},
            "reward": 0.0,
            "done": True,
            "info": {"error": str(e)},
        }


# ----------- State -----------
@app.get("/state")
def state():
    state = env.state()

    return {
        "state": state if isinstance(state, dict) else {},
    }
