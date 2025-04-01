---
title: "Function Calling"
date :  "`r Sys.Date()`" 
weight: 2
chapter: false
pre: " 2. "
---


**_Triển Khai Function Calling Cho Deepseek R1 Distill 8B Agent Với Python và Ollama_**

### Function Calling Là Gì?

#### Khái Niệm Cơ Bản

**Function calling** (hay còn gọi là **tool calling**) là một tính năng cho phép mô hình ngôn ngữ gọi các hàm bên ngoài để thực hiện các tác vụ cụ thể. Thay vì chỉ trả lời bằng văn bản, mô hình có thể:
- Thực hiện phép tính (ví dụ: cộng, trừ).
- Truy xuất dữ liệu từ cơ sở dữ liệu.
- Gọi các dịch vụ hoặc ứng dụng khác.

Với Deepseek R1 Distill 8B, function calling biến mô hình thành một **agent thông minh**, có khả năng xử lý các yêu cầu phức tạp hơn.

#### Cách Hoạt Động

1. **Định nghĩa hàm:** Bạn viết các hàm Python mà mô hình có thể sử dụng.
2. **Cấu hình công cụ:** Đăng ký các hàm này dưới dạng "công cụ" (tools) trong Ollama.
3. **Gửi yêu cầu:** Khi người dùng đặt câu hỏi, mô hình xác định xem có cần gọi hàm nào không.
4. **Thực thi và trả kết quả:** Mô hình gọi hàm, lấy kết quả và trả lời người dùng.

Ví dụ: Nếu bạn hỏi "Tổng của 5 và 7 là bao nhiêu?", mô hình sẽ gọi hàm `add_numbers(5, 7)` và trả về kết quả `12`.

---

### Cấu Hình Function Calling Bằng Python

Bây giờ, chúng ta sẽ đi sâu vào cách cấu hình function calling bằng Python và Ollama. Hãy làm theo từng bước dưới đây.

#### Bước 1: Cài Đặt Thư Viện Ollama

Đầu tiên, cài đặt thư viện Python của Ollama:
```bash
pip install ollama
```

#### Bước 2: Định Nghĩa Hàm Python

Tạo một hàm đơn giản, ví dụ hàm tính tổng hai số:
```python
def add_numbers(a: int, b: int) -> int:
    """Trả về tổng của hai số a và b."""
    return a + b
```

#### Bước 3: Định Nghĩa Công Cụ (Tool)

Ollama yêu cầu mô tả hàm dưới dạng JSON để đăng ký nó như một công cụ. Dưới đây là cách định nghĩa công cụ cho `add_numbers`:
```python
tool = {
    "name": "add_numbers",
    "description": "Tính tổng của hai số nguyên",
    "parameters": {
        "type": "object",
        "properties": {
            "a": {"type": "integer", "description": "Số thứ nhất"},
            "b": {"type": "integer", "description": "Số thứ hai"}
        },
        "required": ["a", "b"]
    }
}
```

- **`name`:** Tên hàm (phải khớp với hàm Python).
- **`description`:** Mô tả chức năng của hàm.
- **`parameters`:** Thông tin về các tham số mà hàm yêu cầu.

#### Bước 4: Tích Hợp Với Mô Hình

Sử dụng thư viện Ollama để gửi yêu cầu đến mô hình, kèm theo công cụ:
```python
import ollama

# Danh sách công cụ
tools = [tool]

# Gửi yêu cầu
response = ollama.chat(
    model="MFDoom/deepseek-r1-tool-calling",
    messages=[{"role": "user", "content": "Hãy tính tổng của 5 và 7"}],
    tools=tools
)

# Xử lý phản hồi
if "tool_calls" in response["message"]:
    for tool_call in response["message"]["tool_calls"]:
        if tool_call["name"] == "add_numbers":
            a = tool_call["arguments"]["a"]
            b = tool_call["arguments"]["b"]
            result = add_numbers(a, b)
            print(f"Kết quả: {result}")
else:
    print(response["message"]["content"])
```

###### Giải Thích
- **`ollama.chat`:** Gửi yêu cầu đến mô hình với thông tin công cụ trong tham số `tools`.
- **`tool_calls`:** Nếu mô hình quyết định gọi hàm, phản hồi sẽ chứa thông tin về hàm được gọi và các tham số.
- **Thực thi hàm:** Trích xuất tham số từ `tool_call["arguments"]`, gọi hàm và in kết quả.

---

### Ví Dụ Minh Họa

Dưới đây là mã hoàn chỉnh để tạo một trợ lý tính tổng hai số bất kỳ:

```python
import ollama

# Định nghĩa hàm
def add_numbers(a: int, b: int) -> int:
    """Trả về tổng của hai số a và b."""
    return a + b

# Định nghĩa công cụ
tool = {
    "name": "add_numbers",
    "description": "Tính tổng của hai số nguyên",
    "parameters": {
        "type": "object",
        "properties": {
            "a": {"type": "integer", "description": "Số thứ nhất"},
            "b": {"type": "integer", "description": "Số thứ hai"}
        },
        "required": ["a", "b"]
    }
}

# Danh sách công cụ
tools = [tool]

# Gửi yêu cầu
response = ollama.chat(
    model="MFDoom/deepseek-r1-tool-calling",
    messages=[{"role": "user", "content": "Hãy tính tổng của 5 và 7"}],
    tools=tools
)

# Xử lý phản hồi
if "tool_calls" in response["message"]:
    for tool_call in response["message"]["tool_calls"]:
        if tool_call["name"] == "add_numbers":
            a = tool_call["arguments"]["a"]
            b = tool_call["arguments"]["b"]
            result = add_numbers(a, b)
            print(f"Kết quả: {result}")
else:
    print(response["message"]["content"])
```

#### Kết Quả
Khi chạy, bạn sẽ thấy:
```
Kết quả: 12
```

---

### Lưu Ý Quan Trọng

- **Phần cứng:** Mô hình 8B yêu cầu máy tính mạnh (16GB RAM, GPU 16GB VRAM). Nếu không đủ, thử phiên bản nhỏ hơn như 7B hoặc 1.5B.
- **Kiểm tra hàm:** Đảm bảo hàm của bạn xử lý lỗi tốt để tránh crash.
- **Cập nhật Ollama:** Sử dụng phiên bản mới nhất để có hiệu suất và tính năng tốt nhất.
- **Thử nghiệm:** Thêm nhiều công cụ khác (ví dụ: tìm kiếm, tra cứu thời tiết) để khám phá thêm khả năng của mô hình.
