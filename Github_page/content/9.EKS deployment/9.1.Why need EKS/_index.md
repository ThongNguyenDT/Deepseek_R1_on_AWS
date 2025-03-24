---
title: "Why need EKS?"
date :  "`r Sys.Date()`" 
weight: 1
chapter: false
pre: " <b> 9.1. </b> "
---


🚀 **Deploying LLM Models on Kubernetes with AWS EKS** 🌍
<img src="https://miro.medium.com/v2/resize:fit:1200/1*l_1e7ai3MUJmeKQ49w7NjA.jpeg" width="700"/>

## 🔹 Introduction to Kubernetes and AWS EKS

### 🏗️ **What is Kubernetes?**
Kubernetes (K8s) is a powerful **orchestration system** designed to manage, deploy, and scale containerized applications **automatically and flexibly**. It serves as a crucial platform for running **AI/ML applications** at scale.

**Key Features:**
- 🛠 **Auto Scaling for dynamic workload management**
- 🏗 **Efficient resource management**
- 🔄 **Support for Rolling Updates & Rollbacks**
- 🔒 **Security and access control management**

### ☁️ **What is AWS EKS?**
AWS Elastic Kubernetes Service (**AWS EKS**) is a **Managed Kubernetes** service by AWS that simplifies the deployment and operation of Kubernetes on the **AWS cloud**.

**Benefits of AWS EKS:**
- ✅ **Automated Kubernetes management** (reducing operational overhead)
- 🔥 **Seamless integration with AWS services** such as EC2, S3, IAM, Auto Scaling...
- 📈 **Optimized performance & cost efficiency**
- 🛡 **High security with IAM, VPC, and Security Groups**

---

## 🤖 **Using AWS EKS for Deploying LLM Models (DeepSeek)**

### 🌐 **Why Choose Kubernetes & AWS EKS for LLM?**
Deploying Large Language Models (LLM) like **DeepSeek**, LLaMA, and GPT on **Kubernetes** addresses key challenges:

| 🔍 **Challenges** | 🚀 **AWS EKS Solutions** |
|-----------------|------------------------|
| High resource demand (GPU, RAM) | 🖥️ Support for specialized GPUs (NVIDIA, AMD) |
| Need for flexible scaling | 📈 Auto Scaling with HPA & Cluster Autoscaler |
| Managing multiple model versions | 🔄 Canary Deployments & Rolling Updates |
| Fast recovery & fault tolerance | 🛡️ High Availability & Self-healing |

### 🔬 **Case Study: Deploying DeepSeek on AWS EKS**
DeepSeek is a powerful LLM requiring **large-scale resources** for training and inference. AWS EKS provides:

- 📌 **Cost-optimized GPU EC2 instances (A10, A100)**
- 🌊 **Integration with Amazon FSx for Lustre** for high-speed data retrieval
- 🚀 **Auto Scaling** to adjust the number of Pods based on demand
- 🔗 **Istio & KServe integration** for efficient inference management

 🔗 **DEMO !!!**

![](https://github.com/aws-samples/deepseek-using-vllm-on-eks/raw/main/static/images/chatbot.jpg)

---

## 🎯 **Summary**
✅ Kubernetes + AWS EKS is a **powerful platform** for deploying large-scale AI models
✅ Running DeepSeek on AWS EKS ensures **high performance, flexible scaling, and cost efficiency**
✅ Support for GPU, Storage, and Auto Scaling enables **efficient resource management**

🔗 **Learn More:** [AWS EKS Documentation](https://docs.aws.amazon.com/eks/)

🚀 Start deploying your AI models today with **AWS EKS!** 🔥
