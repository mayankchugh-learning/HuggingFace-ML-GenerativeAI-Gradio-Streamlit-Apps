### TextSummarizer

### STEPS:
## How to run? 
### STEP 01- Create a conda environment after opening the repository
```bash
conda create -p textsummarizationenv python -y
```

```bash
source activate ./textsummarizationenv
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

### STEP 03- run application
```bash
Python app.py
```

##### after download move the model to code folder
```bash 
sudo mv /Users/mayankchugh/.cache/huggingface/hub/models--sshleifer--distilbart-cn
n-12-6 /Users/mayankchugh/gitRepos/mayankchugh.learning/HuggingFace-ML-GenerativeAI-Gradio-Streamlit-Apps/TextSummarizer-Gradio/models--sshleifer--distilbart-cnn-12-6
```
```bash
[best text blog]
(https://www.forbes.com/advisor/business/software/best-blogging-platforms/)
```

### Prompt
```bash
Write a python code text summarisation as user input text provide a summarization of as output using model "sshleifer/distilbart-cnn-12-6" and use Gradio frontend application
```
