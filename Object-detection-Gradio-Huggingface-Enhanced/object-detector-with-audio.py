# Use a pipeline as a high-level helper
from transformers import pipeline

tts_model_pathx = pipeline("text-to-speech", model="kakao-enterprise/vits-ljs")