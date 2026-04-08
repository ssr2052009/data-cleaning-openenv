import os
import requests
from env import DataCleaningEnv, Action as EnvAction

# =========================
# ENV VARIABLES
# =========================
HF_TOKEN = os.getenv("HF_TOKEN")
MODEL_NAME = os.getenv("MODEL_NAME", "google/flan-t5-large")
API_URL = f"https://api-inference.huggingface.co/models/{MODEL_NAME}"

HEADERS = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

# =========================
# HELPER FUNCTION
# =========================
def query(payload):
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.json()

# =========================
# CLEANING LOGIC
# =========================
def clean_data(text):
    try:
        parts = text.replace(":", "=").split("||")
        cleaned = []

        for part in parts:
            if "=" not in part:
                continue

            key, value = part.split("=")
            key = key.strip().lower()
            value = value.strip()

            if key == "name":
                value = value.capitalize()
            elif key == "city":
                value = value.capitalize()
            elif key == "country":
                value = value.upper()
            elif key == "email":
                value = value.lower()

            cleaned.append(f"{key}={value}")

        return " || ".join(cleaned)
    except:
        return text

# =========================
# AGENT ACTION
# =========================
def act(observation):
    raw_data = observation.get("raw_data", "")

    cleaned = clean_data(raw_data)

    # optional LLM
    try:
        prompt = f"Clean and normalize this: {cleaned}"
        output = query({"inputs": prompt})
        result = output[0]["generated_text"]
        if result:
            cleaned = result
    except:
        pass

    return {"cleaned_data": cleaned}

# =========================
# MAIN LOOP (IMPORTANT)
# =========================
def main():
    env = DataCleaningEnv()

    for i in range(len(env.__dict__.get("TASKS", [1,2,3])) + 3):
        obs = env.reset()

        task_name = obs.get("task_type", "unknown")

        # 🔥 REQUIRED
        print(f"[START] task={task_name}", flush=True)

        action_dict = act(obs)
        action = EnvAction(**action_dict)

        obs, reward, done, info = env.step(action)

        # 🔥 REQUIRED
        print(f"[STEP] step=1 reward={reward}", flush=True)

        score = reward

        # 🔥 REQUIRED
        print(f"[END] task={task_name} score={score} steps=1", flush=True)


# =========================
# ENTRYPOINT
# =========================
if __name__ == "__main__":
    main()
