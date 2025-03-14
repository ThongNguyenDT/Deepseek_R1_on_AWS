---
title: "Hand on"
date :  "`r Sys.Date()`" 
weight: 2
chapter: false
pre: " <b> 6.2. </b> "
---
**Deploying DeepSeek Model on AWS Inferentia with vLLM**

### Introduction
The DeepSeek model, particularly optimized versions like DeepSeek-R1-Distill-Llama-8B and 70B, is designed to enhance inference efficiency, making it well-suited for deployment on AWS Inferentia. The vLLM library provides a flexible and optimized model serving capability. This guide walks you through deploying the DeepSeek model on an AWS EC2 instance using vLLM in a professional and efficient manner.

---

### Step 1: Launching an EC2 Instance

#### Prerequisites
- An active AWS account.
- Sufficient permissions to create and manage EC2 instances.
- A service quota of at least 96 for Running On-Demand Inf Instances.
- A key pair created for SSH access.

#### Launching an EC2 Instance
1. Navigate to the [AWS Management Console](https://console.aws.amazon.com/) and select "EC2".
2. Click "Launch Instance".
3. Choose "Deep Learning AMI Neuron" (Ubuntu 22.04) as it comes pre-installed with Neuron SDK.
4. Select "inf2.24xlarge" or a higher-tier instance for the 70B model. Choose an appropriate instance based on your model and requirements.
5. Configure a 500GB gp3 root volume.
6. Set up SSH access using the key pair.
7. Click "Launch Instance".

#### Connecting to the Instance
Copy the public DNS of the instance and connect using the following command:
```bash
ssh -i /path/to/key-pair.pem ubuntu@instance-public-dns-name
```
Ensure the key pair file has the correct permissions set to 400.

---

### Step 2: Installing vLLM

#### Activating the Environment
```bash
source /opt/aws_neuronx_venv_pytorch_2_5_nxd_inference/bin/activate
```

#### Installing git-lfs
```bash
sudo apt-get install git-lfs
```
```bash
git lfs install
```

#### Installing vLLM
```bash
git clone https://github.com/vllm-project/vllm
cd vllm
pip install -U -r requirements-neuron.txt
pip install .
```

---

### Step 3: Downloading the DeepSeek Model from Hugging Face

> Ensure that `huggingface-cli` is installed in your environment before proceeding.

#### Logging into Hugging Face
Visit [Hugging Face Tokens](https://huggingface.co/settings/tokens) and log in:
```bash
huggingface-cli login
```

#### Downloading the Model
- For the 8B model:
  ```bash
  huggingface-cli download deepseek-ai/DeepSeek-R1-Distill-Llama-8B
  ```
- For the 70B model:
  ```bash
  huggingface-cli download deepseek-ai/DeepSeek-R1-Distill-Llama-70B
  ```

#### Setting the Model Path
The model files are typically stored in:
`/home/ubuntu/.cache/huggingface/hub/models--deepseek-ai--DeepSeek-R1-Distill-Llama-8B/snapshots/d66bcfc2f3fd52799f95943264f32ba15ca0003d/`

Set the model path environment variable:
```bash
export MODEL_PATH=/path/to/your/model
```

---

### Step 4: Running vLLM and Testing Inference

#### Launching the Model Server
```bash
vllm serve $MODEL_PATH
```
The server will be available at `localhost:8000`.

You can further configure the model with the following command:
```bash
cd ~/vllm/

python3 -m vllm.entrypoints.openai.api_server \
    --model $MODEL_PATH \
    --served-model-name DeepSeek-R1-Distill-Llama-8B \
    --tensor-parallel-size 8 \
    --max-model-len 2048 \
    --max-num-seqs 4 \
    --block-size 8 \
    --use-v2-block-manager \
    --device neuron \
    --port 8080
```

#### Testing with Curl
```bash
curl -X POST http://localhost:8000/v1/chat/completions -d '{ "model": "deepseek-r1-distill-lama-8b", "messages": [ { "role": "user", "content": "Hello, world!" } ] }'
```

