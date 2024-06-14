import gradio as gr
from PIL import Image

# Use a pipeline as a high-level helper
from transformers import pipeline

# pipe = pipeline("object-detection", model="facebook/detr-resnet-50")

model_path = "../Models/models--facebook--detr-resnet-50/snapshots/1d5f47bd3bdd2c4bbfa585418ffe6da5028b4c0b"

object_detector = pipeline("object-detection", model=model_path)

raw_image = Image.open("./Files/A image copy 12.png")

output = object_detector(raw_image)

print(output)


