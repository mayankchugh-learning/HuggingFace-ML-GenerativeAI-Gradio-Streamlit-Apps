# Use a pipeline as a high-level helper
from transformers import pipeline
import gradio as gr

import pandas as pd
from textblob import TextBlob


# pipe = pipeline("text-classification", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

model_path = ("..//Models/models--distilbert--distilbert-base-uncased-finetuned-sst-2-english/snapshots/714eb0fa89d2f80546fda750413ed43d93601a13")

analyser = pipeline("text-classification", model=model_path)

# print(analyser(["This product is good!", "This product is expensive!"]))

def sentiment_analysis(text_to_review):
    sentiment = analyser(text_to_review)
    return sentiment[0]['label']

def read_excel_and_get_sentiment(file_path):
    """
    Reads an Excel file, checks if the 'Review' column is present,
    calls the `getSentiment()` function for each review,
    and returns a DataFrame with the reviews and their corresponding sentiments.
    
    Args:
        file_path (str): The file path of the Excel file.
    
    Returns:
        pd.DataFrame: A DataFrame with the reviews and their corresponding sentiments.
    
    Raises:
        KeyError: If the 'Review' column is not found in the Excel file.
    """
    try:
        df = pd.read_excel(file_path)
        if 'Review' not in df.columns:
            raise KeyError("'Review' column not found in the Excel file.")
        df['Sentiment'] = df['Review'].apply(sentiment_analysis)
        return df
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        raise
    except Exception as e:
        print(f"Error: {e}")
        raise

# Example usage
try:
    # file_path = input("Enter the file path of the Excel file: ")
    # result_df = read_excel_and_get_sentiment(file_path)
    result_df = read_excel_and_get_sentiment("../Files/ProductReview.xlsx")
    print(result_df)
except KeyError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error: {e}")





gr.close_all()

demo = gr.Interface(fn=sentiment_analysis,
                    inputs=[gr.Textbox(label="Input text to review",lines=6)],
                    outputs=[gr.Textbox(label="Reviewed text",lines=4)],
                    title="@IT AI Enthusiast (https://www.youtube.com/@itaienthusiast/) - Project 2: Sentiment Analysis",
                    description="THIS APPLICATION WILL BE USED TO ANALYZETHE SENTIMENT BASED ON THE COMMENT PROVIDER.",
                    concurrency_limit=16)
demo.launch()

