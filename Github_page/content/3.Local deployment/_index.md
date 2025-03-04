---
title : "Local deployment"
date :  "`r Sys.Date()`" 
weight : 3
chapter : false
pre : " <b> 3. </b> "
---

**_🚀 Deploying DeepSeek-R1 Locally with Ollama_**

### 🌟 Introduction
[Ollama](https://ollama.ai) simplifies running large language models (LLMs) on your local machine by handling model downloads, optimization, and seamless deployment.

![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fzs14jj69iuu1m20yjroi.png)


### 🛠️ Step 1: Install Ollama
Visit the official [Ollama website](https://ollama.ai) to download and install Ollama like any other application.

![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fettkoobbuh63ia4khm34.png)

### 🔍 Step 2: Check Available DeepSeek-R1 Models
Before downloading and running DeepSeek-R1, you can check the list of available models supported by Ollama using:

```bash
ollama list
```
This command displays the models you have already downloaded or that are available for use.



### 📥 Step 3: Download & Run DeepSeek-R1
Run the following command in your terminal to download and launch DeepSeek-R1:

```bash
ollama run deepseek-r1
```
If you want to use a specific model size, replace `Xb` in the command below with the desired size (**1.5b**, **7b**, **8b**, **14b**, **32b**, **70b**, **671b**):

```bash
ollama run deepseek-r1:Xb
```



### ⚡ Step 4: Run DeepSeek-R1 in the Background
To keep DeepSeek-R1 running as a background service and enable API access, start the Ollama server:

```bash
ollama serve
```
This allows seamless integration with other applications.



### 💡 Using DeepSeek-R1 Locally

#### 🖥️ 1. Perform Inference via CLI
Once installed, interact with DeepSeek-R1 directly from your terminal.

#### 🌐 2. Access DeepSeek-R1 via API
Use `cURL` to send API requests:

```bash
curl http://localhost:11434/api/chat -d '{
  "model": "deepseek-r1",
  "messages": [{ "role": "user", "content": "What is 25 * 25?" }],
  "stream": false
}'
```
This command sends a request to the DeepSeek-R1 API and retrieves the response.

#### 🐍 3. Interact with DeepSeek-R1 in Python
First, install the `ollama` Python package:

```bash
pip install ollama
```
Then, use the following Python script to communicate with the model:

```python
import ollama

response = ollama.chat(
    model="deepseek-r1",
    messages=[
        {"role": "user", "content": "Explain Newton's Second Law."},
    ],
)

print(response["message"]["content"])
```
This script sends a query to the model and prints the response.



🎉 **Now you’re all set to run DeepSeek-R1 locally with Ollama!** 🚀


