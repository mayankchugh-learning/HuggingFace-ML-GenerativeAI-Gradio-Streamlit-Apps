# Use a pipeline as a high-level helper
from transformers import pipeline
import torch
import json

# text_translator = pipeline("translation", model="facebook/nllb-200-distilled-600M")

model_path  = "../Models/models--facebook--nllb-200-distilled-600M/snapshots/f8d333a098d19b4fd9a8b18f94170487ad3f821d"

text_translator = pipeline("translation", model=model_path, torch_dtype=torch.bfloat16)

text = "Hello friends how are you?"
translation = text_translator(text,
                              src_lang="eng_Latn",
                              tgt_lang="hin_Deva")

