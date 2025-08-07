# Gradio Web Demo

:::{Note}
**Support:** MiniCPM-V 4.0
:::

Gradio Web Demo is a web interface demonstration service for MiniCPM-V, supporting multimodal conversations with images and videos. The demo consists of two parts: **server** and **client**

Before getting started, please obtain the relevant code via [this link](https://github.com/OpenSQZ/MiniCPM-V-CookBook/tree/main/demo/web_demo/gradio).

## Deployment Steps

### Server

```bash
cd server
conda create -n gradio-server python=3.10
conda activate gradio-server
pip install -r requirements.txt
python gradio_server.py
```

**Custom Parameters:**

```bash
# Specify server port, log directory, model path and model type
python gradio_server.py --port=39240 --log_dir=logs_v4 --model_path=/path/to/model --model_type=minicpmv4
```

### Client

```bash
cd client
conda create -n gradio-client python=3.10
conda activate gradio-client
pip install -r requirements.txt
python gradio_client_minicpmv4.py
```

**Custom Parameters:**

```bash
# Specify frontend port and backend service address
python gradio_client_minicpmv4.py --port=9090 --server=http://localhost:39240/api
```

## Access

By default, after the services are started, you can access the web demo by visiting http://localhost:8889 in your browser.

![demo](./assets/demo.png)
