# Use a pipeline as a high-level helper
from transformers import pipeline
import gradio as gr
import matplotlib.pyplot as plt
import pandas as pd
from textblob import TextBlob


# analyser = pipeline("text-classification", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

model_path = ("../Models/models--distilbert--distilbert-base-uncased-finetuned-sst-2-english/snapshots/714eb0fa89d2f80546fda750413ed43d93601a13")

analyser = pipeline("text-classification", model=model_path)

def sentiment_analysis(text_to_review):
    sentiment = analyser(text_to_review)
    return sentiment[0]['label']

def plot_sentiment_pie(df):
    # Count the number of positive and negative reviews
    sentiment_counts = df['Sentiment'].value_counts()
    
    # Create the pie chart
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(sentiment_counts.values, labels=sentiment_counts.index, autopct='%1.1f%%')
    ax.set_title('Sentiment Distribution')
    
    # Convert the Matplotlib figure to a Gradio Plots component
    return fig

def read_excel_and_get_sentiment(file):
    try:
        # df = pd.read_excel(file_path)
        df = pd.read_excel(file)
        if 'Review' not in df.columns:
            raise KeyError("'Review' column not found in the Excel file.")
        df['Sentiment'] = df['Review'].apply(sentiment_analysis)
        chart_object = plot_sentiment_pie(df)
        return df, chart_object
    except FileNotFoundError:
        print(f"Error: {file} not found.")
        raise
    except Exception as e:
        print(f"Error: {e}")
        raise

gr.close_all()

demo = gr.Interface(fn=read_excel_and_get_sentiment,
                    inputs=[gr.File(file_types=["xlsx"],label="upload your review comment Excel file.")],
                    outputs=[gr.Dataframe(label="Reviewed text"), gr.Plot(label="Sentiment Analysis")],
                    title="@IT AI Enthusiast (https://www.youtube.com/@itaienthusiast/) - Project 3: Sentiment Analysis",
                    description="THIS APPLICATION WILL BE USED TO ANALYZETHE SENTIMENT BASED ON THE FILE UPLOADED.",
                    concurrency_limit=16)
demo.launch()

