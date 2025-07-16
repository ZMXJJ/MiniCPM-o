# llama.cpp

:::{attention}
Currently, this readme only supports minicpm-omni's image capabilities, and we will update the full-mode support as soon as possible.
:::


## 1. Build llama.cpp

Clone the llama.cpp repository:  
[https://github.com/ggml-org/llama.cpp.git](https://github.com/ggml-org/llama.cpp.git)
```bash
git clone https://github.com/ggml-org/llama.cpp.git
cd llama.cpp
```

Build llama.cpp using [CMake](https://github.com/ggerganov/llama.cpp/blob/master/docs/build.md):

**CPU/Metal:**
```bash
cmake -B build
cmake --build build --config Release
```

**CUDA:**
```bash
cmake -B build -DGGML_CUDA=ON
cmake --build build --config Release
```
## 2. GGUF files

### Option 1: Download official GGUF files

Download converted language model file (e.g., `Model-3.6B-Q4_K_M.gguf`) and vision model file (`mmproj-model-f16.gguf`) from:  
[HuggingFace](https://huggingface.co/openbmb/openbmb/MiniCPM-V-4-gguf)  
[ModelScope](https://modelscope.cn/models/OpenBMB/OpenBMB/MiniCPM-V-4-gguf)

### Option 2: Convert from PyTorch model

Download the MiniCPM-o-2_6 PyTorch model to "MiniCPM-o-2_6" folder:  
[HuggingFace](https://huggingface.co/openbmb/MiniCPM-o-2_6)  
[ModelScope](https://modelscope.cn/models/OpenBMB/MiniCPM-o-2_6)

Convert the PyTorch model to GGUF:

```bash
python ./tools/mtmd/legacy-models/minicpmv-surgery.py -m ../MiniCPM-o-2_6

python ./tools/mtmd/legacy-models/minicpmv-convert-image-encoder-to-gguf.py -m ../MiniCPM-o-2_6 --minicpmv-projector ../MiniCPM-o-2_6/minicpmv.projector --output-dir ../MiniCPM-o-2_6/ --image-mean 0.5 0.5 0.5 --image-std 0.5 0.5 0.5

python ./convert-hf-to-gguf.py ../MiniCPM-o-2_6/model

# quantize int4 version
./llama-quantize ../MiniCPM-o-2_6/model/ggml-model-f16.gguf ../MiniCPM-o-2_6/model/ggml-model-Q4_K_M.gguf Q4_K_M
```

## 3. Model Inference

### 3.1 Command-Line Inference

```bash
cd build/bin/

# run f16 version
./llama-mtmd-cli -m ../MiniCPM-o-2_6/model/ggml-model-f16.gguf --mmproj ../MiniCPM-o-2_6/mmproj-model-f16.gguf -c 4096 --temp 0.7 --top-p 0.8 --top-k 100 --repeat-penalty 1.05 --image xx.jpg -p "What is in the image?"

# run quantized int4 version
./llama-mtmd-cli -m ../MiniCPM-o-2_6/model/ggml-model-Q4_K_M.gguf --mmproj ../MiniCPM-o-2_6/mmproj-model-f16.gguf -c 4096 --temp 0.7 --top-p 0.8 --top-k 100 --repeat-penalty 1.05 --image xx.jpg -p "What is in the image?"

# or run in interactive mode
./llama-mtmd-cli -m ../MiniCPM-o-2_6/model/ggml-model-Q4_K_M.gguf --mmproj ../MiniCPM-o-2_6/mmproj-model-f16.gguf -c 4096 --temp 0.7 --top-p 0.8 --top-k 100 --repeat-penalty 1.05 --image xx.jpg -i
```

**Argument Reference:**

| Argument | `-m, --model` | `--mmproj` | `--image` | `-p, --prompt` | `-c, --ctx-size` |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Description | Path to the language model | Path to the vision model | Path to the input image | The prompt | Maximum context size |

### 3.2 WebUI Deployment

Run `llama-server`:

```bash
cd build/bin/

./llama-server -m ../MiniCPM-o-2_6/model/ggml-model-Q4_K_M.gguf --mmproj ../MiniCPM-o-2_6/mmproj-model-f16.gguf

# use GPU for accelerated inference
./llama-server -m ../MiniCPM-o-2_6/model/ggml-model-Q4_K_M.gguf --mmproj ../MiniCPM-o-2_6/mmproj-model-f16.gguf -ngl 10000
```

More API usage for `llama-server`:  
[https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)

Deploy the frontend WebUI:

```bash
# install Node.js
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
source ~/.bashrc  # or ~/.zshrc, depending on your shell
nvm install --lts

# build
cd tools/server/webui
npm install --registry=https://registry.npmmirror.com
npm run dev
```
