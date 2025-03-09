---
title: "mobile app"
date :  "`r Sys.Date()`" 
weight: 2
chapter: false
pre: " <b> 4.2. </b> "
---

## Giới thiệu về SwiftChat

[SwiftChat](https://github.com/aws-samples/swift-chat) là một ứng dụng chat AI đa nền tảng, được phát triển bằng React Native, hỗ trợ nhiều mô hình AI, bao gồm **DeepSeek**. Ứng dụng này mang lại trải nghiệm trò chuyện real-time mượt mà, hỗ trợ đa phương tiện (hình ảnh, video, tài liệu) và hoạt động trên cả Android, iOS và macOS.

### Tính năng nổi bật

#### 1. Hỗ trợ nhiều mô hình AI
SwiftChat cho phép dễ dàng chuyển đổi giữa các mô hình AI, với DeepSeek là một trong những mô hình chính. Từ phiên bản v1.10.0, ứng dụng đã hỗ trợ nhiều mô hình AI khác nhau, mang lại sự linh hoạt tối đa cho người dùng.

#### 2. Trò chuyện real-time
SwiftChat cung cấp khả năng chat nhanh chóng và mượt mà, giúp tối ưu hóa trải nghiệm người dùng khi tương tác với AI.

<div style="display: flex; flex-direction: 'row'; background-color: #888888;">
<img src="https://raw.githubusercontent.com/aws-samples/swift-chat/refs/heads/main/assets/avif/text_streaming.avif" width=24%>
<img src="https://raw.githubusercontent.com/aws-samples/swift-chat/refs/heads/main/assets/avif/image_summary.avif" width=24%>
<img src="https://raw.githubusercontent.com/aws-samples/swift-chat/refs/heads/main/assets/avif/doc_summary.avif" width=24%>
<img src="https://raw.githubusercontent.com/aws-samples/swift-chat/refs/heads/main/assets/avif/video_summary.avif" width=24%>
</div>

#### 3. Hỗ trợ Markdown
Ứng dụng hỗ trợ định dạng Markdown, giúp hiển thị văn bản rõ ràng và dễ đọc hơn.

![image](https://raw.githubusercontent.com/aws-samples/swift-chat/refs/heads/main/assets/markdown.png)

#### 4. Giao diện tùy chỉnh
Giao diện tối giản, dễ sử dụng và có thể tùy chỉnh theo sở thích cá nhân, giúp nâng cao trải nghiệm người dùng.

#### 5. Khả năng tương thích đa nền tảng
SwiftChat có thể hoạt động ổn định trên nhiều nền tảng, bao gồm Android, iOS và macOS, mang lại sự tiện lợi cho người dùng.

#### 6. System Prompt Assistant
Cho phép người dùng tùy chỉnh System Prompt để tối ưu hóa phản hồi của AI theo mục đích sử dụng cá nhân.

<div style="display: flex; flex-direction: 'row'; background-color: #888888;">
<img src="https://raw.githubusercontent.com/aws-samples/swift-chat/refs/heads/main/assets/avif/prompt_translate.avif" width=24%>
<img src="https://raw.githubusercontent.com/aws-samples/swift-chat/refs/heads/main/assets/avif/prompt_code.avif" width=24%>
<img src="https://raw.githubusercontent.com/aws-samples/swift-chat/refs/heads/main/assets/avif/prompt_add_chef.avif" width=24%>
<img src="https://raw.githubusercontent.com/aws-samples/swift-chat/refs/heads/main/assets/avif/prompt_edit.avif" width=24%>
</div>

#### 7. Các tính năng khác
- **Hỗ trợ đa phương tiện**: Xử lý hình ảnh, video và tài liệu.
- **Quản lý lịch sử hội thoại**: Dễ dàng xem lại và truy xuất các cuộc trò chuyện trước đó.
- **Tối ưu hóa cho tablet**: Hiển thị giao diện phù hợp với màn hình lớn.
- **Khởi động nhanh và hiệu suất cao**: Giúp tối ưu thời gian phản hồi.
- **Tạo ảnh AI**: Hỗ trợ tạo hình ảnh từ mô hình AI.
- **Bảo vệ quyền riêng tư**: Đảm bảo dữ liệu người dùng được bảo mật tối đa.

<div style="display: flex; flex-direction: 'row'; background-color: #888888;">
<img src="https://raw.githubusercontent.com/aws-samples/swift-chat/refs/heads/main/assets/avif/copy_code.avif" width=32%>
<img src="https://raw.githubusercontent.com/aws-samples/swift-chat/refs/heads/main/assets/avif/select_mode.avif" width=32%>
<img src="https://raw.githubusercontent.com/aws-samples/swift-chat/refs/heads/main/assets/avif/scroll_token.avif" width=32%>
</div>

![image](https://raw.githubusercontent.com/aws-samples/swift-chat/refs/heads/main/assets/history_settings.png)

---

## Hướng dẫn triển khai SwiftChat với DeepSeek-R1 distill

### Bước 1: Deploy mô hình DeepSeek-R1 distill bằng Ollama

#### 1. Cài đặt Ollama
Tải và cài đặt Ollama từ trang web chính thức.

#### 2. Tải và chạy DeepSeek-R1
Mở terminal và chạy lệnh sau để tải và khởi động mô hình DeepSeek-R1:

```
ollama serve
```

Lệnh này giúp mô hình sẵn sàng để tích hợp với các ứng dụng khác.

---

### Bước 2: Kết nối SwiftChat với server Ollama

#### 1. Tải ứng dụng SwiftChat
- **Android**: [Tải xuống](https://github.com/aws-samples/swift-chat/releases/download/1.10.0/SwiftChat.apk)
- **macOS**: [Tải xuống](https://github.com/aws-samples/swift-chat/releases/download/1.10.0/SwiftChat.dmg)
- **iOS**: Yêu cầu tự build bằng Xcode.

#### 2. Cấu hình kết nối
1. Mở ứng dụng SwiftChat.
2. Truy cập **Settings** từ menu chính.
3. Tìm tab **Ollama** và nhập thông tin:
   - **URL Server**: `http://localhost:11434`
   - **Chọn mô hình AI**: DeepSeek-R1 từ danh sách "Text Model".

4. Lưu cài đặt bằng cách nhấn vào biểu tượng ✓.
5. Bắt đầu trò chuyện với AI.

#### Lưu ý:
- Đảm bảo server Ollama đang chạy trên thiết bị của bạn.
- Nếu server chạy trên một máy khác, thay `localhost` bằng địa chỉ IP của máy chủ.

Với các bước trên, bạn đã có thể triển khai và sử dụng DeepSeek-R1 distill trên thiết bị di động thông qua ứng dụng SwiftChat, tận hưởng một trải nghiệm chat AI mượt mà và tiện lợi.

