import os
from env import DataCleaningEnv, Action as EnvAction
from tasks import TASKS

# =========================
# CLEANING LOGIC
# =========================
def clean_data(text):
    try:
        text = text.replace(":", "=")
        parts = text.split("||")
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
    return {"cleaned_data": cleaned}


# =========================
# MAIN LOOP (CRITICAL)
# =========================
def main():
    env = DataCleaningEnv()

    for _ in range(len(TASKS)):   # ✅ correct loop
        obs = env.reset()
        task_name = obs.get("task_type", "unknown")

        print(f"[START] task={task_name}", flush=True)

        action_dict = act(obs)
        action = EnvAction(**action_dict)

        obs, reward, done, info = env.step(action)

        print(f"[STEP] step=1 reward={reward}", flush=True)

        print(f"[END] task={task_name} score={reward} steps=1", flush=True)


# =========================
# ENTRYPOINT
# =========================
if __name__ == "__main__":
    main()
