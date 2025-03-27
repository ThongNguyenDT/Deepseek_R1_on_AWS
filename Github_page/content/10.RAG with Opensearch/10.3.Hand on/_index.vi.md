---
title: "Hand on"
date :  "`r Sys.Date()`" 
weight: 3
chapter: false
pre: " <b> 10.3. </b> "
---

**_Triển Khai DeepSeek-R1 Distill với Amazon OpenSearch Service và Amazon SageMaker cho Ứng Dụng RAG_**

Hướng dẫn này trình bày chi tiết cách triển khai **DeepSeek-R1 Distill** như một ứng dụng **Retrieval Augmented Generation (RAG)** bằng cách sử dụng **Amazon OpenSearch Service** kết hợp với **Amazon SageMaker**. Các script Python, công cụ CLI và cấu hình IAM được sử dụng để đảm bảo quá trình triển khai chỉnh chu, chuyên nghiệp và dễ hiểu, với thuật ngữ chuyên ngành được áp dụng chính xác.

---

### 1. Điều Kiện Tiên Quyết

- **Git:** Cần cài đặt Git để clone repository chứa mã nguồn mẫu:
  ```bash
  git clone https://github.com/Jon-AtAWS/opensearch-examples.git
  ```
- **Python:** Sử dụng Python 3.13. Tạo môi trường ảo để quản lý dependencies.
- **AWS Account:** Tài khoản AWS phải có quyền tạo domain OpenSearch Service và thiết lập endpoint SageMaker.
- **IDE:** Visual Studio Code hoặc IDE tương tự để phát triển và quản lý mã nguồn.
- **AWS CLI hoặc Boto3:** AWS CLI cần được cấu hình với thông tin đăng nhập hợp lệ.

---

### 2. Triển Khai DeepSeek trên Amazon SageMaker

- Triển khai mô hình **DeepSeek-R1** trên SageMaker để tạo endpoint inference.
- Tham khảo tài liệu “Deploying DeepSeek-R1 Distill Model on AWS using Amazon SageMaker AI” để biết chi tiết về cấu hình, yêu cầu và quy trình triển khai.

---

### 3. Tạo Domain Amazon OpenSearch Service

Một **OpenSearch Service domain** tương đương với một cụm OpenSearch. Các domain bao gồm các cài đặt, loại instance, số lượng instance và tài nguyên lưu trữ do bạn chỉ định. Bạn có thể tạo domain bằng console AWS, AWS CLI hoặc AWS SDKs.

#### Để tạo domain OpenSearch Service bằng console:

1. Truy cập https://aws.amazon.com và chọn **Sign In to the Console**.
2. Trong mục **Analytics**, chọn **Amazon OpenSearch Service**.
3. Nhấn **Create domain**.
4. Đặt tên cho domain (ví dụ: `movies` được sử dụng trong hướng dẫn này).
5. Chọn phương thức tạo domain là **Standard create**.
   - **Lưu ý:** Để nhanh chóng thiết lập domain sản xuất với best practices, bạn có thể chọn **Easy create**. Trong hướng dẫn này, chúng ta dùng **Standard create** cho mục đích phát triển và thử nghiệm.
6. Chọn template **Dev/test**.
7. Chọn tùy chọn triển khai **Domain with standby**.
8. Chọn phiên bản OpenSearch mới nhất trong mục **Version**.
9. Bỏ qua các phần **Data nodes**, **Warm and cold data storage**, **Dedicated master nodes**, **Snapshot configuration**, và **Custom endpoint** trong hướng dẫn này.
10. Để đơn giản, chọn domain với quyền truy cập công cộng: trong **Network**, chọn **Public access**.
11. Trong cài đặt **fine-grained access control**, giữ nguyên tùy chọn **Enable fine-grained access control**. Chọn **Create master user** và nhập tên người dùng cùng mật khẩu.
12. Bỏ qua các phần **SAML authentication** và **Amazon Cognito authentication**.
13. Trong **Access policy**, chọn **Only use fine-grained access control**. Trong hướng dẫn này, fine-grained access control sẽ xử lý xác thực thay vì chính sách truy cập domain.
14. Bỏ qua các cài đặt còn lại và nhấn **Create**. 
    - Thời gian khởi tạo domain thường từ 15–30 phút, nhưng có thể lâu hơn tùy cấu hình.
    - Sau khi domain khởi tạo xong, chọn domain để xem bảng cấu hình. Ghi lại **domain endpoint** trong **General information** (ví dụ: `https://search-my-domain.us-east-1.es.amazonaws.com`) để sử dụng ở bước sau.
