# Smart Data Cleaning OpenEnv

## Overview
This environment simulates real-world data cleaning tasks where AI agents transform messy raw data into structured formats.

## Real-world Importance
Data cleaning is a critical step in data science pipelines, affecting model performance and reliability.

## Observation Space
- raw_data: messy input string
- task_type: format | normalize | deduplicate

## Action Space
- cleaned_data: structured output string

## Tasks
- Easy: simple formatting
- Medium: normalization
- Hard: noisy mixed-format data

## Reward
- 1.0: perfect match
- 0.0–0.9: partial match based on structure

## Run
pip install -r requirements.txt
uvicorn main:app

## Baseline
Run inference.py to evaluate baseline agent performance
```
