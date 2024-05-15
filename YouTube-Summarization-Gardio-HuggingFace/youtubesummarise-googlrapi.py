import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from urllib.parse import urlparse, parse_qs

# Set up the YouTube Data API client
DEVELOPER_KEY = "AIzaSyBpJJW2oa4ZeZZauTOiOtSHMy270bpfhVY" #os.getenv("YOUTUBE_DATA_KEY")
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

# Function to extract video ID from the URL
def get_video_id(url):
    parsed_url = urlparse(url)
    video_id = parse_qs(parsed_url.query).get('v')
    if video_id:
        return video_id[0]
    else:
        raise ValueError('Invalid YouTube URL')

# Function to get the transcript of a video
def get_video_transcript(video_id):
    try:
        # Retrieve the video caption tracks
        caption_tracks = youtube.captions().list(
            part='snippet',
            videoId=video_id
        ).execute()

        if not caption_tracks['items']:
            return 'Transcript not found for this video.'

        # Retrieve the transcript for the first caption track (assuming it's in English)
        captions = youtube.captions().download(
            id=caption_tracks['items'][0]['id'],
            tfmt='srt'
        ).execute()

        return captions['body']

    except HttpError as e:
        return f'An HTTP error occurred: {e}'

# Main function
def main():
    video_url = input('Enter the YouTube video URL: ')
    video_id = get_video_id(video_url)
    transcript = get_video_transcript(video_id)
    print(transcript)

# Run the script
if __name__ == '__main__':
    main()