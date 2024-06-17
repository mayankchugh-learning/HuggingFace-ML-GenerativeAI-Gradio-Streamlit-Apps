### TextSummarizer

### STEPS:
## How to run? 
### STEP 01- Create a conda environment after opening the repository
```bash
conda create -p hallbotvenv python -y
```

```bash
source activate ./hallbotvenv
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
sudo mv /Users/mayankchugh/.cache/huggingface/hub/models--deepset--roberta-base-squad2 /Users/mayankchugh/gitRepos/mayankchugh.learning/HuggingFace-ML-GenerativeAI-Gradio-Streamlit-Apps/Models
```

```bash
../Models/models--deepset--roberta-base-squad2/snapshots/cbf50ba81465d4d8676b8bab348e31835147541b
```

## Prompt
```bash
write a gradio python program in which user can select value for "UG Hall" from roman number 1 to 9 and "Room type" radio buttons values are "Single room, Double room, Triple room and Bunkbed". also ask name of student and its class. upon submit create as json objec fo selected values
```

```bash
write a small story about friendship between a machine and a boy.
```

##### after download move the model to code folder
```
cd /Users/mayankchugh/.cache/huggingface/hub/
```

[Gradio documentation link](https://www.gradio.app/docs/gradio/file)

### related to question

[Wikipedia Link](https://en.wikipedia.org/wiki/Continent)
