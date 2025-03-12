---
title: "Hand on"
date :  "`r Sys.Date()`" 
weight: 2
chapter: false
pre: " <b> 5.2. </b> "
---

vLLM is a powerful solution for optimizing AI model inference. This guide will help you set up and deploy vLLM quickly and efficiently.

---

### 1️⃣ Check Python Installation
Before starting, ensure Python is installed on your system:
```bash
python3 -V
```
**Recommendation:** Use the latest Python version for optimal compatibility and security.

---

### 2️⃣ Install or Update pip
Install pip (Python package manager) using the command:
```bash
apt install -y python3-pip
```
![Install pip](https://nodeshift.com/_next/image?url=https%3A%2F%2Fstatic.nodeshift.com%2Fuploads%2F2025%2F01%2Fimage-578-1024x639.png&w=640&q=75)

---

### 3️⃣ Create a Virtual Environment
Using a virtual environment helps manage Python packages independently:
```bash
python3 -m venv vllm
source vllm/bin/activate
```
**Note:** Activate the virtual environment each time you work with vLLM.

---

### 4️⃣ Install vLLM
Install vLLM using the command:
```bash
pip install vllm
```
![Install vLLM](https://nodeshift.com/_next/image?url=https%3A%2F%2Fstatic.nodeshift.com%2Fuploads%2F2025%2F01%2Fimage-582-1024x639.png&w=640&q=75)

**Handling common errors:** If you encounter issues related to `transformers`, update it with:
```bash
pip install transformers -U
```
![Transformers error](https://nodeshift.com/_next/image?url=https%3A%2F%2Fstatic.nodeshift.com%2Fuploads%2F2025%2F01%2Fimage-586-1024x442.png&w=640&q=75)

---

### 5️⃣ Load and Run a Model
Start vLLM with an AI model:
```bash
vllm serve
```
You can load various models from Hugging Face, for example:
```bash
vllm serve "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"
vllm serve "deepseek-ai/DeepSeek-R1-Distill-Llama-8B"
```

**Important:** Limit the output token count to prevent memory exhaustion:
```bash
vllm serve "deepseek-ai/DeepSeek-R1-Distill-Llama-8B" --max_model 4096
```
![Run model](https://nodeshift.com/_next/image?url=https%3A%2F%2Fstatic.nodeshift.com%2Fuploads%2F2025%2F01%2Fimage-588-1024x639.png&w=640&q=75)

---

### 6️⃣ Test the Model
Open a new terminal window and send a query to the model using `curl`:
```bash
curl -X POST "http://localhost:8000/v1/chat/completions" \
-H "Content-Type: application/json" \
--data '{ "model": "deepseek-ai/DeepSeek-R1", "messages": [ { "role": "user", "content": "Tell me the recipe for tea" } ] }'
```
Replace the `"content"` field with your desired prompt to test the model response.

---

### 📹 Demo Video
Watch this video to see the performance difference between vLLM and a traditional Flask API:
[![Watch Video](https://img.youtube.com/vi/xSt-HLkZC2I/maxresdefault.jpg)](https://youtu.be/xSt-HLkZC2I?t=1045)


