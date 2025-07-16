# Quickstart

## 1. Installation
```bash
pip install -r inference/requirements.txt
```

## 2. Basic Usage
```python
import torch
from transformers import AutoModel, AutoTokenizer

# Load the model
model = AutoModel.from_pretrained('openbmb/MiniCPM-o-2_6', trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained('openbmb/MiniCPM-o-2_6', trust_remote_code=True)

# Start inference!
# See our recipe notebooks for detailed instructions
```