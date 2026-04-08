---
title: Smart Data Cleaning
emoji: 🧹
colorFrom: blue
colorTo: green
sdk: gradio
python_version: "3.10"
app_file: app.py
pinned: false
---
# 🧹 Smart Data Cleaning Environment (OpenEnv)

## 🚀 Overview

This project implements a **real-world data cleaning environment** using the OpenEnv framework.
It allows an AI agent to **learn how to clean messy structured data** through interactions using:

* `reset()`
* `step()`
* `state()`

... (rest of your README content follows)
# 🧹 Smart Data Cleaning Environment (OpenEnv)

## 🚀 Overview

This project implements a **real-world data cleaning environment** using the OpenEnv framework.
It allows an AI agent to **learn how to clean messy structured data** through interactions using:

* `reset()`
* `step()`
* `state()`

---

## 🎯 Problem Solved

Raw data is often inconsistent:

* Mixed casing (`joHN`, `chENNAI`)
* Invalid formats (`TEST@GMAIL.COM`)
* Poor structure

👉 This environment trains agents to:

* Normalize text
* Clean structured key-value data
* Improve data quality automatically

---

## 🧠 Features

* Custom OpenEnv environment (`env.py`)
* Rule-based + intelligent cleaning
* Reward-based evaluation system
* Multiple test tasks
* Fully offline (no API required)

---

## 📂 Project Structure

```
Smart Data Cleaning/
│── env.py              # Core environment
│── tasks.py            # Sample tasks
│── grader.py           # Reward calculation
│── inference.py        # Agent interaction
│── main.py             # Entry point
│── requirements.txt    # Dependencies
│── Dockerfile          # Deployment config
│── openenv.yaml        # OpenEnv config
```

---

## ⚙️ How It Works

### 1. Reset Environment

```python
env.reset()
```

### 2. Take Step

```python
env.step(action)
```

### 3. Get Reward

* Based on correctness of cleaned output
* Score range: `0.0 → 1.0`

---

## 🧪 Example

### Input:

```
NAME=joHN||age=25
```

### Output:

```
name=John || age=25
```

### Reward:

```
0.9
```

---

## 🏆 Results

* Final Score: **0.9**
* Accurate normalization of:

  * Names
  * Emails
  * Cities
  * Countries

---

## 🐳 Run Locally

```bash
pip install -r requirements.txt
python3 inference.py
```

---

## ☁️ Deployment

This project is designed for deployment using:

* Hugging Face Spaces (Docker)
* OpenEnv ecosystem

---

## 🔐 Security Note

* No external API keys required
* Fully offline safe execution

---

## 👨‍💻 Author

**Saisriram**
GitHub: https://github.com/ssr2052009

---

## ⭐ Final Note

This project demonstrates how AI agents can **learn real-world data cleaning tasks**, making it useful for:

* Data Science
* Machine Learning pipelines
* Automation systems

---
