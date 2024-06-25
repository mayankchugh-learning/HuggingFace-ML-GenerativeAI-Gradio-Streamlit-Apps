import torch
import gradio as gr
from diffusers import StableDiffusiojn3Pipeline

def image_generator():
    device = "cude" if torch.cuda.is_available() else "cpu"
    pipeline = StableDiffusiojn3Pipeline.from_pretrained("stabilityai/stable-diffusion-3-medium", 
                                                         torch_dtype=torch.float16 if device == "cuda" else torch.float32
                                                         )
    pipeline.enable_model_cpu_offload()
    #pipeline.to(device)

    image = pipeline(
        prompt=prompt,
        negative_prompts="blurred, ugly, watermark, low, resolution, blurry",
        max_inference_steps=40,
        height=1024,
        width=1024,
        guidance_scale=9.0
    ).images[0]

    image.show()