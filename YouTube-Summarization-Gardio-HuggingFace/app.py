import pytube
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import gradio as gr

# Load the Hugging Face model and tokenizer
model_name = "sshleifer/distilbart-cnn-12-6"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

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

    # Summarize the transcript text using the Hugging Face model
    inputs = tokenizer(transcript_text, return_tensors="pt", truncation=True, padding="longest")
    summary_ids = model.generate(inputs["input_ids"], num_beams=4, max_length=100, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return summary

# Create a Gradio interface
iface = gr.Interface(
    fn=get_transcript,
    inputs="text",
    outputs="text",
    title="@IT AI Enthusiast (Mayank Chugh) (https://www.youtube.com/@itaienthusiast/) - Project 2: YouTube Video Transcript Generator",
    description="Enter a YouTube URL to generate and summarize the video transcript.",
    examples=['https://www.youtube.com/watch?v=0vK7AwUpRvY',
                'https://www.youtube.com/watch?v=tQb7bumjkIM',
                'https://www.youtube.com/watch?v=GWJYxR2Hy3g&t',
                'https://www.youtube.com/watch?v=Bokfvs4ht4k',
                'https://www.youtube.com/watch?v=YSMWN8VpY6A',
                'https://www.youtube.com/watch?v=HFYv-rk4v9Y'],
    concurrency_limit=8
)

# Launch the Gradio interface
iface.launch(share=False)