- Sau khi tạo, lưu lại **Amazon Resource Name (ARN)** và **Endpoint URL** của domain để sử dụng trong các bước tiếp theo.

---

### 4. Tải Xuống và Chuẩn Bị Mã Nguồn

Thực hiện các bước sau trong môi trường cục bộ:

1. **Clone Repository và Di Chuyển Vào Thư Mục Dự Án:**
   ```bash
   cd opensearch-examples/opensearch-deepseek-rag
   ```

2. **Tạo Môi Trường Ảo và Cài Đặt Dependencies:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Thiết Lập Biến Môi Trường:**
   Cập nhật các biến sau với thông tin phù hợp:
   ```bash
   export DEEPSEEK_AWS_REGION='<vùng AWS của bạn>'
   export SAGEMAKER_MODEL_INFERENCE_ARN='<ARN endpoint SageMaker>'
   export SAGEMAKER_MODEL_INFERENCE_ENDPOINT='<URL endpoint SageMaker>'
   export OPENSEARCH_SERVICE_DOMAIN_ARN='<ARN domain OpenSearch>'
   export OPENSEARCH_SERVICE_DOMAIN_ENDPOINT='<API endpoint domain>'
   export OPENSEARCH_SERVICE_ADMIN_USER='<tên người dùng admin>'
   export OPENSEARCH_SERVICE_ADMIN_PASSWORD='<mật khẩu admin>'
   ```

Mã nguồn được tổ chức thành các script Python riêng biệt để dễ theo dõi và bảo trì.

---

### 5. Thiết Lập Quyền (IAM Roles)

#### 5.1. Vai Trò Cho Phép OpenSearch Gọi SageMaker Endpoint

- Kiểm tra file `create_invoke_role.py`.
- Chạy script:
  ```bash
  python create_invoke_role.py
  ```
- Lưu ARN vai trò và thiết lập biến môi trường `INVOKE_DEEPSEEK_ROLE` theo hướng dẫn từ script.

**Đoạn mã `create_invoke_role.py` dùng để:**
- Tạo chính sách và vai trò IAM cho phép OpenSearch Service gọi hành động `sagemaker:InvokeEndpoint` trên endpoint SageMaker.
- Vai trò được cấu hình để OpenSearch Service có thể assume, kết hợp với chính sách để gọi DeepSeek trên SageMaker.

#### 5.2. Vai Trò Cho Phép Người Dùng Tạo Connector Trong OpenSearch

- Kiểm tra file `create_connector_role.py`.
- Chạy script:
  ```bash
  python create_connector_role.py
  ```
- Lưu ARN vai trò và thiết lập biến môi trường `CREATE_DEEPSEEK_CONNECTOR_ROLE`.

**Đoạn mã `create_connector_role.py` dùng để:**
- Tạo chính sách và vai trò IAM cho phép người dùng thực hiện `iam:PassRole` và `es:ESHttpPost` trên domain OpenSearch.
- Vai trò cho phép người dùng hiện tại assume để tạo connector.

#### 5.3. Thiết Lập Bảo Mật cho OpenSearch Service

- Kiểm tra file `setup_opensearch_security.py`.
- Chạy script:
  ```bash
  python setup_opensearch_security.py
  ```
- Cài đặt plugin bảo mật để mapping vai trò IAM (`invoke_create_connector_role` và `LambdaInvokeOpenSearchMLCommonsRole`) với quyền `ml_full_access`.

**Đoạn mã `setup_opensearch_security.py` dùng để:**
- Cấu hình fine-grained access control trong OpenSearch để gán vai trò IAM vào `ml_full_access`, cho phép truy cập đầy đủ vào tính năng ML.

