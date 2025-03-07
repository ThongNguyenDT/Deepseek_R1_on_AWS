---
title: "web chat"
date :  "`r Sys.Date()`" 
weight: 1
chapter: false
pre: " <b> 4.1. </b> "
---

## 🚀 Giới thiệu

Bạn muốn trải nghiệm **AI ngay trên máy tính cá nhân** mà không cần kết nối Internet? Hãy thử **Open WebUI**, một giao diện trực quan giúp bạn dễ dàng chạy mô hình **Deepseek** với **Ollama**. Trong hướng dẫn này, chúng ta sẽ thiết lập môi trường và triển khai Open WebUI chỉ trong vài bước đơn giản!

### 🔧 Công cụ cần có:
- **Ollama**: Quản lý và chạy các mô hình AI.
- **Deepseek**: Mô hình ngôn ngữ mạnh mẽ hỗ trợ nhiều tác vụ.
- **UV**: Trình quản lý runtime giúp thiết lập môi trường Python.
- **Open WebUI**: Giao diện dễ sử dụng để tương tác với AI.

![Open WEBUI](https://docs.openwebui.com/assets/images/demo-d3952c8561c4808c1d447fc061c71174.gif)

---
## 📌 Các Bước Cài Đặt

### 1️⃣ Cài đặt Ollama
Đầu tiên, chúng ta cần cài đặt **Ollama** để quản lý mô hình Deepseek:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```
🔹 **Kiểm tra phiên bản** sau khi cài đặt:
```bash
ollama --version
```

### 2️⃣ Tải xuống mô hình Deepseek
Chọn phiên bản phù hợp và tải xuống bằng lệnh:
```bash
ollama pull deepseek-r1:Xb
```
> 📌 *Lưu ý:* Thay `Xb` bằng phiên bản mô hình bạn muốn dùng.

### 3️⃣ Cài đặt UV
UV giúp quản lý môi trường Python hiệu quả hơn.

📌 **Trên macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
📌 **Trên Windows:**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 4️⃣ Tạo môi trường ảo với UV
Chúng ta cần một môi trường ảo để chạy Open WebUI.

📌 **Trên macOS/Linux:**
```bash
mkdir ~/Documents/openwebui && cd ~/Documents/openwebui && uv venv --python 3.11
```
📌 **Trên Windows:**
```powershell
mkdir ~/Documents/openwebui
cd ~/Documents/openwebui
uv venv --python 3.11
```
> 🔹 *Python 3.11 được khuyến nghị để đảm bảo hiệu suất tốt nhất!*

### 5️⃣ Cài đặt Open WebUI
Sau khi thiết lập môi trường ảo, chúng ta cài đặt Open WebUI:
```bash
cd ~/Documents/openwebui && uv pip install open-webui
```
📌 **Trên Windows:**
```powershell
cd ~/Documents/openwebui && uv pip install open-webui
```

### 6️⃣ Khởi động Open WebUI
Bây giờ, hãy khởi động Open WebUI và tương tác với mô hình AI của bạn!

📌 **Trên macOS/Linux:**
```bash
DATA_DIR=~/.open-webui uv run open-webui serve
```
📌 **Trên Windows:**
```powershell
$env:DATA_DIR="C:\open-webui\data"; uv run open-webui serve
```
> 🔹 *Thiết lập `DATA_DIR` giúp lưu trữ dữ liệu một cách lâu dài.*

### 7️⃣ Khắc phục lỗi timeout (nếu có)
Nếu gặp lỗi timeout khi chạy mô hình, hãy thử tăng thời gian chờ:

📌 **Trên macOS/Linux:**
```bash
AIOHTTP_CLIENT_TIMEOUT_OPENAI_MODEL_LIST=5 DATA_DIR=~/.open-webui uv run open-webui serve
```
📌 **Trên Windows:**
```powershell
$env:AIOHTTP_CLIENT_TIMEOUT_OPENAI_MODEL_LIST=5; $env:DATA_DIR="C:\open-webui\data"; uv run open-webui serve
```

### 8️⃣ Truy cập Open WebUI
Sau khi khởi động thành công, Open WebUI sẽ hiển thị địa chỉ truy cập:
```bash
http://localhost:8080
```
Mở trình duyệt và truy cập địa chỉ trên để trải nghiệm AI ngay lập tức! 🚀

---
#### 🔥 Lưu ý quan trọng khi sử dụng Open WebUI offline
✅ **Tải mô hình trước khi mất kết nối**: Đảm bảo bạn đã tải sẵn các mô hình AI cần thiết.\
✅ **Chạy Open WebUI mà không cần mạng**: Sau khi thiết lập xong, bạn có thể sử dụng Open WebUI hoàn toàn offline.\
✅ **Tích hợp API**: Open WebUI hỗ trợ API với các tùy chọn bảo mật như JWT và API key.
