---
title: "Use Deepseek as RAG?"
date :  "`r Sys.Date()`" 
weight: 2
chapter: false
pre: " <b> 10.2. </b> "
---

**_Hướng Dẫn Chi Tiết Triển Khai RAG cho Mô Hình DeepSeek Distill_**

Retrieval-Augmented Generation (RAG) là một kỹ thuật mạnh mẽ kết hợp giữa truy xuất thông tin và tạo văn bản, giúp các mô hình ngôn ngữ lớn (LLM) như DeepSeek-R1 cung cấp câu trả lời chính xác, cập nhật dựa trên cơ sở kiến thức bên ngoài. Trong hướng dẫn này, chúng ta sẽ triển khai RAG cho mô hình DeepSeek distill một cách chi tiết, chỉnh chu, chuyên nghiệp và sinh động, dựa trên bài viết từ DataCamp. Hướng dẫn bao gồm các bước cụ thể, công dụng của từng công cụ/phần mềm, và chú thích code rõ ràng để bạn có thể thực hiện dễ dàng.

---

## Tổng Quan về RAG và DeepSeek-R1

- **RAG (Retrieval-Augmented Generation)**: Kỹ thuật này cho phép mô hình ngôn ngữ truy xuất thông tin từ cơ sở kiến thức (ví dụ: tài liệu PDF, văn bản) và kết hợp thông tin đó để tạo câu trả lời. Điều này đặc biệt hữu ích khi bạn cần trả lời câu hỏi dựa trên dữ liệu không có trong quá trình huấn luyện của mô hình.
- **DeepSeek-R1**: Một mô hình ngôn ngữ lớn do DeepSeek AI (Trung Quốc) phát triển, nổi bật với khả năng suy luận logic, giải toán, và ra quyết định thời gian thực. Nó cũng có thể hiển thị quá trình suy luận, giúp người dùng kiểm tra logic của câu trả lời.

Mục tiêu của chúng ta là xây dựng một chatbot RAG sử dụng DeepSeek-R1, chạy cục bộ, với giao diện web thân thiện.

---

## Công Cụ và Phần Mềm Cần Thiết

Dưới đây là danh sách các công cụ/phần mềm được sử dụng, kèm theo công dụng cụ thể:

1. **Ollama**  
   - **Công dụng**: Chạy các mô hình ngôn ngữ lớn (như DeepSeek-R1) cục bộ trên máy tính. Không cần kết nối internet sau khi tải mô hình, đảm bảo quyền riêng tư và tốc độ xử lý.
   - **Vai trò**: Tải và gọi mô hình DeepSeek-R1 để tạo câu trả lời.

2. **LangChain**  
   - **Công dụng**: Khuôn khổ mã nguồn mở để xây dựng ứng dụng với LLM, hỗ trợ kết nối mô hình với dữ liệu bên ngoài (cơ sở kiến thức) và quản lý quy trình truy xuất/tạo văn bản.
   - **Vai trò**: Tích hợp RAG bằng cách xử lý văn bản, tạo embedding, và kết nối với cơ sở dữ liệu vector.

3. **Chroma**  
   - **Công dụng**: Cơ sở dữ liệu vector để lưu trữ và truy xuất nhanh các vectơ embedding (biểu diễn số của văn bản).  
   - **Vai trò**: Lưu trữ embedding của cơ sở kiến thức và tìm kiếm các đoạn văn bản liên quan đến câu hỏi.

4. **Gradio**  
   - **Công dụng**: Thư viện Python tạo giao diện web tương tác cho ứng dụng máy học.  
   - **Vai trò**: Xây dựng giao diện người dùng để người dùng nhập câu hỏi và nhận câu trả lời từ chatbot.

5. **PyMuPDF**  
   - **Công dụng**: Thư viện Python xử lý tệp PDF, trích xuất văn bản từ tài liệu.  
   - **Vai trò**: Tải cơ sở kiến thức từ tệp PDF để sử dụng trong RAG.

6. **RecursiveCharacterTextSplitter**  
   - **Công dụng**: Công cụ từ LangChain để chia văn bản dài thành các đoạn nhỏ (chunks) có kích thước quản lý được.  
   - **Vai trò**: Chuẩn bị dữ liệu bằng cách chia cơ sở kiến thức thành các đoạn phù hợp để tạo embedding.

7. **OllamaEmbeddings**  
   - **Công dụng**: Lớp từ LangChain để tạo embedding từ văn bản bằng mô hình Ollama (như DeepSeek-R1).  
   - **Vai trò**: Chuyển các đoạn văn bản thành vectơ số để lưu trữ và so sánh.

8. **Chroma Client**  
   - **Công dụng**: Công cụ giao tiếp với cơ sở dữ liệu Chroma.  
   - **Vai trò**: Quản lý việc lưu trữ và truy xuất embedding trong Chroma.

---

## Hướng Dẫn Triển Khai Từng Bước

### Bước 1: Cài Đặt Môi Trường

Đầu tiên, bạn cần cài đặt Python (phiên bản 3.8 trở lên). Sau đó, cài đặt các thư viện cần thiết bằng lệnh sau trong terminal:

```bash
pip install ollama langchain gradio pymupdf chromadb
```

- **Chú thích**: Lệnh này cài đặt tất cả các công cụ/phần mềm cần thiết để triển khai RAG.

