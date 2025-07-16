# Ollama

## Requirements
- **Non-quantized version:** Requires over 9GB of RAM.
- **Quantized version:** Requires over 3GB of RAM.

## 1. Install Ollama

### macOS

[Download](https://ollama.com/download/Ollama.dmg)

### Windows

[Download](https://ollama.com/download/OllamaSetup.exe)

### Linux

```shell
curl -fsSL https://ollama.com/install.sh | sh
```

[Manual install instructions](https://github.com/ollama/ollama/blob/main/docs/linux.md)

### Docker

The official [Ollama Docker image](https://hub.docker.com/r/ollama/ollama) `ollama/ollama` is available on Docker Hub.

## 2. Quick Start

The MiniCPM-V 4 model can be used directly:

```shell
ollama run openbmb/minicpm-v4.0
```

### Command Line
Separate the input prompt and the image path with space.
```bash
What is in the picture? xx.jpg
```
### API
```python
with open(image_path, 'rb') as image_file:
    # Convert the image file to a base64 encoded string
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    data = {
    "model": "minicpm-v4.0",
    "prompt": query,
    "stream": False,
    "images": [encoded_string] # The 'images' list can hold multiple base64-encoded images.
    }

    # Set request URL
    url = "http://localhost:11434/api/generate"
    response = requests.post(url, json=data)

    return response
```

## 3. Customize model

**If the method above fails, please refer to the following guide.**

### Environment requirements

- cmake version 3.24 or above
- go version 1.22 or above
- gcc version 11.4.0 or above

### Download GGUF Model

[HuggingFace](https://huggingface.co/openbmb/openbmb/MiniCPM-V-4-gguf)  
[ModelScope](https://modelscope.cn/models/OpenBMB/OpenBMB/MiniCPM-V-4-gguf)

### Clone Official OpenBMB Ollama Fork

```sh
git clone https://github.com/OpenBMB/ollama.git
cd ollama
```

### Install Dependencies

```sh
go generate ./...
```

### Build Ollama

```sh
go build .
```

### Start Ollama Service

Once the build is successful, start the Ollama service from its root directory:

```sh
./ollama serve
```

### Create a ModelFile

Create and edit a ModelFile:

```sh
vim minicpmv4.Modelfile
```

The content of the Modelfile should be as follows:

```
FROM ./MiniCPM-V-4/model/ggml-model-Q4_K_M.gguf
FROM ./MiniCPM-V-4/mmproj-model-f16.gguf

TEMPLATE """{{ if .System }}<|im_start|>system

{{ .System }}<|im_end|>{{ end }}

{{ if .Prompt }}<|im_start|>user

{{ .Prompt }}<|im_end|>{{ end }}

<|im_start|>assistant<|im_end|>

{{ .Response }}<|im_end|>"""

PARAMETER stop "<|endoftext|>"
PARAMETER stop "<|im_end|>"
PARAMETER num_ctx 8192
```
Parameter Descriptions:

| first from | second from | num_ctx |
|-----|-----|-----|
| Your language GGUF model path | Your vision GGUF model path | Max Model length |

### Create Ollama Model
```bash
ollama create minicpm-v4.0 -f minicpmv4.Modelfile
```

### Run
In a new terminal window, run the model instance:
```bash
ollama run minicpm-v4.0
```

### Input Prompt
Enter the prompt and the image path, separated by a space.
```bash
What is in the picture? xx.jpg
```
