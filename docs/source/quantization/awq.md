# AWQ

:::{attention}
To be updated for MiniCPM-V 4.0
:::

:::{Note}
**Support:** MiniCPM-V2.6
:::


## AWQ Quantization (Recommended for vLLM)

### Environment Configuration

| vllm | transformers | torchvision | torch | triton | trl | autoawq_kernels |
|---|---|---|---|---|---|---|
| 0.5.4 | 4.44.0 | 0.19.0 | 2.4.0 | 3.0.0 | 0.9.6 | 0.0.6 |

### Method 1 (Recommended)

**1. Download the Pre-Quantized Model**

```bash
git clone https://www.modelscope.cn/models/linglingdan/MiniCPM-V_2_6_awq_int4
```

**2. Download and Build the AutoAWQ Fork**

> **Note**: A pull request for MiniCPM-V 2.6 support has been submitted to the official AutoAWQ repository and is pending merge. In the meantime, please use the following fork.

```bash
git clone https://github.com/LDLINGLINGLING/AutoAWQ.git
cd AutoAWQ
git checkout minicpmv2.6
pip install -e .
```

**3. Inference with the Pre-Quantized Model**

> Usage with vLLM is identical to the non-quantized model. For details, please refer to the "MiniCPM-V 2.6 Deployment Guide".

```python
from PIL import Image
from transformers import AutoTokenizer
from vllm import LLM, SamplingParams

# Path to the image file
IMAGES = [
    "./assets/airplane.jpeg",  # Example local image path
]

# Path to the quantized AWQ model
MODEL_PATH = "/path/to/MiniCPM-V_2_6_awq_int4"
# Load and convert the image
image = Image.open(IMAGES[0]).convert("RGB")

# Initialize the tokenizer
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)

# Initialize the LLM
llm = LLM(model=MODEL_PATH,
           gpu_memory_utilization=0.9,  # Adjust GPU memory utilization as needed
           trust_remote_code=True,
           max_model_len=2048)  # Adjust this value based on your available VRAM

# Construct the conversation messages
messages = [{'role': 'user', 'content': '(<image>./</image>)\n' + 'Describe this image.'}]

# Apply the chat template
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

# Set stop tokens
stop_tokens = ['<|im_end|>', '<|endoftext|>']
stop_token_ids = [tokenizer.convert_tokens_to_ids(i) for i in stop_tokens]

# Set sampling parameters
sampling_params = SamplingParams(
    stop_token_ids=stop_token_ids,
    max_tokens=1024,
    temperature=0,
    use_beam_search=True,
    best_of=3)

# Generate and retrieve the output
outputs = llm.generate({
    "prompt": prompt,
    "multi_modal_data": {
        "image": image
    }
}, sampling_params=sampling_params)
print(outputs[0].outputs[0].text)
```

### Method 2 (Manual Quantization)
This method is recommended for quantizing trained models.

**1. Download the PyTorch Model**
```bash
# Hugging Face
git clone https://huggingface.co/openbmb/MiniCPM-V-2_6
# ModelScope
git clone https://www.modelscope.cn/models/openbmb/minicpm-v-2_6
```

**2. Download and Build the AutoAWQ Fork**

> **Note**: A pull request for MiniCPM-V 2.6 support has been submitted to the official AutoAWQ repository and is pending merge. In the meantime, please use the following fork.

```bash
git clone https://github.com/LDLINGLINGLING/AutoAWQ.git
cd AutoAWQ
git checkout minicpmv2.6
pip install -e .
```

**3. Prepare the Quantization Scripts**

```bash
git clone https://github.com/OpenBMB/MiniCPM-CookBook.git
```

Replace the `modeling_minicpmv.py` file in your downloaded MiniCPM-V 2.6 model directory with the one from `MiniCPM-CookBook/MiniCPMV2_6_awq/modeling_minicpmv.py`.

**4. Run Quantization**

Modify the following parameters in the `MiniCPM-CookBook/MiniCPMV2_6_awq/quantize.py` file:

```python
# Path to the original MiniCPM-V 2.6 model
model_path = 'path/to/your/MiniCPM-V-2_6' 
# Path to save the quantized model
quant_path = 'path/to/save/MiniCPM-V-2_6_awq'

# Change this line:
# data = load_dataset('/root/ld/ld_project/MiniCPM/quantize/quantize_data/alpaca', split="train")
# to:
data = load_dataset('tatsu-lab/alpaca', split="train") 
```

Execute the quantization script:

```bash
python ./MiniCPM-CookBook/MiniCPMV2_6_awq/quantize.py
```

**5. Inference with the Quantized Model**

The inference code is the same as the example provided in **Method 1**. Please ensure you update the `MODEL_PATH` variable to the path you specified in `quant_path`.

```python
from PIL import Image
from transformers import AutoTokenizer
from vllm import LLM, SamplingParams

# Path to the image file
IMAGES = [
    "./assets/airplane.jpeg",  # Example local image path
]

# Path to the quantized AWQ model
MODEL_PATH = "/path/to/MiniCPM-V_2_6_awq_int4"
# Load and convert the image
image = Image.open(IMAGES[0]).convert("RGB")

# Initialize the tokenizer
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)

# Initialize the LLM
llm = LLM(model=MODEL_PATH,
           gpu_memory_utilization=0.9,  # Adjust GPU memory utilization as needed
           trust_remote_code=True,
           max_model_len=2048)  # Adjust this value based on your available VRAM

# Construct the conversation messages
messages = [{'role': 'user', 'content': '(<image>./</image>)\n' + 'Describe this image.'}]

# Apply the chat template
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

# Set stop tokens
stop_tokens = ['<|im_end|>', '<|endoftext|>']
stop_token_ids = [tokenizer.convert_tokens_to_ids(i) for i in stop_tokens]

# Set sampling parameters
sampling_params = SamplingParams(
    stop_token_ids=stop_token_ids,
    max_tokens=1024,
    temperature=0,
    use_beam_search=True,
    best_of=3)

# Generate and retrieve the output
outputs = llm.generate({
    "prompt": prompt,
    "multi_modal_data": {
        "image": image
    }
}, sampling_params=sampling_params)
print(outputs[0].outputs[0].text)
```
