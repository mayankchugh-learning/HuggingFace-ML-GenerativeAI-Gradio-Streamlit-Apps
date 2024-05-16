### TextSummarizer

### STEPS:
## How to run? 
### STEP 01- Create a conda environment after opening the repository
```bash
conda create -p sentimentanalysisenv python -y
```

```bash
source activate ./sentimentanalysisenv
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

### STEP 03- run application
```bash
Python app.py
```

## Prompt
```bash
Could you please write a python script that would take a you tube url as input and give the transcript of that video as output
```
```bash
@GPT-4o Write a Python code that would take a youtube URL as input and give the video transcript as output. also include gradio UI and use hugging face model "sshleifer/distilbart-cnn-12-6"
```

##### after download move the model to code folder
```
cd /Users/mayankchugh/.cache/huggingface/hub/
```
###### copy your downloaded model name and path and paste it below (it already pasted for my workspace)
```bash 
sudo mv /Users/mayankchugh/.cache/huggingface/hub/models--distilbert--distilbert-base-uncased-finetuned-sst-2-english /Users/mayankchugh/gitRepos/mayankchugh.learning/HuggingFace-ML-GenerativeAI-Gradio-Streamlit-Apps/Models/models--distilbert--distilbert-base-uncased-finetuned-sst-2-english
```
