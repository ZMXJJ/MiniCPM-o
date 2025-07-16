<<<<<<< HEAD
# MiniCPM-V 4.0 - SGLang Documentation

[SGLang](https://github.com/sgl-project/sglang) is a fast serving framework for large language models and vision language models.
To learn more about SGLang, please refer to the [documentation](https://docs.sglang.ai/).

## 1. Environment Setup
### 1.1 Installing SGLang

**Install SGLang from Source Code**

=======
# SGLang

## 1. Installing SGLang
### Install SGLang from Source Code
>>>>>>> 936220f (Add Chinese localization and documentation updates for LlamaFactory)
```bash
git clone https://github.com/sgl-project/sglang.git
cd sglang

pip install --upgrade pip
pip install -e "python[all]"
```

<<<<<<< HEAD
**Installing flashinfer Dependencies**

**Method 1:** pip installation (network speed may be insufficient)
=======
### Installing flashinfer Dependencies

Method 1: pip installation (network speed may be insufficient)
>>>>>>> 936220f (Add Chinese localization and documentation updates for LlamaFactory)
```cpp
pip install flashinfer -i https://flashinfer.ai/whl/cu121/torch2.4/
```

<<<<<<< HEAD
**Method 2:** whl file installation
=======
Method 2: whl file installation
>>>>>>> 936220f (Add Chinese localization and documentation updates for LlamaFactory)
- Visit: [https://flashinfer.ai/whl/cu121/torch2.4/flashinfer/](https://flashinfer.ai/whl/cu121/torch2.4/flashinfer/)
- Locate and download the whl file compatible with your server, e.g. `flashinfer-0.1.6+cu121torch2.4-cp310-cp310-linux_x86_64.whl`
- Install using pip:
    ```cpp
    pip install flashinfer-0.1.6+cu121torch2.4-cp310-cp310-linux_x86_64.whl
    ```
For any installation issues, please consult the [official installation documentation](https://docs.sglang.ai/start/install.html)

<<<<<<< HEAD
## 2. API Service Deployment

### 2.1 Launching Inference Service with sglang

It is easy to build an OpenAI-compatible API service with SGLang, which can be deployed as a server that implements OpenAI API protocol. By default, it starts the server at http://localhost:8000. You can specify the address with --host and --port arguments. Run the command as shown below:

```bash
python -m sglang.launch_server --model-path openbmb/MiniCPM-V-4.0 --port 30000
```

Alternatively, you can specify a local model path after the `--model-path` parameter

=======
## 2. Launching Inference Service with sglang

By default, it downloads model files from Hugging Face Hub
```cpp
python -m sglang.launch_server --model-path openbmb/MiniCPM-V-4.0 --port 30000
```
Alternatively, you can specify a local path after the `--model-path` parameter
>>>>>>> 936220f (Add Chinese localization and documentation updates for LlamaFactory)
```cpp
python -m sglang.launch_server --model-path your_model_path --port 30000 --trust-remote-code
```

<<<<<<< HEAD
## 2.2 Image Inference

::::{tab-set}

:::{tab-item} curl

```bash
curl -s http://localhost:30000/v1/chat/completions \
-H "Content-Type: application/json" \
-d '{
    "model": "MiniCPM-V-4.0",
    "messages": [
    {
        "role": "user",
        "content": [
        {
            "type": "text",
            "text": "What's in this image?"
        },
        {
            "type": "image_url",
            "image_url": {
            "url": "https://github.com/tc-mb/MiniCPM-o-cookbook_private/blob/main/inference/assets/airplane.jpeg?raw=true"
            }
        }
        ]
    }
    ],
    "max_tokens": 300
}'
```
:::

:::{tab-item} Python

You can use the API client with the `openai` Python SDK as shown below:

```python
from openai import OpenAI

client = OpenAI(base_url=f"http://localhost:30000/v1", api_key="None")

response = client.chat.completions.create(
    model="MiniCPM-V-4.0",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What is in this image?",
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://github.com/tc-mb/MiniCPM-o-cookbook_private/blob/main/inference/assets/airplane.jpeg?raw=true",
                    },
                },
            ],
        }
    ],
    max_tokens=300,
)

print(response.choices[0].message.content)
```

::::



:::{note}

**If the image_url is inaccessible, it can be replaced with a local image path**

For more calling methods, please refer to the [SGLang documentation](https://docs.sglang.ai/backend/openai_api_vision.html)

:::



=======
## 3. Service API Calls
- Bash call
    ```python
    curl -s http://localhost:30000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "MiniCPM-V-4.0",
        "messages": [
        {
            "role": "user",
            "content": [
            {
                "type": "text",
                "text": "What's in this image?"
            },
            {
                "type": "image_url",
                "image_url": {
                "url": "https://github.com/tc-mb/MiniCPM-o-cookbook_private/blob/main/inference/assets/airplane.jpeg?raw=true"
                }
            }
            ]
        }
        ],
        "max_tokens": 300
    }'
    ```

- Python call
    ```python
    from openai import OpenAI

    client = OpenAI(base_url=f"http://localhost:30000/v1", api_key="None")

    response = client.chat.completions.create(
        model="MiniCPM-V-4.0",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "What is in this image?",
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": "https://github.com/tc-mb/MiniCPM-o-cookbook_private/blob/main/inference/assets/airplane.jpeg?raw=true",
                        },
                    },
                ],
            }
        ],
        max_tokens=300,
    )

    print(response.choices[0].message.content)
    ```
> **If the image_url is inaccessible, it can be replaced with a local image path**
> 
> For more calling methods, please refer to the [SGLang documentation](https://docs.sglang.ai/backend/openai_api_vision.html)
>>>>>>> 936220f (Add Chinese localization and documentation updates for LlamaFactory)
