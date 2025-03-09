---
title: "mobile app"
date :  "`r Sys.Date()`" 
weight: 2
chapter: false
pre: " <b> 4.2. </b> "
---
## Introduction to SwiftChat

[SwiftChat](https://github.com/aws-samples/swift-chat) is a cross-platform AI chat application developed using React Native, supporting multiple AI models, including **DeepSeek**. This application provides a smooth real-time chat experience, supports multimedia (images, videos, documents), and operates on Android, iOS, and macOS.

### Key Features

#### 1. Support for Multiple AI Models
SwiftChat allows easy switching between various AI models, with DeepSeek being one of the primary models. Since version v1.10.0, the application has supported multiple AI models, providing maximum flexibility for users.

#### 2. Real-Time Chat
SwiftChat delivers fast and seamless chat capabilities, optimizing user interaction with AI.

<div style="display: flex; flex-direction: 'row'; background-color: #888888;">
<img src="https://raw.githubusercontent.com/aws-samples/swift-chat/refs/heads/main/assets/avif/text_streaming.avif" width=24%>
<img src="https://raw.githubusercontent.com/aws-samples/swift-chat/refs/heads/main/assets/avif/image_summary.avif" width=24%>
<img src="https://raw.githubusercontent.com/aws-samples/swift-chat/refs/heads/main/assets/avif/doc_summary.avif" width=24%>
<img src="https://raw.githubusercontent.com/aws-samples/swift-chat/refs/heads/main/assets/avif/video_summary.avif" width=24%>
</div>

#### 3. Markdown Support
The application supports Markdown formatting, ensuring clear and readable text display.

![image](https://raw.githubusercontent.com/aws-samples/swift-chat/refs/heads/main/assets/markdown.png)

#### 4. Customizable Interface
A minimalist and user-friendly interface that can be customized to suit personal preferences, enhancing user experience.

#### 5. Cross-Platform Compatibility
SwiftChat operates smoothly on multiple platforms, including Android, iOS, and macOS, ensuring convenience for users.

#### 6. System Prompt Assistant
Allows users to customize System Prompts to optimize AI responses based on personal needs.

<div style="display: flex; flex-direction: 'row'; background-color: #888888;">
<img src="https://raw.githubusercontent.com/aws-samples/swift-chat/refs/heads/main/assets/avif/prompt_translate.avif" width=24%>
<img src="https://raw.githubusercontent.com/aws-samples/swift-chat/refs/heads/main/assets/avif/prompt_code.avif" width=24%>
<img src="https://raw.githubusercontent.com/aws-samples/swift-chat/refs/heads/main/assets/avif/prompt_add_chef.avif" width=24%>
<img src="https://raw.githubusercontent.com/aws-samples/swift-chat/refs/heads/main/assets/avif/prompt_edit.avif" width=24%>
</div>

#### 7. Additional Features
- **Multimedia Support**: Handles images, videos, and documents.
- **Conversation History Management**: Easily review and retrieve past conversations.
- **Optimized for Tablets**: Displays a UI suitable for larger screens.
- **Fast Startup and High Performance**: Enhances response time.
- **AI Image Generation**: Supports AI-powered image creation.
- **Privacy Protection**: Ensures maximum user data security.

<div style="display: flex; flex-direction: 'row'; background-color: #888888;">
<img src="https://raw.githubusercontent.com/aws-samples/swift-chat/refs/heads/main/assets/avif/copy_code.avif" width=32%>
<img src="https://raw.githubusercontent.com/aws-samples/swift-chat/refs/heads/main/assets/avif/select_mode.avif" width=32%>
<img src="https://raw.githubusercontent.com/aws-samples/swift-chat/refs/heads/main/assets/avif/scroll_token.avif" width=32%>
</div>

![image](https://raw.githubusercontent.com/aws-samples/swift-chat/refs/heads/main/assets/history_settings.png)

---

## Guide to Deploying SwiftChat with DeepSeek-R1 distill

### Step 1: Deploy the DeepSeek-R1 distill Model Using Ollama

#### 1. Install Ollama
Download and install Ollama from the official website.

#### 2. Download and Run DeepSeek-R1
Open a terminal and run the following command to download and start the DeepSeek-R1 model:

```
ollama serve
```

This command makes the model ready for integration with other applications.

---

### Step 2: Connect SwiftChat to the Ollama Server

#### 1. Download the SwiftChat Application
- **Android**: [Download](https://github.com/aws-samples/swift-chat/releases/download/1.10.0/SwiftChat.apk)
- **macOS**: [Download](https://github.com/aws-samples/swift-chat/releases/download/1.10.0/SwiftChat.dmg)
- **iOS**: Requires manual build using Xcode.

#### 2. Configure the Connection
1. Open the SwiftChat application.
2. Access **Settings** from the main menu.
3. Navigate to the **Ollama** tab and enter the following details:
   - **Server URL**: `http://localhost:11434`
   - **Select AI Model**: DeepSeek-R1 from the "Text Model" list.

4. Save the settings by tapping the ✓ icon.
5. Start chatting with AI.

#### Notes:
- Ensure the Ollama server is running on your device.
- If the server runs on another machine, replace `localhost` with the server's IP address.

By following these steps, you can successfully deploy and use DeepSeek-R1 distill on your mobile device through the SwiftChat application, enjoying a smooth and convenient AI chat experience.

