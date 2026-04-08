import gradio as gr
from env import DataCleaningEnv, Action

# Initialize environment
env = DataCleaningEnv()

def run_cleaning(input_text):
    try:
        # Reset environment to get a task
        obs = env.reset()

        # Use user input as cleaned output
        action = Action(cleaned_data=input_text)

        obs, reward, done, info = env.step(action)

        return (
            obs.raw_data,
            input_text,
            reward,
            info.get("expected_output", "N/A")
        )

    except Exception as e:
        return "Error", str(e), 0, "Error"

# UI
interface = gr.Interface(
    fn=run_cleaning,
    inputs=gr.Textbox(label="Enter Cleaned Data"),
    outputs=[
        gr.Textbox(label="Original Raw Data"),
        gr.Textbox(label="Your Cleaned Output"),
        gr.Number(label="Reward Score"),
        gr.Textbox(label="Expected Output")
    ],
    title="🧹 Smart Data Cleaning AI",
    description="Enter cleaned version of messy data and get reward score!"
)

interface.launch(server_name="0.0.0.0", server_port=7860)
