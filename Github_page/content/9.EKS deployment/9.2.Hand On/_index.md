---
title: "Hand On"
date :  "`r Sys.Date()`" 
weight: 2
chapter: false
pre: " <b> 9.2. </b> "
---


**🚀 DeepSeek Deployment Guide**

In this guide, we will deploy **DeepSeek-R1-Distill-Llama-8B**, a lightweight version requiring fewer resources than the full-scale **671-billion parameter model**. If you prefer deploying the full model, simply update the model configuration in vLLM.

---

### 📌 Deployment Prerequisites

We will use **AWS CloudShell** to simplify the setup process.

#### ✅ Check AWS Service Quotas
Ensure your AWS account has sufficient quotas to launch the required **EC2 instances**, especially GPU instances like **G** or **P** series.
🔗 [Check AWS EC2 Instance Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/ec2.html)

#### 🔧 Install Required Tools
- **kubectl** - CLI tool for interacting with Kubernetes.
- **Terraform** - Infrastructure as Code (IaC) tool.
- **Finch or Docker** - Container management tools.

---

### 📜 Step-by-Step Deployment Guide

#### 🛠️ Step 1: Clone the Repository
Clone the GitHub repository containing the necessary configuration files:

```bash
git clone https://github.com/aws-samples/deepseek-using-vllm-on-eks
cd deepseek-using-vllm-on-eks
```

#### ⚙️ Step 2: Initialize and Apply Terraform Configuration
Use Terraform to create an **EKS Cluster, VPC, and ECR Repository**:

```bash
terraform init
terraform apply -auto-approve
```

Configure **kubectl** to connect with the EKS cluster:

```bash
$(terraform output configure_kubectl | jq -r)
```

📌 The `nodepool_automode.tf` file enables **Auto Mode** for node pools, allowing AWS to dynamically manage instance scaling and selection, optimizing performance and cost.

---

### 🚀 Step 3: Deploy DeepSeek Model with vLLM
You can deploy using **GPU** or **Neuron (Inferentia)**. Follow the relevant steps below.

#### 🔹 GPU Deployment

```bash
terraform apply -auto-approve -var="enable_deep_seek_gpu=true" -var="enable_auto_mode_node_pool=true"
```

#### 🔹 Neuron (Inferentia) Deployment

1️⃣ Export the **ECR Repository URI** for Neuron:

```bash
export ECR_repo_neuron=$(terraform output ecr_repository_uri_neuron | jq -r)
```

2️⃣ Clone the vLLM repository:

```bash
git clone https://github.com/vllm-project/vllm
```

3️⃣ Build and push the Neuron-compatible vLLM image:

```bash
finch build --platform linux/amd64 -f Dockerfile.neuron -t $ECR_repo_neuron:0.1 .
aws ecr get-login-password | finch login --username AWS --password-stdin $ECR_repo_neuron
finch push $ECR_repo_neuron:0.1
```

4️⃣ Apply Terraform with Neuron support:

```bash
terraform apply -auto-approve -var="enable_deep_seek_gpu=true" -var="enable_deep_seek_neuron=true" -var="enable_auto_mode_node_pool=true"
```

📌 AWS **Neuron SDK** is optimized for **Inferentia** and **Trainium** chips, making it ideal for efficient inference of large models.

---

### 🏗️ Step 4: Verify Pod and Node Status

#### 🔍 Check running pods:
```bash
kubectl get po -n deepseek
```

#### 🔍 Check active nodes:
```bash
kubectl get nodes -l owner=data-engineer
```

#### 📜 Troubleshoot pending pods:
```bash
kubectl logs deployment.apps/deepseek-gpu-vllm-chart -n deepseek
kubectl logs deployment.apps/deepseek-neuron-vllm-chart -n deepseek
```
🔗 [AWS EC2 Instance Quotas](https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-instance-quotas.html)

---

### 🔄 Step 5: Set Up Local Proxy for Model Interaction

#### 🎯 Neuron (Port **8080**):
```bash
kubectl port-forward svc/deepseek-neuron-vllm-chart -n deepseek 8080:80 > port-forward-neuron.log 2>&1 &
```

#### 🎯 GPU (Port **8081**):
```bash
kubectl port-forward svc/deepseek-gpu-vllm-chart -n deepseek 8081:80 > port-forward-gpu.log 2>&1 &
```

#### 🛠️ Test Model with `curl`:
```bash
curl -X POST "http://localhost:8080/v1/chat/completions" -H "Content-Type: application/json" --data '{
"model": "deepseek-ai/DeepSeek-R1-Distill-Llama-8B",
"messages": [{"role": "user", "content": "What is Kubernetes?"}]
}'
```

📌 The `helm.tf` file customizes the **Helm chart** for vLLM, configuring resource allocation, node selectors, and tolerations for **DeepSeek**.

---

### 🎨 Step 6: Build & Deploy Chatbot UI

1️⃣ Export **ECR Repository URI**:
```bash
export ECR_repo=$(terraform output ecr_repository_uri | jq -r)
```

2️⃣ Build Chatbot UI Image:
```bash
finch build --platform linux/amd64 -t $ECR_repo:0.1 chatbot-ui/application/.
```

3️⃣ Authenticate and Push Image:
```bash
aws ecr get-login-password | finch login --username AWS --password-stdin $ECR_repo
finch push $ECR_repo:0.1
```

4️⃣ Update Deployment Manifest:
```bash
sed -i "s#__IMAGE_DEEPSEEK_CHATBOT__#$ECR_repo:0.1#g" chatbot-ui/manifests/deployment.yaml
sed -i "s|__PASSWORD__|$(openssl rand -base64 12 | tr -dc A-Za-z0-9 | head -c 16)|" chatbot-ui/manifests/deployment.yaml
```

5️⃣ Apply Manifest Files:
```bash
kubectl apply -f chatbot-ui/manifests/ingress-class.yaml
kubectl apply -f chatbot-ui/manifests/deployment.yaml
```

6️⃣ Retrieve Chatbot UI URL:
```bash
echo http://$(kubectl get ingress/deepseek-chatbot-ingress -n deepseek -o json | jq -r '.status.loadBalancer.ingress[0].hostname')
```

7️⃣ Fetch Admin Credentials:
```bash
echo -e "Username=$(kubectl get secret deepseek-chatbot-secrets -n deepseek -o jsonpath='{.data.admin-username}' | base64 --decode)\nPassword=$(kubectl get secret deepseek-chatbot-secrets -n deepseek -o jsonpath='{.data.admin-password}' | base64 --decode)"
```

---

✅ **Deployment Complete!** Your DeepSeek chatbot is now live and ready for interaction. 🚀

