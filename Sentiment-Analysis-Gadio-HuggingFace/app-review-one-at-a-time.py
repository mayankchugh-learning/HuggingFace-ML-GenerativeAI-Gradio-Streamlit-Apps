# Use a pipeline as a high-level helper
from transformers import pipeline
import gradio as gr

# pipe = pipeline("text-classification", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

model_path = ("..//Models/models--distilbert--distilbert-base-uncased-finetuned-sst-2-english/snapshots/714eb0fa89d2f80546fda750413ed43d93601a13")

analyser = pipeline("text-classification", model=model_path)

# print(analyser(["This product is good!", "This product is expensive!"]))


def sentiment_analysis(text_to_review):
    sentiment = analyser(text_to_review)
    return sentiment[0]['label']


gr.close_all()

demo = gr.Interface(fn=sentiment_analysis,
                    inputs=[gr.Textbox(label="Input text to review",lines=6)],
                    outputs=[gr.Textbox(label="Reviewed text",lines=4)],
                    title="@IT AI Enthusiast (https://www.youtube.com/@itaienthusiast/) - Project 2: Sentiment Analysis",
                    description="THIS APPLICATION WILL BE USED TO ANALYZETHE SENTIMENT BASED ON THE COMMENT PROVIDER.",
                    concurrency_limit=16)
demo.launch()

