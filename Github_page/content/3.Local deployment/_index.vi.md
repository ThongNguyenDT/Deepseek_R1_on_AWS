---
title : "Local deployment"
date :  "`r Sys.Date()`" 
weight : 3 
chapter : false
pre : " <b> 3. </b> "
---
## Hướng dẫn triển khai DeepSeek-R1 trên máy local với Ollama

## Giới thiệu
Ollama giúp đơn giản hóa việc chạy các mô hình ngôn ngữ lớn (LLM) trên máy local bằng cách quản lý việc tải xuống, lược bớ và triển khai mô hình một cách mềm mỏ.
![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fzs14jj69iuu1m20yjroi.png)

## Bước 1: Cài đặt Ollama
Truy cập trang web chính thức của Ollama để tải về và cài đặt Ollama như một ứng dụng bình thường.

![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fettkoobbuh63ia4khm34.png)


## Bước 2: Kiểm tra các mô hình DeepSeek-R1 đang có sẵn
Trước khi tải về và chạy DeepSeek-R1, bạn có thể xem danh sách các mô hình đang được hỗ trợ bởi Ollama bằng lệnh:
```bash
ollama list
```
Lệnh này sẽ hiển thị danh sách các mô hình đã được tải về hoặc đang được hỗ trợ trên Ollama.

## Bước 3: Tải về và chạy DeepSeek-R1
Cháy lệnh sau trong terminal để tải về và chạy DeepSeek-R1:
```bash
ollama run deepseek-r1
```
Nếu bạn muốn chạy một phiên bản nhỏ hơn, hãy thay "**Xb**" trong câu lệnh sau bằng kích thước mô hình mong muốn (**1.5b**, **7b**, **8b**, **14b,** **32b**, **70b**, **671b**):
```bash
ollama run deepseek-r1:Xb
```

## Bước 4: Chạy DeepSeek-R1 trong nền
Nếu bạn muốn DeepSeek-R1 chạy liên tục và cung cấp API, hãy khởi động Ollama server:
```bash
ollama serve
```
Lệnh này giúp mô hình sẵn sàng tích hợp với các ứng dụng khác.

## Sử dụng DeepSeek-R1 trên local

### 1. Chạy suy luận (inference) qua CLI
Sau khi tải về, bạn có thể tương tác với DeepSeek-R1 trực tiếp trong terminal.

### 2. Truy cập DeepSeek-R1 qua API
Sử dụng cURL để gửi request API:
```bash
curl http://localhost:11434/api/chat -d '{
  "model": "deepseek-r1",
  "messages": [{ "role": "user", "content": "25 * 25 là bao nhiêu?" }],
  "stream": false
}'
```
Câu lệnh trên gửi một request đến API của DeepSeek-R1 và nhận kết quả trả về.

### 3. Truy cập DeepSeek-R1 qua Python
Cài đặt thư viện Ollama trong Python:
```bash
pip install ollama
```
Sau đó, dùng mã Python sau để tương tác với mô hình:
```python
import ollama
response = ollama.chat(
    model="deepseek-r1",
    messages=[
        {"role": "user", "content": "Giải thích định luật hai của Newton"},
    ],
)
print(response["message"]["content"])
```
Mã Python trên gửi câu hỏi tới mô hình và in kết quả nhận được.

