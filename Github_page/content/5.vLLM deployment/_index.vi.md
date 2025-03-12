---
title: "vLLM deployment"
date :  "`r Sys.Date()`" 
weight: 5
chapter: false
pre: " <b> 5. </b> "
---

![](https://docs.vllm.ai/en/latest/_images/vllm-logo-text-light.png)
### 1. Giới thiệu

Trong phần này, chúng ta sẽ cùng nhau khám phá cách triển khai thực tế một mô hình ngôn ngữ lớn (LLM) từ môi trường local lên server một cách tối ưu chi phí nhất. 

Một trong những thách thức lớn trong quá trình này là làm sao để thiết kế một ứng dụng mạnh mẽ, có thể xử lý nhiều request đồng thời trên phần cứng giới hạn mà vẫn đảm bảo hiệu suất cao.

Để giải quyết vấn đề này, chúng ta sẽ tìm hiểu về **vLLM** 

### 2. Nội dung

Trong phần này, chúng ta sẽ trải qua hai nội dung chính:

1. **Tìm hiểu về vLLM** – Cách hoạt động, lợi ích và ứng dụng thực tế của vLLM trong việc tối ưu hóa suy luận mô hình ngôn ngữ lớn.
2. **Triển khai DeepSeek R1 Distill trên vLLM** – Hướng dẫn chi tiết về cách triển khai một mô hình tinh gọn (distill) trên vLLM để đạt được hiệu suất cao với chi phí thấp.

Hãy cùng bắt đầu khám phá vLLM và cách nó giúp tăng tốc suy luận cho các mô hình LLM!

