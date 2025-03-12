---
title: "Hand on"
date :  "`r Sys.Date()`" 
weight: 2
chapter: false
pre: " <b> 5.2. </b> "
---



vLLM là một giải pháp mạnh mẽ để tối ưu hóa quá trình suy luận của mô hình AI. Bài hướng dẫn này sẽ giúp bạn thiết lập và triển khai vLLM một cách nhanh chóng và hiệu quả.

---

### 1️⃣ Kiểm tra Python
Trước khi bắt đầu, hãy đảm bảo rằng Python đã được cài đặt trên hệ thống của bạn:
```bash
python3 -V
```
**Khuyến nghị:** Sử dụng phiên bản Python mới nhất để đảm bảo tính tương thích và bảo mật tốt nhất.

---

### 2️⃣ Cài đặt hoặc cập nhật pip
Cài đặt pip (trình quản lý gói Python) bằng lệnh:
```bash
apt install -y python3-pip
```
![Cài đặt pip](https://nodeshift.com/_next/image?url=https%3A%2F%2Fstatic.nodeshift.com%2Fuploads%2F2025%2F01%2Fimage-578-1024x639.png&w=640&q=75)

---

### 3️⃣ Tạo môi trường ảo (Virtual Environment)
Việc sử dụng môi trường ảo giúp quản lý các gói Python một cách độc lập:
```bash
python3 -m venv vllm
source vllm/bin/activate
```
**Lưu ý:** Mỗi khi làm việc với vLLM, bạn cần kích hoạt môi trường ảo.

---

### 4️⃣ Cài đặt vLLM
Cài đặt vLLM bằng lệnh:
```bash
pip install vllm
```
![Cài đặt vLLM](https://nodeshift.com/_next/image?url=https%3A%2F%2Fstatic.nodeshift.com%2Fuploads%2F2025%2F01%2Fimage-582-1024x639.png&w=640&q=75)

**Xử lý lỗi phổ biến:** Nếu gặp lỗi liên quan đến `transformers`, chạy lệnh sau để cập nhật:
```bash
pip install transformers -U
```
![Lỗi transformers](https://nodeshift.com/_next/image?url=https%3A%2F%2Fstatic.nodeshift.com%2Fuploads%2F2025%2F01%2Fimage-586-1024x442.png&w=640&q=75)

---

### 5️⃣ Tải và chạy model
Dùng lệnh sau để khởi chạy vLLM với model AI:
```bash
vllm serve
```
Bạn có thể tải các model khác từ Hugging Face, ví dụ:
```bash
vllm serve "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"
vllm serve "deepseek-ai/DeepSeek-R1-Distill-Llama-8B"
```

**Quan trọng:** Giới hạn số lượng token đầu ra để tránh hết bộ nhớ:
```bash
vllm serve "deepseek-ai/DeepSeek-R1-Distill-Llama-8B" --max_model 4096
```
![Chạy model](https://nodeshift.com/_next/image?url=https%3A%2F%2Fstatic.nodeshift.com%2Fuploads%2F2025%2F01%2Fimage-588-1024x639.png&w=640&q=75)

---

### 6️⃣ Kiểm tra model
Mở một terminal mới và gửi truy vấn đến model bằng `curl`:
```bash
curl -X POST "http://localhost:8000/v1/chat/completions" \
-H "Content-Type: application/json" \
--data '{ "model": "deepseek-ai/DeepSeek-R1-Distill-Llama-8B", "messages": [ { "role": "user", "content": "Tell me the recipe for tea" } ] }'
```
Thay `"content"` bằng prompt của bạn để kiểm tra kết quả.

---

### 📹 Video Demo
Xem video sau để thấy sự khác biệt về hiệu suất giữa vLLM và Flask API truyền thống:
[![Xem Video](https://img.youtube.com/vi/xSt-HLkZC2I/maxresdefault.jpg)](https://youtu.be/xSt-HLkZC2I?t=1045)


