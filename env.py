from pydantic import BaseModel
from typing import Tuple, Dict
from tasks import TASKS
from grader import grade

# Observation (what agent sees)
class Observation(BaseModel):
    raw_data: str
    task_type: str

# Action (what agent sends)
class Action(BaseModel):
    cleaned_data: str

# Environment
class DataCleaningEnv:
    def __init__(self):
        self.index = 0
        self.current_task = None
        self.steps = 0

    def reset(self) -> dict:
        """Reset environment and return initial observation as dict"""
        self.current_task = TASKS[self.index % len(TASKS)]
        self.index += 1
        self.steps = 0
        obs = Observation(**self.current_task["input"])
        return obs.dict()  # Convert Pydantic model to dict

    def step(self, action: Action) -> Tuple[dict, float, bool, Dict]:
        """Take action and return (observation, reward, done, info)"""
        actual = self.current_task["output"]
        pred = action.cleaned_data

        reward = float(grade(pred, actual))

        self.steps += 1
        done = self.steps >= 1

        obs = Observation(**self.current_task["input"])

        info = {
            "expected_output": actual,
            "your_output": pred,
            "task_type": self.current_task["input"]["task_type"]
        }

        return obs.dict(), reward, done, info  # Ensure observation is dict

    def state(self) -> dict:
        """Return current environment state"""
        return {
            "input": self.current_task["input"],
            "expected_output": self.current_task["output"]
        }
