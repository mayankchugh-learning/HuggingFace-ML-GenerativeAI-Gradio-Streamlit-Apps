# Machine-Failure-Gardio-Huggingface-MLDeployment

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference


## How to run? 
### STEP 01- Create a conda environment after opening the repository
```bash
conda create -p machinefailureenv python -y
conda create -n machinefailureenv_py310 python=3.10  -y
```

```bash
conda init
conda activate ./machinefailureenv

conda activate machinefailureenv_py310

source activate ./machinefailureenv
```
```bash
conda install scikit-learn=1.2.2 -y
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

```bash
python app.py
```