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
# HELPER FUNCTION TO QUERY LLM
# =========================
def query(payload):
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.json()

# =========================
# RULE-BASED CLEANING
# =========================
def clean_data(text):
    """Simple rule-based normalization"""
    try:
        parts = text.split("||")
        cleaned = []
        for part in parts:
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
    except Exception:
        return text

# =========================
# ACT FUNCTION REQUIRED BY OPENENV
# =========================
def act(observation: dict) -> dict:
    """
    Takes environment observation and returns action dict.
    Expected output format: {"cleaned_data": <str>}
    """
    raw_data = observation.get("raw_data", "")
    # Step 1: Rule-based cleaning
    cleaned = clean_data(raw_data)
    # Step 2: Optional LLM refinement
    try:
        prompt = f"Clean and normalize this data properly: {cleaned}"
        output = query({"inputs": prompt})
        result = output[0]["generated_text"]
        cleaned = result if result else cleaned
    except Exception:
        pass  # fallback to rule-based
    return {"cleaned_data": cleaned}
