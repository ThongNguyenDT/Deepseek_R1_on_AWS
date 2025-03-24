---
title: "Details"
date :  "`r Sys.Date()`" 
weight: 3
chapter: false
pre: " <b> 9.3. </b> "
---

**🚀 Triển Khai DeepSeek sử dụng vLLM trên AWS EKS**

### 📌 Tổng Quan
Dự án **DeepSeek sử dụng vLLM trên EKS** giúp triển khai mô hình DeepSeek trên **AWS EKS (Elastic Kubernetes Service)**, tối ưu hóa với GPU hoặc NeuronCore. Dưới đây là hướng dẫn chi tiết về cách thiết lập hạ tầng, triển khai mô hình và ứng dụng UI chatbot.

---
### 🏗️ Cấu Trúc Dự Án
```
chatbot-ui/
│── application/
│   ├── Dockerfile          # Dockerfile để build container UI
│   ├── app.py              # Ứng dụng UI chatbot (Gradio)
│   ├── requirements.txt    # Dependencies của Python app
│
│── manifests/
│   ├── deployment.yaml     # Kubernetes Deployment cho UI
│   ├── ingress-class.yaml  # Cấu hình Ingress
│
│── static/images/          # Chứa các file ảnh UI
│
│── vllm-chart/             # Helm chart cho vLLM
│   ├── values.yaml         # Giá trị cấu hình mặc định
│   ├── templates/
│       ├── deployment.yaml # Pod Configuration
│       ├── service.yaml    # Cấu hình Service
│       ├── _helpers.tpl    # Template helpers
│
│── .gitignore
│── helm.tf                 # Terraform cấu hình Helm
│── main.tf                 # Terraform cấu hình hạ tầng
│── nodepool_automode.tf    # Cấu hình node pool tự động
│── README.md               # Tài liệu hướng dẫn
```
---
### 🔄 Luồng Xử Lý

#### 1️⃣ Khởi tạo hạ tầng với Terraform
1. **Tạo VPC và EKS Cluster**
   - Được định nghĩa trong `main.tf` với module `terraform-aws-modules/eks/aws`.
   - Cấu hình Auto Mode Node Pool (`nodepool_automode.tf`) để tự động chọn instance GPU/Neuron.
   - Tạo repository trên Amazon ECR để lưu trữ image của chatbot và vLLM.
   
2. **Cấu hình node pool** (`nodepool_automode.tf`)
   - Thiết lập GPU (`g5/g6/p5`) hoặc Neuron (`inf2`).
   - Định nghĩa node selector, taints, labels để phân bổ tài nguyên hợp lý.

#### 2️⃣ Triển khai mô hình với Helm
1. **Triển khai Helm chart (`helm.tf`)**
   - Cài đặt hai deployment:
     - `deepseek_gpu`: Chạy trên GPU.
     - `deepseek_neuron`: Chạy trên Neuron.
   - Định nghĩa tài nguyên, selector, môi trường runtime cho vLLM.
   
2. **Cấu hình vLLM Chart (`vllm-chart/`)**
   - `deployment.yaml`: Định nghĩa Pod chạy vLLM.
   - `service.yaml`: Cấu hình Service để vLLM có thể nhận request.

#### 3️⃣ Triển khai UI Chatbot
1. **Build container UI (`Dockerfile`)**
   - Base Image: `python:3.12-slim`
   - Cài đặt dependencies từ `requirements.txt`.
   - Chạy app với `uvicorn app:app --host 0.0.0.0 --port 7860`.
   
2. **Triển khai UI lên Kubernetes (`manifests/`)**
   - `deployment.yaml`: Tạo Pod chạy UI container.
   - `ingress-class.yaml`: Cấu hình Ingress với ALB (Application Load Balancer).

---
### ⚙️ Cấu Hình Chi Tiết

#### 🌍 **Hạ tầng AWS**
- **EKS Cluster**: Triển khai với Terraform.
- **Node Pool**: Tự động chọn GPU hoặc Neuron.
- **ECR**: Lưu trữ container images.

#### 🛠 **Ứng dụng Chatbot**
- **Backend**: Sử dụng `FastAPI` để giao tiếp với vLLM.
- **Frontend**: Dùng `Gradio` để tạo UI tương tác.
- **Authentication**: Hỗ trợ login với username/password.

#### 📦 **Triển khai vLLM**
- **GPU Model**: DeepSeek chạy trên GPU (g5/g6/p5).
- **Neuron Model**: DeepSeek chạy trên NeuronCore (inf2).
- **Resource Requests & Limits**: Giới hạn tài nguyên theo nhu cầu.

---
### 🔒 Bảo Mật
- **Sử dụng IAM Role** để quản lý quyền truy cập.
- **Chứng chỉ SSL** với Ingress Controller.
- **Secrets trong Kubernetes** để bảo vệ credentials.

---
### 📊 Giám Sát & Hiệu Năng
- **Liveness & Readiness Probes** để kiểm tra trạng thái container.
- **Resource Limits** để tránh quá tải.
- **Node Affinity & Taints** để tối ưu hóa phân bổ tài nguyên.