---

### Bước 2: Tải Mô Hình DeepSeek-R1

Sử dụng Ollama để tải mô hình DeepSeek-R1. Tùy vào tài nguyên máy tính, bạn có thể chọn phiên bản phù hợp (ví dụ: 7B):

```bash
ollama pull deepseek-r1:7b
```

- **Chú thích**: 
  - `deepseek-r1:7b` là phiên bản 7 tỷ tham số, cân bằng giữa hiệu suất và yêu cầu phần cứng.
  - Sau khi tải, mô hình được lưu cục bộ và sẵn sàng sử dụng.

---

### Bước 3: Chuẩn Bị Cơ Sở Kiến Thức

Ở đây, chúng ta sử dụng một tệp PDF làm cơ sở kiến thức. Bạn có thể thay bằng nguồn dữ liệu khác (ví dụ: văn bản thô, tài liệu Word).

Sử dụng PyMuPDF để trích xuất văn bản:

```python
from langchain_community.document_loaders import PyMuPDFLoader

# Thay "path/to/your/pdf.pdf" bằng đường dẫn đến tệp PDF của bạn
loader = PyMuPDFLoader("path/to/your/pdf.pdf")
documents = loader.load()
```

- **Chú thích**: 
  - `PyMuPDFLoader` đọc tệp PDF và trả về danh sách các trang dưới dạng đối tượng tài liệu.
  - Đảm bảo đường dẫn tệp PDF chính xác.

---

### Bước 4: Chia Văn Bản Thành Các Đoạn Nhỏ

Sử dụng RecursiveCharacterTextSplitter để chia văn bản thành các đoạn có kích thước hợp lý:

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = text_splitter.split_documents(documents)
```

- **Chú thích**: 
  - `chunk_size=1000`: Mỗi đoạn tối đa 1000 ký tự.
  - `chunk_overlap=200`: 200 ký tự chồng lấp giữa các đoạn để giữ ngữ cảnh.
  - Kết quả là danh sách các đoạn văn bản nhỏ (chunks).

---

### Bước 5: Tạo Embedding cho Các Đoạn Văn Bản

Sử dụng OllamaEmbeddings để chuyển các đoạn văn bản thành vectơ số:

```python
from langchain_community.embeddings import OllamaEmbeddings

embeddings = OllamaEmbeddings(model="deepseek-r1:7b")
```

- **Chú thích**: 
  - Embedding là biểu diễn số của văn bản, giúp so sánh độ tương đồng giữa câu hỏi và cơ sở kiến thức.
  - Mô hình DeepSeek-R1 được sử dụng để tạo embedding.

---

### Bước 6: Lưu Trữ Embedding trong Chroma

Lưu các embedding vào cơ sở dữ liệu vector Chroma:

```python
from langchain.vectorstores import Chroma

vectorstore = Chroma.from_documents(documents=chunks, embedding=embeddings)
```

- **Chú thích**: 
  - `Chroma.from_documents` tạo cơ sở dữ liệu vector từ các đoạn văn bản và embedding.
  - `vectorstore` sẽ được sử dụng để truy xuất thông tin sau này.

---

### Bước 7: Xây Dựng Hàm Truy Xuất và Tạo Văn Bản

Tạo hàm để truy xuất thông tin liên quan và sử dụng DeepSeek-R1 để trả lời câu hỏi:

```python
import ollama

def ask_question(question):
    # Truy xuất 3 đoạn văn bản liên quan nhất
    retrieved_chunks = vectorstore.similarity_search(question, k=3)
    context = " ".join([chunk.page_content for chunk in retrieved_chunks])

    # Tạo prompt cho DeepSeek-R1
    prompt = f"Dựa trên thông tin sau: {context}\n\nTrả lời câu hỏi: {question}"

    # Gọi DeepSeek-R1 để tạo câu trả lời
    response = ollama.chat(model="deepseek-r1:7b", messages=[{"role": "user", "content": prompt}])

    return response["message"]["content"]
```

- **Chú thích**: 
  - `similarity_search`: Tìm các đoạn văn bản giống nhất với câu hỏi dựa trên embedding.
  - `context`: Gộp các đoạn truy xuất được thành một chuỗi văn bản.
  - `ollama.chat`: Gọi DeepSeek-R1 để tạo câu trả lời dựa trên prompt.

---

### Bước 8: Xây Dựng Giao Diện Người Dùng với Gradio

Sử dụng Gradio để tạo giao diện web cho chatbot:

```python
import gradio as gr

def chatbot(question):
    return ask_question(question)

interface = gr.Interface(fn=chatbot, inputs="text", outputs="text", title="DeepSeek-R1 RAG Chatbot")
interface.launch()
```

- **Chú thích**: 
  - `gr.Interface`: Tạo giao diện với ô nhập câu hỏi và ô hiển thị câu trả lời.
  - `interface.launch()`: Khởi chạy ứng dụng web trên trình duyệt.

---

## Chạy Toàn Bộ Ứng Dụng

Gộp tất cả code lại thành một tệp Python (ví dụ: `rag_chatbot.py`) và chạy:

```bash
python rag_chatbot.py
```

Một cửa sổ trình duyệt sẽ mở ra, cho phép bạn nhập câu hỏi và nhận câu trả lời từ chatbot RAG dựa trên cơ sở kiến thức.

