from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
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

# ----------- Simple UI -----------
@app.get("/ui", response_class=HTMLResponse)
def ui():
    return """
    <html>
        <head>
            <title>Smart Data Cleaning</title>
        </head>
        <body style="font-family: Arial; text-align: center; padding: 40px;">
            <h1>🧹 Smart Data Cleaning</h1>

            <input id="input" style="width:300px; padding:10px;" 
                   placeholder="NAME=joHN||age=25"/>

            <br><br>

            <button onclick="sendData()" style="padding:10px 20px;">
                Clean Data
            </button>

            <h3 id="output"></h3>

            <script>
                async function sendData() {
                    const input = document.getElementById("input").value;

                    const res = await fetch('/step', {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify({data: input})
                    });

                    const data = await res.json();

                    document.getElementById("output").innerText =
                        JSON.stringify(data, null, 2);
                }
            </script>
        </body>
    </html>
    """

# ----------- Reset Endpoint -----------
@app.post("/reset")
def reset():
    obs = env.reset()
    return {
        "observation": obs,
        "info": {},
    }

# ----------- Step Endpoint -----------
@app.post("/step")
def step(action: ActionInput):
    try:
        env_action = EnvAction(cleaned_data=action.data)
        obs, reward, done, info = env.step(env_action)

        return {
            "observation": obs,
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
    return {
        "state": env.state(),
    }
