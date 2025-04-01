---
title: "Basic agent with n8n"
date :  "`r Sys.Date()`" 
weight: 1
chapter: false
pre: " 1. "
---


**_Triển Khai AI Agent Đơn Giản với n8n và Ollama Locally cho Mô Hình DeepSeek Distill_**

![n8n and Ollama Banner](https://raw.githubusercontent.com/n8n-io/self-hosted-ai-starter-kit/main/assets/n8n-demo.gif)



### 📘 Giới Thiệu về n8n: Công Cụ Tự Động Hóa Đỉnh Cao

**n8n** (phát âm là "n-eight-n" hoặc "nodemation") là một công cụ tự động hóa workflow mã nguồn mở mạnh mẽ, cho phép bạn kết nối các ứng dụng, API và dịch vụ mà không cần viết nhiều mã code. Với giao diện trực quan và khả năng tích hợp AI native, n8n là lựa chọn hoàn hảo để xây dựng các AI agent như chatbot hoặc trợ lý ảo.

#### **Tại Sao Chọn n8n?**
- **Tự host:** Giữ dữ liệu của bạn an toàn và riêng tư trên máy cục bộ.
- **Tiết kiệm chi phí:** Không cần phụ thuộc vào các dịch vụ đám mây đắt đỏ.
- **Tích hợp đa dạng:** Hỗ trợ hơn **400 dịch vụ**, từ Google Sheets đến Slack.
- **AI-ready:** Dễ dàng kết nối với các mô hình ngôn ngữ lớn (LLM) như Ollama.

Nếu bạn muốn tìm hiểu thêm, hãy ghé thăm [tài liệu chính thức của n8n](https://docs.n8n.io/).

---

### 🐳 Hướng Dẫn Triển Khai n8n và Ollama với Docker

Để bắt đầu, chúng ta sẽ triển khai n8n cùng Ollama cục bộ bằng **Docker**, sử dụng [self-hosted AI starter kit](https://github.com/n8n-io/self-hosted-ai-starter-kit). Bộ công cụ này giúp bạn thiết lập mọi thứ nhanh chóng với các cấu hình sẵn sàng cho nhiều loại phần cứng.

#### **Yêu Cầu Hệ Thống**
- **Docker** và **Docker Compose** đã được cài đặt.
- Phần cứng: CPU, GPU Nvidia, Mac/Apple Silicon, hoặc GPU AMD trên Linux.

#### **Các Bước Triển Khai Chi Tiết**

##### 1. **Clone Repository**
Mở terminal và chạy lệnh sau để tải bộ công cụ:
```bash
git clone https://github.com/n8n-io/self-hosted-ai-starter-kit.git
cd self-hosted-ai-starter-kit
```

##### 2. **Chọn Cấu Hình Phù Hợp Với Phần Cứng**
Tùy thuộc vào thiết bị của bạn, sử dụng một trong các lệnh sau:

- **Chỉ dùng CPU:**
  ```bash
  docker compose --profile cpu up
  ```

- **GPU Nvidia:**
  ```bash
  docker compose --profile gpu-nvidia up
  ```
  > **Lưu ý:** Đảm bảo driver Nvidia và CUDA đã được cài đặt. Xem thêm tại [Ollama Docker](https://github.com/ollama/ollama/blob/main/docs/docker.md).

- **Mac/Apple Silicon:**
  ```bash
  docker compose up
  ```
  > **Thêm:** Chỉnh sửa file `docker-compose.yml`, thêm `OLLAMA_HOST=host.docker.internal:11434`.

- **GPU AMD trên Linux:**
  ```bash
  docker compose --profile gpu-amd up
  ```

##### 3. **Kiểm Tra và Truy Cập**
- Mở trình duyệt, vào `http://localhost:5678/` để truy cập giao diện n8n.
- Cập nhật thông tin đăng nhập tại `http://localhost:5678/home/credentials`.
- Đảm bảo Ollama chạy tại `http://localhost:11434/` (kiểm tra bằng lệnh `curl http://localhost:11434/`).

##### 4. **Nâng Cấp (Tùy Chọn)**
Nếu cần cập nhật phiên bản mới:
```bash
docker compose --profile gpu-nvidia pull && docker compose create && docker compose --profile gpu-nvidia up
```

---

### 🤖 Xây Dựng Workflow Đơn Giản: AI Agent Trong Hành Động

Bây giờ, hãy cùng tạo một **workflow** minh họa cách AI agent hoạt động với n8n và mô hình **DeepSeek Distill 8b**. Workflow này sẽ nhận câu hỏi từ người dùng, phân tích ý định, thực hiện tool call (như tìm kiếm web), và trả về kết quả.

<img src="/images/11.Agent/11.2.sample agent/11.2.1.N8n/img.png"/>

---

#### 🏁 Bước 1: Truy Cập Không Gian Làm Việc n8n
Sau khi cài đặt và chạy thành công **n8n** thông qua Docker, bạn có thể truy cập giao diện làm việc bằng cách:

🔗 Mở trình duyệt và truy cập: `http://localhost:5678`

🆕 Nếu đây là lần đầu tiên, bạn cần tạo một tài khoản bằng cách nhập **email** và **mật khẩu**.

---

#### 🛠️ Bước 2: Tạo Quy Trình Làm Việc Mới
1️⃣ Trong không gian làm việc n8n, nhấn vào **Create a new workflow** để bắt đầu.

---

#### 💬 Bước 3: Thêm Nút "Chat"
1️⃣ Trong quy trình làm việc mới, nhấn **`+`** để thêm một **nút mới**.

2️⃣ Tìm kiếm và chọn **"Chat"**.

---

#### 🤖 Bước 4: (Tuỳ Chọn) Tạo Tác Nhân Mới
🔹 Trong phần **cấu hình của nút Chat**, bạn có thể tạo một **tác nhân mới (Agent)** nếu cần.

📌 *Lưu ý: Bước này là tùy chọn nhưng hữu ích nếu bạn muốn quản lý hội thoại AI chuyên sâu hơn.*

---

#### 📌 Bước 5: Chọn Mô Hình Chat Ollama
1️⃣ Trong phần cấu hình của **nút Chat**, tìm đến tuỳ chọn **chọn mô hình Chat**.

2️⃣ Chọn **Ollama Chat Model**.

---

#### 🔑 Bước 6: Tạo Thông Tin Đăng Nhập Ollama Mới
💡 Nếu bạn chưa có **thông tin đăng nhập Ollama**, hãy nhấn **"Create new credential" (Tạo thông tin đăng nhập mới)**.

---

#### ⚠️ Bước 7: Cấu Hình Thông Tin Đăng Nhập Ollama (QUAN TRỌNG)
📌 **Bước này rất quan trọng để kết nối n8n với Ollama chạy cục bộ.**

1️⃣ Trong cửa sổ cấu hình, tìm đến trường **"Base URL"**.

2️⃣ **Không sử dụng** `http://localhost:11434` (cổng mặc định của Ollama).

3️⃣ **Thay vào đó, nhập địa chỉ:**
   ```bash
   http://host.docker.internal:11434
   ```
4️⃣ Nhấn **"Save"** để lưu cấu hình.

5️⃣ Kiểm tra kết nối: Nếu thiết lập đúng, bạn sẽ thấy thông báo **"Connection test successfully"**.

🚨 *Nếu bạn không sử dụng đúng địa chỉ trên, n8n sẽ KHÔNG thể kết nối với Ollama!* 🚨

---

#### 🏷️ Bước 8: Chọn Mô Hình Ngôn Ngữ Lớn (LLM)
✅ Sau khi thiết lập thành công thông tin đăng nhập, bạn sẽ thấy danh sách **mô hình LLM** có sẵn.

🛠️ Chọn mô hình bạn muốn sử dụng, ví dụ:
   - `Llama 3.1`
   - `Gemma 2 2B`
   - `deepseek 1.5B`

---

#### 🗃️ Bước 9: (Tuỳ Chọn) Thêm Nút "Buffer Memory"
📝 Bạn có thể thêm **nút "Windows Buffer Memory"** vào workflow để quản lý hội thoại tốt hơn.

📌 *Bước này không bắt buộc nhưng có thể hữu ích cho các phiên làm việc dài.*

---

#### ✅ Bước 10: Kiểm Tra Quy Trình Làm Việc
🔄 Sau khi hoàn thành thiết lập, kiểm tra workflow bằng cách:

1️⃣ Nhấn vào nút **"Chat"** trong nút Chat.

2️⃣ Nhập một tin nhắn thử, ví dụ: `Hello, how are you?`

3️⃣ Nếu mọi thứ hoạt động chính xác, bạn sẽ nhận được phản hồi từ mô hình AI đã chọn.

🎉 Chúc mừng! Bạn đã thiết lập thành công n8n kết nối với Ollama để chạy mô hình AI cục bộ. 🚀


---

### 🎨 Những Chi Tiết Thú Vị và Mẹo Chuyên Nghiệp

Trong quá trình triển khai, có một số điểm đáng chú ý:
- **Hỗ trợ Tool Call:** Hiên Chỉ mô hình **32b** hoạt động tốt với tool calls. Các phiên bản khác không được hổ trợ native, nhưng cộng đồng đã tạo ra các bản tùy chỉnh như [deepseek-r1-tool-calling](https://ollama.com/MFDoom/deepseek-r1-tool-calling).
- **Tối Ưu Hóa:** Với GPU mạnh như RTX 4090, bạn có thể tăng độ dài ngữ cảnh lên 16K để xử lý các tác vụ phức tạp hơn.

#### **Mẹo Hay**
- Tham gia [cộng đồng n8n](https://community.n8n.io/t/ollama-and-toolagent/61232) để cập nhật các giải pháp mới.
- Kiểm tra log của Ollama nếu gặp lỗi: `docker logs <container-id>`.
