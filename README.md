# NTU_AI_Club_Customer_Service

## GPU Device
RTX 3090 (24G)

## Creat Environment
```bash
conda create -n customer python=3.10
conda activate customer
```

## Install dependency
```bash
pip install torch==2.3.0 torchvision==0.18.0 torchaudio==2.3.0
pip install -r requirement.txt
```

## Download LLM model
```bash
python model.py # if gpu out of memory, decrease "max_tokens" and increase "gpu_memory_utilization".
```

## Run Customer Service
```bash
python main.py
```
use "exit" to end the program.