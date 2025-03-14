---
title: "Hand on"
date :  "`r Sys.Date()`" 
weight: 2
chapter: false
pre: " <b> 6.2. </b> "
---
**Hướng dẫn triển khai model DeepSeek trên AWS Inferentia với vLLM**

### Giới thiệu
Model DeepSeek, đặc biệt là phiên bản tinh gọn như DeepSeek-R1-Distill-Llama-8B và 70B, được thiết kế để tối ưu hiệu suất suy luận, rất phù hợp với việc triển khai trên AWS Inferentia. Thư viện vLLM cung cấp khả năng phục vụ mô hình linh hoạt và tối ưu. Bài viết này hướng dẫn bạn triển khai model DeepSeek trên máy ảo EC2 của AWS sử dụng vLLM một cách chuyên nghiệp, hiệu quả.

---

### Bước 1: Khởi chạy Instance EC2

#### Yêu cầu trước khi bắt đầu
- Tài khoản AWS đang hoạt động.
- Quyền hạn đủ để tạo và quản lý EC2.
- Hạn mức dịch vụ ("Service Quota") có ít nhất 96 đối với Running On-Demand Inf Instances.
- Tạo một cặp key pair để truy cập SSH.

#### Khởi chạy EC2
1. Truy cập [AWS Management Console](https://console.aws.amazon.com/), chọn "EC2".
2. Nhấn "Launch Instance".
3. Chọn "Deep Learning AMI Neuron" (Ubuntu 22.04) vì nó đã cài sẵn Neuron SDK.
4. Chọn "inf2.24xlarge" hoặc lớn hơn cho model 70B. Hãy chọn các instant phù hợp với model và nhu cầu của bạn
5. Cấu hình volume gốc 500GB gp3.
6. Cấu hình truy cập bằng key pair.
7. Nhấn "Launch Instance".

#### Kết nối vào Instance
Sao chép DNS công khai của instance và kết nối bằng lệnh:
```bash
ssh -i /path/to/key-pair.pem ubuntu@instance-public-dns-name
```
Nhớ đặt quyền truy cập key pair là 400.

---

### Bước 2: Cài đặt vLLM

#### Kích hoạt môi trường
```bash
source /opt/aws_neuronx_venv_pytorch_2_5_nxd_inference/bin/activate
```

#### Cài git-lfs
```bash
sudo apt-get install git-lfs
```
```bash
git lfs install
```

#### Cài vLLM
```bash
git clone https://github.com/vllm-project/vllm
cd vllm
pip install -U -r requirements-neuron.txt
pip install .
```

---

### Bước 3: Tải Model DeepSeek từ Hugging Face

> Bạn phải cài huggingface-cli phù hợp với môi trường của bạn trước khi tiến hành các bước tiếp theo

#### Đăng nhập Hugging Face
Truy cập [Hugging Face](https://huggingface.co/settings/tokens) và đăng nhập:

```bash
huggingface-cli login
```

#### Tải model
- Model 8B:
  ```bash
  huggingface-cli download deepseek-ai/DeepSeek-R1-Distill-Llama-8B
  ```
- Model 70B:
  ```bash
  huggingface-cli download deepseek-ai/DeepSeek-R1-Distill-Llama-70B
  ```

#### Thiết lập đường dẫn
Đường dẫn đến file lưu model có thể nằm ở `/home/ubuntu/.cache/huggingface/hub/models--deepseek-ai--DeepSeek-R1-Distill-Llama-8B/snapshots/d66bcfc2f3fd52799f95943264f32ba15ca0003d/`
```bash
export MODEL_PATH=/path/to/your/model
```

---

### Bước 4: Chạy vLLM và kiểm tra suy luận

#### Khởi chạy model
```bash
vllm serve $MODEL_PATH
```
Máy chủ sẽ hoạt động trên `localhost:8000`.

Bạn có thể thiết lập một số thông só của model của bạn như sau:

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

#### Kiểm tra bằng curl
```bash
curl -X POST http://localhost:8000/v1/chat/completions -d '{ "model": "deepseek-r1-distill-lama-8b", "messages": [ { "role": "user", "content": "Hello, world!" } ] }'
```
