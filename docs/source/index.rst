.. MiniCPM Cookbook documentation master file, created by
   sphinx-quickstart on Sat Jul 12 18:12:12 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to MiniCPM-o Cookbook
==============================

.. figure:: assets/minicpm.svg
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

Cook up amazing multimodal AI applications effortlessly with MiniCPM-o / MiniCPM-V, bringing vision, speech, and live-streaming capabilities right to your fingertips!


🌟 What Makes Our Recipes Special?
**********************************

User Groups Covered
~~~~~~~~~~~~~~~~~~~

We support a wide range of users, from individuals to enterprises and researchers.

* **Individuals (Low-barrier, easy inference):** Ollama, Llama.cpp
* **Enterprises (High-throughput inference):** vLLM, SGLang
* **Researchers (Secondary development):** Huggingface Transformers, LLaMA-Factory, SWIFT, Align-anything

Application Scenarios Covered
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our solutions fit various deployment needs and hardware environments.

* **Private deployment:** Web Demo
* **Quantized deployment:** GGUF, BNB, AWQ
* **Edge devices:** iOS, iPad

🔥 Inference recipes
********************

*Ready-to-run examples*

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Recipe
     - Description

   * - **Vision Capabilities**
     - 

   * - 🎬 `Video QA <./inference/video_understanding.md>`_
     - Video-based question answering

   * - 🧩 `Multi-image QA <./inference/multi_images.md>`_
     - Question answering with multiple images

   * - 🖼️ `Single-image QA <./inference/single_image.md>`_
     - Question answering on a single image

   * - 📄 `Document Parser <./inference/pdf_parse.md>`_
     - Parse and extract content from PDFs and webpages

   * - 📝 `Text Recognition <./inference/ocr.md>`_
     - Reliable OCR for photos and screenshots

   * - 🔍 `Multimodal RAG <./inference/rag.md>`_
     - Retrieve and organize multimodal data

   * - 🤖 `Agents <./inference/agent.md>`_
     - AI assistants with tool integration

   * - **Audio Capabilities**
     -

   * - 🎤 `Speech-to-Text <./inference/speech2text.md>`_
     - Multilingual speech recognition

   * - 🎭 `Voice Cloning <./inference/voice_clone.md>`_
     - Realistic voice cloning and role-play

   * - 🗣️ `Text-to-Speech <./inference/text2speech.md>`_
     - Instruction-following speech synthesis

🏋️ Fine-tuning recipes
**********************

*Customize your model with your own ingredients*

**Data preparation**

Follow the `guidance <./finetune/fintune.html#data-preparation>`_ to set up your training datasets.


**Training**

We provide training methods serving different needs as following:

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Method
     - Description
   * - `Full <./finetune/fintune.html#full-parameter-finetuning>`_
     - Comprehensive model customization
   * - `LoRA <./finetune/fintune.html#lora-finetuning>`_
     - Efficient parameter tuning
   * - `LLaMA-Factory <./finetune/llamafactory.html>`_
     - Flexible and modular fine-tuning framework
   * - `SWIFT <./finetune/swift.html>`_
     - Lightweight and fast parameter-efficient tuning
   * - `Align-anything <./finetune/align-anything.html>`_
     - Visual instruction alignment for multimodal models


.. _serving-recipes:

🥡 Serving recipes
******************

*Deploy your model efficiently*

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Method
     - Description
   * - `vLLM <./deployment/vllm.html>`_
     - High-throughput GPU inference
   * - `SGLang <./deployment/sglang.html>`_
     - High-throughput GPU inference
   * - `Llama.cpp <./run_locally/llama.cpp.html>`_
     - Fast CPU inference
   * - `Ollama <./run_locally/ollama.html>`_
     - User-friendly setup
   * - `Web Demo <./demo/webdemo.html>`_
     - Interactive user interface


.. _quantization-recipes:

🥄 Quantization recipes
***********************
*Compress your model to improve efficiency*

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Format
     - Key Feature
   * - `GGUF <./quantization/gguf.html>`_
     - Simplest and most portable format
   * - `BNB <./quantization/bnb.html>`_
     - Efficient 4/8-bit weight quantization


.. _community:

👥 Community
============

.. _contributing:

**Contributing**

We love new recipes! Please share your creative dishes:

1. Fork the repository
2. Create your recipe
3. Submit a pull request


.. _issues-support:

**Issues & Support**

- Found a bug? `Open an issue <https://github.com/OpenBMB/MiniCPM-o/issues>`__
- Need help? Join our `Discord <https://discord.gg/rM6sC9G2MA>`__ and `WeChat <https://github.com/OpenBMB/MiniCPM-o/blob/main/assets/wechat-QR.jpeg>`__ group.

For more information, please visit our:

* `GitHub <https://github.com/OpenBMB>`__
* `Hugging Face <https://huggingface.co/OpenBMB>`__
* `Modelscope <https://modelscope.cn/organization/OpenBMB>`__

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

   quantization/bnb
   quantization/gguf
   

.. toctree::
   :maxdepth: 1
   :caption: finetune
   :hidden:

   finetune/fintune
   finetune/llamafactory
   finetune/swift
   finetune/align-anything
   
.. toctree::
   :maxdepth: 1
   :caption: Demo
   :hidden:

   demo/webdemo
   demo/openwebui