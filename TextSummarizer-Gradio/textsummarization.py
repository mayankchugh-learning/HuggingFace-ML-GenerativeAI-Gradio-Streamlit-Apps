import gradio as gr
from transformers import pipeline

# import json
# import uuid
# # from huggingface_hub import CommitScheduler
# from pathlib import Path

# log_file = Path("logs/") / f"data_{uuid.uuid4()}.json"
# log_folder = log_file.parent

# scheduler = CommitScheduler(
#     repo_id="text-summarization-logs",
#     repo_type="dataset",
#     folder_path=log_folder,
#     path_in_repo="data",
#     every=2
# )

# Load the summarization model
model_name = "sshleifer/distilbart-cnn-12-6"
summarizer = pipeline("summarization", model=model_name, tokenizer=model_name)

# Function to generate the summary
def generate_summary(text):
    # Set the maximum length of the summary
    max_length = 100  # You can adjust this value based on your needs
    # Generate the summary
    summary = summarizer(text, max_length=max_length, min_length=10, do_sample=False)

    print('Input Text:', text)
    print('Summary:', summary[0]['summary_text'])
    
    # with scheduler.lock:
    #     with log_file.open("a") as f:
    #         f.write(json.dumps(
    #             {
    #                 'Input Text': text,
    #                 'Summary': summary[0]['summary_text']
    #             }
    #         ))
    #         f.write("\n")
            
    return summary[0]['summary_text']

# Create the Gradio interface
def summarize_text(input_text):
    summary = generate_summary(input_text)
    return summary

iface = gr.Interface(
    fn=summarize_text,
    inputs=[gr.Textbox(label="Input text to summarize",lines=6)],
    outputs=[gr.Textbox(label="Summarized text",lines=4)],
    title="@IT AI Enthusiast (https://www.youtube.com/@itaienthusiast/) - Project 1: Text Summarizer",
    description="THIS APPLICATION WILL BE USED TO SUMMARIZE THE TEXT",
    concurrency_limit=16,
    theme=gr.themes.Soft()
)

# Launch the interface
iface.launch()