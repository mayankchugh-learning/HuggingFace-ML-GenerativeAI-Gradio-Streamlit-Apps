import gradio as gr
from PIL import Image, ImageDraw

# Use a pipeline as a high-level helper
from transformers import pipeline

# pipe = pipeline("object-detection", model="facebook/detr-resnet-50")

model_path = "../Models/models--facebook--detr-resnet-50/snapshots/1d5f47bd3bdd2c4bbfa585418ffe6da5028b4c0b"

object_detector = pipeline("object-detection", model=model_path)

def draw_bounding_boxes(image, object_detections):
    """
    Draws bounding boxes around detected objects on a PIL image.
    
    Args:
        image (PIL.Image): The input image.
        object_detections (list): A list of dictionaries, where each dictionary represents a detected object. 
                                 Each dictionary should have the following keys:
                                 - 'score': the confidence score of the detection
                                 - 'label': the label of the detected object
                                 - 'box': a dictionary with keys 'xmin', 'ymin', 'xmax', 'ymax' 
                                   representing the bounding box coordinates.
    
    Returns:
        PIL.Image: The input image with bounding boxes drawn around the detected objects.
    """
    draw = ImageDraw.Draw(image)
    for detection in object_detections:
        box = detection['box']
        label = detection['label']
        score = detection['score']
        
        # Draw the bounding box
        draw.rectangle((box['xmin'], box['ymin'], box['xmax'], box['ymax']), outline=(255, 0, 0), width=2)
        
        # Draw the label and score
        text = f"{label} ({score:.2f})"
        draw.text((box['xmin'], box['ymin'] - 20), text, fill=(255, 0, 0))
    
    return image

def detect_object(image):
    # raw_image = Image.open(image)
    output = object_detector(image)
    processed_image = draw_bounding_boxes(image, output)
    return processed_image

gr.close_all()

demo = gr.Interface(fn=detect_object,
                    inputs=[gr.Image(label="Select Image", type="pil")],
                    outputs=[gr.Image(label="Processed Image", type="pil")],
                    title="@IT AI Enthusiast (https://www.youtube.com/@itaienthusiast/) - Project 6: Object Detector",
                    description="THIS APPLICATION WILL BE USED TO DETECT OBJECT INSIDE THE PROVIDED INPUT IMGAES",
                    concurrency_limit=16)
demo.launch()