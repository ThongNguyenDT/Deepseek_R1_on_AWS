---
title: "About vLLM"
date :  "`r Sys.Date()`" 
weight: 1
chapter: false
pre: " <b> 5.1. </b> "
---

### 1. vLLM là gì?

[vLLM](https://github.com/vllm-project/vllm) là một thư viện tối ưu suy luậu cho các mô hình ngôn ngữ lớn (LLM - Large Language Models), được thiết kế để tăng tốc độ sinh văn bản, tối ưu bộ nhớ và hỗ trợ môi trường đa GPU. Công nghệ **PagedAttention** trong vLLM giúp giảm thiểu chi phí bộ nhớ và tối đa hiệu suất khi xử lý batch lớn.

![](https://docs.vllm.ai/en/latest/_images/vllm-logo-text-light.png)

### 2. Tại sao cần vLLM?

Với xu hướng tăng trưởng nhanh chóng của các mô hình ngôn ngữ lớn trong các lĩnh vực như chatbot, tổng hợp văn bản, dịch thuật và hỗ trợ lập trình, những thách thức khi triển khai LLM ngày càng lớn:

- **Hiệu suất suy luậu chậm**: Quá trình sinh token tuần tự làm giảm tốc độ phản hồi.
- **Bộ nhớ GPU hạn chế**: Việc quản lý bộ nhớ khi xử lý batch lớn trên GPU dễ gây tràn bộ nhớ.
- **Khó mở rộng quy mô**: Việc tăng throughput bằng nhiều GPU gặp nhiều rào cản kỹ thuật.

vLLM giúp giải quyết những vấn đề trên, mang lại hiệu suất vượt trội và tối đa hóa tài nguyên.

### 3. Công dụng vLLM

#### 3.1. Tăng tốc suy luậu

vLLM tối đa tốc độ sinh văn bản nhờ cơ chế **PagedAttention**, giúp quản lý bộ nhớ hiệu quả và giảm latency.

#### 3.2. Tối ưu bộ nhớ GPU

PagedAttention giúp giảm bộ nhớ tiêu tụ nhờ việc tổ chức cache KV (Key-Value) hiệu quả, cho phép batch lớn hơn mà không bị tràn bộ nhớ.

#### 3.3. Hỗ trợ đa GPU và phân tán

vLLM khai thác nhiều GPU một cách linh hoạt, giúp gia tăng throughput mà không gây nghẹn tắc tài nguyên.

#### 3.4. Dễ dàng tích hợp

- API tương thích với **Hugging Face Transformers**, giúp chuyển đổi dễ dàng.
- Hỗ trợ **OpenAI-compatible API**, tích hợp nhanh vào các hệ thống chatbot.

### 4. Sự vượt trội của vLLM

#### 4.1. Benchmark vLLM vs. Hugging Face Transformers

| Mô hình | vLLM (Tokens/s) | HF Transformers (Tokens/s) | Cải thiện |
|---------|----------------|----------------------------|-----------|
| GPT-3 6.7B | 200 | 120 | ~1.67x |
| GPT-3 13B | 150 | 80 | ~1.87x |
| LLaMA-2 7B | 180 | 110 | ~1.63x |

#### 4.2. Hiệu quả bộ nhớ và throughput

- **PagedAttention giúp giảm lãng phí bộ nhớ dưới 4%**, tăng tốc xử lý.
- **Parallel Sampling tối ưu**: Giảm bộ nhớ tôn hao khi sinh song song lên tới **55%**.
- Trong các bài kiểm tra thực tế, vLLM **vượt HF Transformers 14x-24x về throughput**.
- So với Hugging Face Text Generation Inference (TGI), vLLM vẫn **nhanh hơn tới 3.5x**.
- Cùng một hạ tầng phần cứng, vLLM giúp xử lý **gấp 5 lần lưu lượng** mà không cần thêm GPU.

