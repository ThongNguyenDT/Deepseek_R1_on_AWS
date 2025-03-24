---
title: "Details"
date :  "`r Sys.Date()`" 
weight: 3
chapter: false
pre: " <b> 9.3. </b> "
---


# 🚀 Deploying DeepSeek with vLLM on AWS EKS  

### 📌 Overview  
The **DeepSeek with vLLM on EKS** project facilitates the deployment of DeepSeek models on **AWS EKS (Elastic Kubernetes Service)**, optimized for GPU or NeuronCore. Below is a step-by-step guide on setting up the infrastructure, deploying the model, and integrating the chatbot UI.  

---  
### 🏗️ Project Structure  
```
chatbot-ui/
│── application/
│   ├── Dockerfile          # Dockerfile for building the UI container  
│   ├── app.py              # Chatbot UI application (Gradio)  
│   ├── requirements.txt    # Python dependencies  
│
│── manifests/
│   ├── deployment.yaml     # Kubernetes Deployment for UI  
│   ├── ingress-class.yaml  # Ingress configuration  
│
│── static/images/          # UI image assets  
│
│── vllm-chart/             # Helm chart for vLLM  
│   ├── values.yaml         # Default configuration values  
│   ├── templates/
│       ├── deployment.yaml # Pod configuration  
│       ├── service.yaml    # Service configuration  
│       ├── _helpers.tpl    # Template helpers  
│
│── .gitignore  
│── helm.tf                 # Terraform script for Helm configuration  
│── main.tf                 # Terraform infrastructure setup  
│── nodepool_automode.tf    # Auto-scaling node pool configuration  
│── README.md               # Documentation  
```  
---  
### 🔄 Workflow  

#### 1️⃣ Infrastructure Setup with Terraform  
1. **Create VPC and EKS Cluster**  
   - Defined in `main.tf` using the `terraform-aws-modules/eks/aws` module.  
   - Configure **Auto Mode Node Pool** (`nodepool_automode.tf`) to automatically select GPU/Neuron instances.  
   - Create an Amazon ECR repository to store chatbot and vLLM images.  

2. **Configure Node Pool** (`nodepool_automode.tf`)  
   - Set up GPU (`g5/g6/p5`) or Neuron (`inf2`).  
   - Define node selectors, taints, and labels for optimized resource allocation.  

#### 2️⃣ Deploy Model with Helm  
1. **Deploy Helm Chart (`helm.tf`)**  
   - Set up two deployments:  
     - `deepseek_gpu`: Runs on GPU.  
     - `deepseek_neuron`: Runs on Neuron.  
   - Define resource allocation, selectors, and runtime settings for vLLM.  

2. **Configure vLLM Chart (`vllm-chart/`)**  
   - `deployment.yaml`: Defines the vLLM running pod.  
   - `service.yaml`: Configures the service to handle requests to vLLM.  

#### 3️⃣ Deploy Chatbot UI  
1. **Build UI Container (`Dockerfile`)**  
   - Base Image: `python:3.12-slim`  
   - Install dependencies from `requirements.txt`.  
   - Run the app with `uvicorn app:app --host 0.0.0.0 --port 7860`.  

2. **Deploy UI to Kubernetes (`manifests/`)**  
   - `deployment.yaml`: Creates a pod running the UI container.  
   - `ingress-class.yaml`: Configures Ingress with an **Application Load Balancer (ALB)**.  

---  
### ⚙️ Configuration Details  

#### 🌍 **AWS Infrastructure**  
- **EKS Cluster**: Deployed with Terraform.  
- **Node Pool**: Auto-selects GPU or Neuron.  
- **ECR**: Stores container images.  

#### 🛠 **Chatbot Application**  
- **Backend**: Uses `FastAPI` to communicate with vLLM.  
- **Frontend**: Built with `Gradio` for an interactive UI.  
- **Authentication**: Supports login via username/password.  

#### 📦 **vLLM Deployment**  
- **GPU Model**: DeepSeek runs on GPUs (`g5/g6/p5`).  
- **Neuron Model**: DeepSeek runs on NeuronCore (`inf2`).  
- **Resource Requests & Limits**: Optimized resource allocation.  

---  
### 🔒 Security  
- **IAM Role-Based Access Control** for secure permissions.  
- **SSL Certificates** with Ingress Controller.  
- **Kubernetes Secrets** for protecting credentials.  

---  
### 📊 Monitoring & Performance  
- **Liveness & Readiness Probes** for container health checks.  
- **Resource Limits** to prevent overload.  
- **Node Affinity & Taints** for efficient resource scheduling.  