---

### 6. Tạo Connector

Connector định nghĩa kết nối từ OpenSearch đến endpoint inference trên SageMaker.

1. Xem file `create_connector.py`.
2. Chạy script:
   ```bash
   python create_connector.py
   ```
3. Lưu biến môi trường `DEEPSEEK_CONNECTOR_ID` từ đầu ra.

**Đoạn mã `create_connector.py` dùng để:**
- Tạo connector trong OpenSearch với cấu hình gọi endpoint SageMaker qua hành động `PREDICT`.
- Định nghĩa thông tin xác thực, tham số và xử lý phản hồi từ SageMaker.

---

### 7. Tạo Model OpenSearch

Tạo model ML trên OpenSearch bằng plugin `ml-commons`:

1. Xem file `create_deepseek_model.py`.
2. Chạy script:
   ```bash
   python create_deepseek_model.py
   ```
3. Lưu biến môi trường `DEEPSEEK_MODEL_ID` từ đầu ra.

**Đoạn mã `create_deepseek_model.py` dùng để:**
- Đăng ký và triển khai model trong OpenSearch với connector đã tạo, dùng để liên kết với SageMaker trong pipeline.

---

### 8. Xác Minh Thiết Lập

Kiểm tra kết nối và hoạt động của mô hình:

1. Đăng nhập vào **OpenSearch Dashboards** qua URL từ console OpenSearch Service, sử dụng thông tin admin.
2. Trong **Dev Tools**, chạy lệnh:
   ```json
   POST _plugins/_ml/models/<your model ID>/_predict
   {
     "parameters": {
       "inputs": "Hello"
     }
   }
   ```
3. Kết quả trả về xác nhận mô hình hoạt động đúng với phản hồi từ DeepSeek.

---

### 9. Thiết Lập Quy Trình RAG

- **RAG:** Bổ sung thông tin từ cơ sở tri thức vào prompt để tăng độ chính xác của LLM.
- **Search Pipelines:** Chuỗi processor trong OpenSearch hỗ trợ tìm kiếm hybrid, reranking và RAG.
- Sử dụng dữ liệu vector trên OpenSearch với truy vấn k-NN để lấy thông tin ngữ nghĩa.

---

### 10. Kết Nối Với Mô Hình Embedding và Tải Dữ Liệu

1. **Cấu Hình Domain:**
   - Đảm bảo OpenSearch phiên bản 2.9+ với fine-grained access control.
   - Trong console, vào **Integrations**, chọn **Configure domain** dưới mục embedding models, nhập endpoint OpenSearch.

2. **Triển Khai Mô Hình Embedding:**
   - Sử dụng mô hình **all-MiniLM-L6-v2** trên SageMaker.
   - Sau khi CloudFormation triển khai xong, lấy **ModelID** từ tab **Outputs**.

3. **Tải Dữ Liệu:**
   ```bash
   export EMBEDDING_MODEL_ID='<Model ID từ CloudFormation>'
   python load_data.py
   ```
   - Script tạo index `population_data` với trường `text_embedding` cho tìm kiếm k-NN.

**Đoạn mã `load_data.py` dùng để:**
- Tạo index với cài đặt k-NN, sử dụng trường `knn_vector` (chiều 384) và thuật toán HNSW.

---

### 11. Chạy Truy Vấn RAG

1. Xem file `run_rag.py`.
2. Chạy script:
   ```bash
   python run_rag.py
   ```
   - Tạo search pipeline với processor `retrieval_augmented_generation` để gọi DeepSeek qua SageMaker.
3. Kết quả bao gồm tài liệu truy xuất và phản hồi từ DeepSeek.

**Đoạn mã `run_rag.py` dùng để:**
- Thiết lập pipeline RAG, dùng embedding model để truy vấn k-NN và DeepSeek để sinh câu trả lời.

---

### 12. Dọn Dẹp Tài Nguyên

- Xóa endpoint SageMaker, stack CloudFormation và domain OpenSearch để tránh chi phí.
