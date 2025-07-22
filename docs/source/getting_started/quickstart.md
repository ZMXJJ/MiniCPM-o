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
model = AutoModel.from_pretrained('openbmb/MiniCPM-V-4', trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained('openbmb/MiniCPM-V-4', trust_remote_code=True)

# Start inference!
# See our recipe notebooks for detailed instructions
```

## 🍽️ Menu

### 🔥 Inference recipes
> *Ready-to-run examples*

| Recipe | Description |
| ------ | ----------- |
| **Vision Capabilities** |  |
| 🎬 [Video QA](https://github.com/OpenSQZ/MiniCPM-o-cookbook/blob/main/inference/video_understanding.md) | Video-based question answering |
| 🧩 [Multi-image QA](https://github.com/OpenSQZ/MiniCPM-o-cookbook/blob/main/inference/multi_images.md) | Question answering with multiple images |
| 🖼️ [Single-image QA](https://github.com/OpenSQZ/MiniCPM-o-cookbook/blob/main/inference/single_image.md) | Question answering on a single image |
| 📄 [Document Parser](https://github.com/OpenSQZ/MiniCPM-o-cookbook/blob/main/inference/pdf_parse.md) | Parse and extract content from PDFs and webpages |
| 📝 [Text Recognition](https://github.com/OpenSQZ/MiniCPM-o-cookbook/blob/main/inference/ocr.md) | Reliable OCR for photos and screenshots |
| **Audio Capabilities** |  |
| 🎤 [Speech-to-Text](https://github.com/OpenSQZ/MiniCPM-o-cookbook/blob/main/inference/speech2text.md) | Multilingual speech recognition |
| 🎭 [Voice Cloning](https://github.com/OpenSQZ/MiniCPM-o-cookbook/blob/main/inference/voice_clone.md) | Realistic voice cloning and role-play |
| 🗣️ [Text-to-Speech](https://github.com/OpenSQZ/MiniCPM-o-cookbook/blob/main/inference/text2speech.md) | Instruction-following speech synthesis |

### 🏋️ Fine-tuning recipes
> *Customize your model with your own ingredients*

| Framework | Description |
| --------- | ----------- |
| [Transformers](./finetune/fintune.html#full-parameter-finetuning) | Most flexible for customization |
| [LLaMA-Factory](./finetune/llamafactory.html) | Modular fine-tuning toolkit |
| [SWIFT](./finetune/swift.html) | Lightweight and fast parameter-efficient tuning |
| [Align-anything](./finetune/align-anything.html) | Visual instruction alignment for multimodal models |

### 🥡 Serving recipes
> *Deploy your model efficiently*

| Method | Description |
| ------ | ----------- |
| [vLLM](./deployment/vllm.html) | High-throughput GPU inference |
| [SGLang](./deployment/sglang.html) | High-throughput GPU inference |
| [Llama.cpp](./run_locally/llama.cpp.html) | Fast inference on PC, iPhone and iPad  |
| [Ollama](./run_locally/ollama.html) | User-friendly setup |
| [Fast API](./demo/webdemo.html) | Interactive Omni Streaming demo with FastAPI |
| [OpenWebUI](./demo/openwebui.html) | Interactive Web demo with Open WebUI |
| [iOS Demo](./demo/iosdemo.html) | Interactive iOS demo with llama.cpp |

### 🥄 Quantization recipes
> *Compress your model to improve efficiency*

| Format | Key Feature |
| ------ | ----------- |
| [GGUF](./quantization/gguf.html) | Simplest and most portable format |
| [BNB](./quantization/bnb.html) | Efficient 4/8-bit weight quantization |

