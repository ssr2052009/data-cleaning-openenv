import os
from openai import OpenAI
from env import DataCleaningEnv, Action as EnvAction

# =========================
# LLM CLIENT (MANDATORY)
# =========================
client = OpenAI(
    base_url=os.environ["API_BASE_URL"],
    api_key=os.environ["API_KEY"]
)

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

    # Step 1: rule-based
    cleaned = clean_data(raw_data)

    # Step 2: LLM (MANDATORY FOR PASS)
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # proxy will handle
            messages=[
                {"role": "system", "content": "You clean and normalize structured data."},
                {"role": "user", "content": f"Clean this data: {cleaned}"}
            ],
            max_tokens=100
        )

        llm_output = response.choices[0].message.content.strip()

        if llm_output:
            cleaned = llm_output

    except Exception:
        pass  # fallback

    return {"cleaned_data": cleaned}

# =========================
# MAIN LOOP (IMPORTANT)
# =========================
def main():
    env = DataCleaningEnv()

    for _ in range(10):
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
