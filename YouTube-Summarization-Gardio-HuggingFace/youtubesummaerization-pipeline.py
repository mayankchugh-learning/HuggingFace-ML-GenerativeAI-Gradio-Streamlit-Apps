import pytube
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline
import gradio as gr

# Set up the summarization pipeline using the Hugging Face model
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def get_transcript(youtube_url):
    # Extract the video ID from the YouTube URL
    video_id = pytube.extract.video_id(youtube_url)

    # Get the transcript using the YouTube Transcript API
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
    except Exception as e:
        return f"Error retrieving transcript: {str(e)}"

    # Join the transcript segments into a single string
    transcript_text = " ".join([segment["text"] for segment in transcript_list])

    # Summarize the transcript text using the Hugging Face summarization pipeline
    summarized_text = summarizer(transcript_text, max_length=150, min_length=30, do_sample=False)

    return summarized_text[0]['summary_text']

# Create a Gradio interface
iface = gr.Interface(
    fn=get_transcript,
    inputs="text",
    outputs="text",
    title="YouTube Video Transcript Generator",
    description="Enter a YouTube URL to generate and summarize the video transcript."
)

# Launch the Gradio interface
iface.launch()