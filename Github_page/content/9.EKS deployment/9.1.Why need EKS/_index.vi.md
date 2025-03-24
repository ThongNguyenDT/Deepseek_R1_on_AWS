---
title: "Why need EKS?"
date :  "`r Sys.Date()`" 
weight: 1
chapter: false
pre: " <b> 9.1. </b> "
---

🚀 **Triển Khai Mô Hình LLM trên Kubernetes với AWS EKS** 🌍
<img src="https://miro.medium.com/v2/resize:fit:1200/1*l_1e7ai3MUJmeKQ49w7NjA.jpeg" width="700"/>
## 🔹 Giới Thiệu về Kubernetes và AWS EKS

### 🏗️ **Kubernetes là gì?**
Kubernetes (K8s) là một hệ thống **orchestration** mạnh mẽ giúp quản lý, triển khai và mở rộng các ứng dụng container một cách **tự động và linh hoạt**. Đây là nền tảng quan trọng để chạy các ứng dụng **AI/ML** trên quy mô lớn.

**Tính năng chính:**
- 🛠 **Tự động cân bằng tải (Auto Scaling)**
- 🏗 **Quản lý tài nguyên hiệu quả**
- 🔄 **Hỗ trợ Rolling Updates & Rollbacks**
- 🔒 **Quản lý bảo mật và quyền truy cập**

### ☁️ **AWS EKS là gì?**
AWS Elastic Kubernetes Service (**AWS EKS**) là dịch vụ **Managed Kubernetes** của AWS, giúp đơn giản hóa việc triển khai và vận hành Kubernetes trên nền tảng **đám mây AWS**.

**Lợi ích của AWS EKS:**
- ✅ **Quản lý Kubernetes tự động** (ít tốn công sức quản trị)
- 🔥 **Tích hợp sẵn với dịch vụ AWS** như EC2, S3, IAM, Auto Scaling...
- 📈 **Tối ưu hiệu suất & chi phí**
- 🛡 **Bảo mật cao với IAM, VPC, Security Groups...**

---

## 🤖 **Ứng Dụng AWS EKS trong việc triển khai Mô Hình LLM (DeepSeek)**

### 🌐 **Tại sao chọn Kubernetes & AWS EKS cho LLM?**
Triển khai Large Language Models (LLM) như **DeepSeek**, LLaMA, GPT trên **Kubernetes** giúp giải quyết các bài toán quan trọng:

| 🔍 **Thách thức** | 🚀 **Giải pháp AWS EKS** |
|-----------------|------------------------|
| Yêu cầu tài nguyên lớn (GPU, RAM) | 🖥️ Hỗ trợ GPU chuyên dụng (NVIDIA, AMD) |
| Mô hình cần mở rộng linh hoạt | 📈 Auto Scaling với HPA & Cluster Autoscaler |
| Quản lý nhiều phiên bản mô hình | 🔄 Canary Deployments & Rolling Updates |
| Khả năng phục hồi nhanh | 🛡️ High Availability & Self-healing |

### 🔬 **Case Study: Triển khai DeepSeek trên AWS EKS**
DeepSeek là một mô hình LLM mạnh mẽ, yêu cầu **tài nguyên lớn** để huấn luyện và suy luận (inference). AWS EKS giúp:

- 📌 **Dùng GPU EC2 (A10, A100) tối ưu chi phí**
- 🌊 **Tích hợp với Amazon FSx for Lustre** để truy xuất dữ liệu nhanh
- 🚀 **Auto Scaling** điều chỉnh số lượng Pod dựa trên nhu cầu
- 🔗 **Kết hợp với Istio, KServe** để quản lý inference

** 🔗DEMO !!!**

![](https://github.com/aws-samples/deepseek-using-vllm-on-eks/raw/main/static/images/chatbot.jpg)

---

## 🎯 **Tóm Tắt**
✅ Kubernetes + AWS EKS là nền tảng mạnh mẽ giúp **triển khai mô hình AI quy mô lớn**
✅ DeepSeek chạy trên AWS EKS đảm bảo **hiệu suất cao, mở rộng linh hoạt, giảm chi phí**
✅ Hỗ trợ GPU, Storage, Auto Scaling giúp quản lý tài nguyên hiệu quả

🔗 **Xem thêm:** [AWS EKS Documentation](https://docs.aws.amazon.com/eks/)

🚀 Hãy bắt đầu triển khai mô hình AI của bạn ngay hôm nay với **AWS EKS!** 🔥
