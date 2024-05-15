### TextSummarizer

### STEPS:
## How to run? 
### STEP 01- Create a conda environment after opening the repository
```bash
conda create -p youtubesummarizationenv python -y
```

```bash
source activate ./youtubesummarizationenv
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

### STEP 03- run application
```bash
Python app.py
```
```bash
Python youtubesummarizer.py
```
## Prompt
```bash
Could you please write a python script that would take a you tube url as input and give the transcript of that video as output
```
```bash
@GPT-4o Write a Python code that would take a youtube URL as input and give the video transcript as output. also include gradio UI and use hugging face model "sshleifer/distilbart-cnn-12-6"
```

##### after download move the model to code folder
```bash 
sudo mv /Users/mayankchugh/.cache/huggingface/hub/models--sshleifer--distilbart-cn
n-12-6 /Users/mayankchugh/gitRepos/mayankchugh.learning/HuggingFace-ML-GenerativeAI-Gradio-Streamlit-Apps/TextSummarizer-Gradio/models--sshleifer--distilbart-cnn-12-6
```
