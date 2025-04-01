---
title: "Basic agent with n8n"
date :  "`r Sys.Date()`" 
weight: 1
chapter: false
pre: " 1. "
---

**n8n** (pronounced "n-eight-n" or "nodemation") is a powerful open-source workflow automation tool that enables you to connect applications, APIs, and services with minimal coding. With an intuitive UI and built-in AI integrations, n8n is the perfect choice for building AI agents, such as chatbots and virtual assistants.

### Why Choose n8n?
✅ **Self-hosted** – Keep your data secure and private.\
✅ **Cost-effective** – Avoid expensive cloud services.\
✅ **Extensive integrations** – Supports over **400+ services**, including Google Sheets and Slack. \
✅ **AI-ready** – Seamlessly connects with Large Language Models (LLMs) like Ollama. \ 

👉 Learn more in the [official n8n documentation](https://docs.n8n.io/).

---

## 🐳 Deploying n8n and Ollama with Docker

We will deploy n8n and Ollama locally using **Docker**, leveraging the [self-hosted AI starter kit](https://github.com/n8n-io/self-hosted-ai-starter-kit). This setup ensures fast and easy deployment across different hardware configurations.

### System Requirements
- Installed **Docker** and **Docker Compose**.
- Supported hardware: CPU, Nvidia GPU, Mac/Apple Silicon, or AMD GPU on Linux.

### Step-by-Step Deployment Guide

#### 🔹 1. Clone the Repository
```bash
git clone https://github.com/n8n-io/self-hosted-ai-starter-kit.git
cd self-hosted-ai-starter-kit
```

#### 🔹 2. Select the Right Configuration for Your Hardware
Depending on your setup, use one of the following commands:

- **CPU only:**
  ```bash
  docker compose --profile cpu up
  ```
- **Nvidia GPU:**
  ```bash
  docker compose --profile gpu-nvidia up
  ```
  *Ensure Nvidia drivers and CUDA are installed. More details: [Ollama Docker](https://github.com/ollama/ollama/blob/main/docs/docker.md).*
- **Mac/Apple Silicon:**
  ```bash
  docker compose up
  ```
  *Modify `docker-compose.yml` to add:* `OLLAMA_HOST=host.docker.internal:11434`
- **AMD GPU (Linux):**
  ```bash
  docker compose --profile gpu-amd up
  ```

#### 🔹 3. Verify and Access
- Open **n8n UI**: `http://localhost:5678/`
- Configure credentials: `http://localhost:5678/home/credentials`
- Ensure **Ollama** is running: `http://localhost:11434/` (Test with `curl http://localhost:11434/`)

#### 🔹 4. Upgrade (Optional)
To update to the latest version:
```bash
docker compose --profile gpu-nvidia pull && docker compose create && docker compose --profile gpu-nvidia up
```

---

## 🤖 Building a Simple AI Agent Workflow

Now, let's create a **workflow** showcasing how an AI agent operates using n8n and the **DeepSeek Distill 8b** model. The workflow processes user queries, analyzes intent, performs tool calls (e.g., web search), and returns responses.
<img src="/images/11.Agent/11.2.sample agent/11.2.1.N8n/img.png"/>
### 🏁 Step 1: Access the n8n Workspace
🔗 Open: `http://localhost:5678`
🆕 First-time users: Register with **email** and **password**.

### 🛠️ Step 2: Create a New Workflow
1️⃣ Click **"Create a new workflow"**.

### 💬 Step 3: Add a "Chat" Node
1️⃣ Click **`+`** to add a new node.
2️⃣ Search for **"Chat"** and select it.

### 🤖 Step 4: (Optional) Create a New AI Agent
🔹 In the **Chat node settings**, you can create an **AI Agent** for advanced conversation management.

### 📌 Step 5: Select the Ollama Chat Model
1️⃣ Navigate to **Chat node settings**.
2️⃣ Select **Ollama Chat Model**.

### 🔑 Step 6: Create New Ollama Credentials
💡 If you haven’t added **Ollama credentials**, click **"Create new credential"**.

### ⚠️ Step 7: Configure Ollama Connection (Important!)
1️⃣ Locate the **"Base URL"** field.
2️⃣ **DO NOT** use `http://localhost:11434`.
3️⃣ Instead, enter:
   ```bash
   http://host.docker.internal:11434
   ```
4️⃣ Click **"Save"**.
5️⃣ Test the connection—if successful, you’ll see **"Connection test successfully"**.
🚨 *Incorrect settings will prevent n8n from connecting to Ollama!*

### 🏷️ Step 8: Select a Large Language Model (LLM)
✅ Choose from available LLMs, such as:
   - `Llama 3.1`
   - `Gemma 2 2B`
   - `deepseek 1.5B`

### 🗃️ Step 9: (Optional) Add "Buffer Memory" Node
📝 Improves conversational memory for better AI interactions.

### ✅ Step 10: Test the Workflow
1️⃣ Click **"Chat"** in the Chat node.
2️⃣ Enter a test message, e.g., `Hello, how are you?`
3️⃣ If successful, you will receive a response from your AI model.

🎉 Congratulations! You've successfully set up n8n with Ollama to run an AI model locally. 🚀

---

## 🎨 Advanced Tips & Pro Insights

### 🔹 Tool Calling Support
- **Only the 32b model** supports native tool calls.
- For other versions, try community mods like [deepseek-r1-tool-calling](https://ollama.com/MFDoom/deepseek-r1-tool-calling).

### 🔹 Optimization
- With high-end GPUs (e.g., RTX 4090), increase context length up to **16K** for complex tasks.

### 🔹 Expert Tips
- Join the [n8n community](https://community.n8n.io/t/ollama-and-toolagent/61232) for the latest solutions.
- Check Ollama logs for debugging: `docker logs <container-id>`.

🚀 Now, you're ready to build powerful AI-powered workflows with n8n! Happy automating! 🎯