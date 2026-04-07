from fastapi import FastAPI
from env import DataCleaningEnv

app = FastAPI()
env = DataCleaningEnv()

@app.get("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: dict):
    return env.step(action)

@app.get("/state")
def state():
    return env.state()