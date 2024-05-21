import torch
import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt

# Use a pipeline as a high-level helper
from transformers import pipeline
# model_path = ("../Models/models--distilbert--distilbert-base-uncased-finetuned-sst-2-english"
#               "/snapshots/714eb0fa89d2f80546fda750413ed43d93601a13")

analyzer = pipeline("text-classification",
                model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

# analyzer = pipeline("text-classification",
#                 model=model_path)



# print(analyzer(["This production is good", "This product was quite expensive"]))

def sentiment_analyzer(review):
    sentiment = analyzer(review)
    return sentiment[0]['label']

def sentiment_bar_chart(df):
    sentiment_counts = df['Sentiment'].value_counts()

    # Create a bar chart
    fig, ax = plt.subplots()
    sentiment_counts.plot(kind='pie', ax=ax, autopct='%1.1f%%', color=['green', 'red'])
    ax.set_title('Review Sentiment Counts')
    ax.set_xlabel('Sentiment')
    ax.set_ylabel('Count')
    # ax.set_xticklabels(['Positive', 'Negative'], rotation=0)

    # Return the figure object
    return fig


def read_reviews_and_analyze_sentiment(file_object):
    # Load the Excel file into a DataFrame
    df = pd.read_excel(file_object)

    # Check if 'Review' column is in the DataFrame
    if 'Reviews' not in df.columns:
        raise ValueError("Excel file must contain a 'Review' column.")

    # Apply the get_sentiment function to each review in the DataFrame
    df['Sentiment'] = df['Reviews'].apply(sentiment_analyzer)
    chart_object = sentiment_bar_chart(df)
    return df, chart_object

# result = read_reviews_and_analyze_sentiment("../Files/Prod-review.xlsx")
# print(result)
# Example usage:
# df = read_reviews_and_analyze_sentiment('path_to_your_excel_file.xlsx')
# print(df)


demo = gr.Interface(fn=read_reviews_and_analyze_sentiment,
                    inputs=[gr.File(file_types=["xlsx"], label="Upload your review comment file")],
                    outputs=[gr.Dataframe(label="Sentiments"), gr.Plot(label="Sentiment Analysis")],
                    title="@GenAILearniverse Project 3: Sentiment Analyzer",
                    description="THIS APPLICATION WILL BE USED TO ANALYZE THE SENTIMENT BASED ON FILE UPLAODED.")
demo.launch()






# Example usage:
# Assuming you have a dataframe `df` with appropriate data
# fig = sentiment_bar_chart(df)
# fig.show()  # This line is just to visualize the plot in a local environment