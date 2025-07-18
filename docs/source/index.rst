.. MiniCPM Cookbook documentation master file, created by
   sphinx-quickstart on Sat Jul 12 18:12:12 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to MiniCPM-o Cookbook
==============================
.. figure:: assets/minicpm-logo.svg
  :width: 70%
  :align: center
  :alt: MiniCPM
  :class: no-scaled-link

.. raw:: html

   <br>

.. _`🏠 Main Repository`: https://github.com/OpenBMB/MiniCPM-o 
.. _`🤗 Hugging Face`: https://huggingface.co/openbmb/MiniCPM-o-4 
.. _`🤖 ModelScope`: https://modelscope.cn/models/openbmb/MiniCPM-o-4 
.. _`📖 Technical Blog`: https://openbmb.notion.site/MiniCPM-o-2-6-A-GPT-4o-Level-MLLM-for-Vision-Speech-and-Multimodal-Live-Streaming-on-Your-Phone-185ede1b7a558042b5d5e45e6b237da9 

| `🏠 Main Repository`_  |  `🤗 Hugging Face`_  |  `🤖 ModelScope`_  |  `📖 Technical Blog`_ 

**MiniCPM-V / MiniCPM-o** is a lightweight, high-performance edge-side large multimodal model jointly developed by ModelBest, the OpenBMB, and the Tsinghua NLP Lab. Both multimodal models are pretrained on large-scale multilingual and multimodal datasets, and subsequently fine-tuned on high-quality data to align with human preferences.
MiniCPM can perform natural language understanding, text generation, visual comprehension, tool utilization, role-playing, and function as an AI agent, among other capabilities.

The latest version, MiniCPM-V 4.0,  includes the following key features:

.. rubric:: 🎯 **GPT-4V Level Performance**

- Surpasses GPT-4V in single-image, multi-image, and video understanding
- Advanced multimodal reasoning capabilities
- Real-time video understanding on iPad

.. rubric:: 📱 **Edge-Friendly & Efficient**

- Only 4B parameters of pure AI magic
- Smooth and fast inference on iPad
- Efficient memory usage (~3GB RAM)
- **Nature Published** – Research in prestigious `Nature Communications <https://www.nature.com/articles/s41467-025-61040-5>`__!

.. rubric:: 🌍 **Multilingual & Creative**

- 30+ languages supported
- Cross-language understanding
- Advanced OCR capabilities
- Multimodal reasoning & analysis

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
   getting_started/model_download

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
   deployment/sglang

.. toctree::
   :maxdepth: 1
   :caption: Run Locally
   :hidden:

   run_locally/llama.cpp
   run_locally/ollama

.. toctree::
   :maxdepth: 1
   :caption: Quantization
   :hidden:

   quantization/awq
   quantization/bnb
   quantization/gguf
   

.. toctree::
   :maxdepth: 1
   :caption: finetune
   :hidden:

   finetune/fintune
   finetune/llamafactory
   
.. toctree::
   :maxdepth: 1
   :caption: Demo
   :hidden:

   demo/webdemo
   demo/openwebui