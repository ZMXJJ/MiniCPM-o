.. MiniCPM Cookbook documentation master file, created by
   sphinx-quickstart on Sat Jul 12 18:12:12 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to MiniCPM-V Cookbook
==============================
.. figure:: assets/MiniCPM-logo.svg
  :width: 70%
  :align: center
  :alt: MiniCPM
  :class: no-scaled-link

.. raw:: html

   <br>


MiniCPM-V is a lightweight, high-performance edge-side large multimodal model jointly developed by ModelBest, the OpenBMB, and the Tsinghua NLP Lab. Both multimodal models are pretrained on large-scale multilingual and multimodal datasets, and subsequently fine-tuned on high-quality data to align with human preferences.
MiniCPM can perform natural language understanding, text generation, visual comprehension, tool utilization, role-playing, and function as an AI agent, among other capabilities.

The latest version, MiniCPM-V 4.0,  includes the following key features:

- **Multimodal Capabilities**: MiniCPM-V supports both text and image inputs, enabling it to understand and generate content that includes visual elements.
- **High Performance**: The model is designed to be lightweight and efficient, making it suitable for deployment in resource-constrained environments.
- **Light Weight**: MiniCPM-V is optimized for performance, ensuring fast inference times while maintaining high accuracy.

For more information, please visit our:

* `GitHub <https://github.com/OpenBMB>`__
* `Hugging Face <https://huggingface.co/OpenBMB>`__
* `Modelscope <https://modelscope.cn/organization/OpenBMB>`__

Welcome to join our community by joining our `Discord <https://discord.gg/rM6sC9G2MA>`__ and `WeChat <https://github.com/OpenBMB/MiniCPM-o/blob/main/assets/wechat-QR.jpeg>`__ group. We are looking forward to seeing you there!


.. toctree::
   :maxdepth: 1
   :caption: Getting Started
   :hidden:

   getting_started/quickstart

.. toctree::
   :maxdepth: 1
   :caption: Inference
   :hidden:

   inference/transformers

.. toctree::
   :maxdepth: 1
   :caption: Deployment
   :hidden:

   deployment/vllm

.. toctree::
   :maxdepth: 1
   :caption: Run Locally
   :hidden:

   run_locally/llama.cpp
   run_locally/ollama
   run_locally/openvino

.. toctree::
   :maxdepth: 1
   :caption: Quantization
   :hidden:

   quantization/awq
   quantization/bnb
   quantization/gguf
   quantization/gptq

.. toctree::
   :maxdepth: 1
   :caption: Training
   :hidden:

   training/llamafactory
   
.. toctree::
   :maxdepth: 1
   :caption: Applications
   :hidden:

   applications/webdemo
   applications/ocr