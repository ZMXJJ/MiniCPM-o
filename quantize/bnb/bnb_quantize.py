"""
the script will use bitandbytes to quantize the /MiniCPM-V-4 model.
the be quantized model can be finetuned by /MiniCPM-V-4 or not.
you only need to set the model_path 、save_path and run bash code 

download the model from https://huggingface.co/openbmb/MiniCPM-V-4
cd MiniCPM-o
python quantize/bnb/bnb_quantize.py

you will get the quantized model in save_path、quantized_model test time and gpu usage
"""


import torch
from transformers import AutoModel, AutoTokenizer, BitsAndBytesConfig
from PIL import Image
import time
import torch
import GPUtil
import os

assert torch.cuda.is_available(),"CUDA is not available, but this code requires a GPU."

device = 'cuda'  # Select GPU to use
model_path = '/mode/MiniCPM-V-4' # Model download path
save_path = './model/MiniCPM-V-4-int4' # Quantized model save path
image_path = './assets/airplane.jpeg'


# Create a configuration object to specify quantization parameters
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,  # Whether to perform 4-bit quantization
    load_in_8bit=False,  # Whether to perform 8-bit quantization
    bnb_4bit_compute_dtype=torch.float16,  # Computation precision setting
    bnb_4bit_quant_storage=torch.uint8,  # Storage format for quantized weights
    bnb_4bit_quant_type="nf4",  # Quantization format, here using normally distributed int4
    bnb_4bit_use_double_quant=True,  # Whether to use double quantization, i.e., quantizing zeropoint and scaling parameters
    llm_int8_enable_fp32_cpu_offload=False,  # Whether LLM uses int8, with fp32 parameters stored on the CPU
    llm_int8_has_fp16_weight=False,  # Whether mixed precision is enabled
    llm_int8_skip_modules=["out_proj", "kv_proj", "lm_head"],  # Modules not to be quantized
    llm_int8_threshold=6.0  # Outlier value in the llm.int8() algorithm, distinguishing whether to perform quantization based on this value
)

tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
model = AutoModel.from_pretrained(
    model_path,
    device_map=device,  # Allocate model to device
    quantization_config=quantization_config,
    trust_remote_code=True
)

gpu_usage = GPUtil.getGPUs()[0].memoryUsed  
start=time.time()
response = model.chat(
    image=Image.open(image_path).convert("RGB"),
    msgs=[
        {
            "role": "user",
            "content": "What is in this picture?"
        }
    ],
    tokenizer=tokenizer
) # 模型推理
print('Output after quantization:',response)
print('Inference time after quantization:',time.time()-start)
print(f"GPU memory usage after quantization: {round(gpu_usage/1024,2)}GB")

"""
Expected output:

    Output after quantization: The image features an Airbus A380-800 aircraft belonging to Hainan Airlines. The airplane is captured in mid-flight against a clear blue sky, showcasing its impressive size and design. The livery of the plane includes distinctive markings such as the red logo on the tail fin and Chinese characters along the fuselage. This particular model is known for being one of the largest passenger airliners globally due to its four powerful engines and double-deck configuration.
    Inference time after quantization: 6.637855052947998
    GPU memory usage after quantization: 4.35GB
"""

# Save the model and tokenizer
os.makedirs(save_path, exist_ok=True)
model.save_pretrained(save_path, safe_serialization=True)
tokenizer.save_pretrained(save_path)