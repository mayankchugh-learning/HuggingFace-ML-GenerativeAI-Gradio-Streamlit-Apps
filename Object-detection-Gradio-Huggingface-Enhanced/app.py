# Use a pipeline as a high-level helper
from transformers import pipeline
import gradio as gr
from PIL import Image, ImageDraw
import scipy.io.wavfile as wavfile

from phonemizer.backend.espeak.wrapper import EspeakWrapper
_ESPEAK_LIBRARY = '/opt/homebrew/Cellar/espeak/1.48.04_1/lib/libespeak.1.1.48.dylib'  #use the Path to the library.
EspeakWrapper.set_library(_ESPEAK_LIBRARY)

# pipe = pipeline("object-detection", model="facebook/detr-resnet-50")

object_detector_model_path = "../Models/models--facebook--detr-resnet-50/snapshots/1d5f47bd3bdd2c4bbfa585418ffe6da5028b4c0b"

object_detector = pipeline("object-detection", model=object_detector_model_path)

# narrator = pipeline("text-to-speech", model="kakao-enterprise/vits-ljs")

tts_model_path = "../Models/models--kakao-enterprise--vits-ljs/snapshots/3bcb8321394f671bd948ebf0d086d694dda95464"

narrator = pipeline("text-to-speech", model=tts_model_path)

# Define the function to generate audio from text 
def generate_audio(text):
    # Generate the narrated text
    narrated_text = narrator(text)

    # Save the audio to WAV file
    wavfile.write("finetuned_output.wav", rate=narrated_text["sampling_rate"],
                  data=narrated_text["audio"][0])

    # Return the path to the saved output WAV file
    return "finetuned_output.wav"

# Could you please write me a python code that will take list of detection object as an input and it will give the response that will include all the objects (labels) provided in the input. For example if the input is like this: [{'score': 0.9996405839920044, 'label': 'person', 'box': {'xmin': 435, 'ymin': 282, 'xmax': 636, 'ymax': 927}}, {'score': 0.9995879530906677, 'label': 'dog', 'box': {'xmin': 570, 'ymin': 694, 'xmax': 833, 'ymax': 946}}]
# The output should be, This pictuture contains 1 person and 1 dog. If there are multiple objects, do not add 'and' between every objects but 'and' should be at the end only


def read_objects(detection_objects):
    # Initialize counters for each object label
    object_counts = {}

    # Count the occurrences of each label
    for detection in detection_objects:
        label = detection['label']
        if label in object_counts:
            object_counts[label] += 1
        else:
            object_counts[label] = 1

    # Generate the response string
    response = "This picture contains"
    labels = list(object_counts.keys())
    for i, label in enumerate(labels):
        response += f" {object_counts[label]} {label}"
        if object_counts[label] > 1:
            response += "s"
        if i < len(labels) - 2:
            response += ","
        elif i == len(labels) - 2:
            response += " and"

    response += "."

    return response

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
    natural_text = read_objects(output)
    processed_audio = generate_audio(natural_text)
    return processed_image, processed_audio

gr.close_all()

demo = gr.Interface(fn=detect_object,
                    inputs=[gr.Image(label="Select Image",type="pil")],
                    outputs=[gr.Image(label="Processed Image", type="pil"), gr.Audio(label="Generated Audio")],
                    title="@IT AI Enthusiast (https://www.youtube.com/@itaienthusiast/) - Project 7: Object Detector with Audio",
                    description="THIS APPLICATION WILL BE USED TO HIGHLIGHT OBJECTS AND GIVES AUDIO DESCRIPTION FOR THE PROVIDED INPUT IMAGE.")
demo.launch()