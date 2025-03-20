---
title: "Hand on"
date :  "`r Sys.Date()`" 
weight: 2
chapter: false
pre: " <b> 8.2. </b> "
---
Hướng dẫn Triển khai Mô hình DeepSeek-R1 trên AWS SageMaker

Mô hình DeepSeek-R1 hiện đã có sẵn trên Amazon SageMaker JumpStart, giúp bạn dễ dàng triển khai và tích hợp vào ứng dụng của mình. Dưới đây là hướng dẫn chi tiết các bước triển khai mô hình DeepSeek-R1 trên AWS SageMaker, cùng với các lưu ý về cách tính chi phí.

### Triển khai DeepSeek-R1 thông qua SageMaker JumpStart

Bạn có thể triển khai mô hình DeepSeek-R1 thông qua giao diện người dùng của SageMaker JumpStart hoặc sử dụng SageMaker Python SDK.

#### Triển khai bằng Giao diện Người dùng SageMaker JumpStart

1. **Truy cập SageMaker Studio**: Mở AWS Management Console, điều hướng đến **SageMaker**, sau đó chọn **Studio**. Nếu đây là lần đầu bạn sử dụng, bạn sẽ được yêu cầu tạo một miền (domain).

2. **Mở JumpStart**: Trong SageMaker Studio, chọn **JumpStart** từ thanh điều hướng bên trái. Giao diện JumpStart sẽ hiển thị các mô hình có sẵn cùng với chi tiết như nhà cung cấp và khả năng của mô hình.

   ![Giao diện SageMaker JumpStart](https://docs.aws.amazon.com/sagemaker/latest/dg/images/studio-jumpstart.png)

3. **Tìm kiếm DeepSeek-R1**: Sử dụng thanh tìm kiếm để tìm **DeepSeek-R1** và xem thẻ mô hình tương ứng.

4. **Xem chi tiết mô hình**: Nhấp vào thẻ mô hình để xem trang chi tiết, bao gồm:
   - Tên mô hình
   - Nhà cung cấp
   - Danh mục tác vụ (ví dụ: Text Generation)
   - Huy hiệu **Bedrock Ready** (nếu có), cho biết mô hình có thể được đăng ký với Amazon Bedrock.

5. **Triển khai mô hình**: Nhấp vào **Deploy** để bắt đầu quá trình triển khai.

6. **Cấu hình triển khai**:
   - **Endpoint name**: Sử dụng tên mặc định hoặc tạo tên tùy chỉnh.
   - **Instance type**: Chọn loại instance phù hợp (mặc định: `ml.p5e.48xlarge`).
   - **Initial instance count**: Nhập số lượng instance (mặc định: 1).

     > **Lưu ý**: Việc chọn loại instance và số lượng phù hợp rất quan trọng để tối ưu hóa chi phí và hiệu suất.

7. **Xác nhận và triển khai**: Xem lại cấu hình và nhấp vào **Deploy**. Quá trình triển khai có thể mất vài phút. Khi hoàn tất, trạng thái endpoint sẽ chuyển thành **InService**, sẵn sàng chấp nhận các yêu cầu suy luận.

#### Triển khai bằng SageMaker Python SDK

1. **Cài đặt SageMaker Python SDK**: Đảm bảo bạn đã cài đặt SageMaker Python SDK và có các quyền AWS cần thiết.

2. **Triển khai mô hình**: Sử dụng đoạn mã sau để triển khai và sử dụng DeepSeek-R1 cho suy luận:
    ```bash
   pip install --force-reinstall --no-cache-dir sagemaker==2.235.2
    ```

   ```python
   from sagemaker.serve.builder.model_builder import ModelBuilder
   from sagemaker.serve.builder.schema_builder import SchemaBuilder
   from sagemaker.jumpstart.model import ModelAccessConfig
   from sagemaker.session import Session
   import logging

   sagemaker_session = Session()
   artifacts_bucket_name = sagemaker_session.default_bucket()
   execution_role_arn = sagemaker_session.get_caller_identity_arn()
   js_model_id = "deepseek-llm-r1"
   gpu_instance_type = "ml.p5e.48xlarge"
   response = "Hello, I'm a language model, and I'm here to help you with your English."
   sample_input = {
       "inputs": "Hello, I'm a language model,",
       "parameters": {"max_new_tokens": 128, "top_p": 0.9, "temperature": 0.6},
   }
   sample_output = [{"generated_text": response}]

   schema_builder = SchemaBuilder(sample_input, sample_output)
   model_builder = ModelBuilder(
       model=js_model_id,
       schema_builder=schema_builder,
       sagemaker_session=sagemaker_session,
       role_arn=execution_role_arn,
       log_level=logging.ERROR
   )

   model= model_builder.build()
   predictor = model.deploy(model_access_configs={js_model_id:ModelAccessConfig(accept_eula=True)}, accept_eula=True)
   predictor.predict(sample_input)
   ```

3. **Gửi yêu cầu suy luận**: Sau khi triển khai, bạn có thể gửi các yêu cầu suy luận bổ sung:

   ```python
   new_input = {
       "inputs": "What is Amazon doing in Generative AI?",
       "parameters": {"max_new_tokens": 64, "top_p": 0.8, "temperature": 0.7},
   }
   prediction = predictor.predict(new_input)
   print(prediction)
   ```


### Triển khai qua SageMaker trên Neuron

Hướng dẫn này mô tả cách triển khai DeepSeek-R1-Distill-Llama-70B trên một máy Neuron của AWS, chẳng hạn như AWS Trainium 2 và AWS Inferentia 2.

#### Yêu cầu trước khi triển khai

Trước khi triển khai mô hình, hãy đảm bảo bạn đã có:
- Một **AWS SageMaker Domain** được cấu hình.
- Hạn mức SageMaker đủ (tăng hạn mức mặc định cho `ml.inf2.48xlarge` lên 1 để sử dụng endpoint).
- Một không gian **JupyterLab** có sẵn để phát triển.

#### Thiết lập phiên làm việc SageMaker

Khởi tạo một phiên làm việc SageMaker để xác định vùng AWS hiện tại và vai trò thực thi:

```python
import json
import sagemaker
import boto3
from sagemaker.huggingface import HuggingFaceModel, get_huggingface_llm_image_uri

try:
    role = sagemaker.get_execution_role()
except ValueError:
    iam = boto3.client("iam")
    role = iam.get_role(RoleName="sagemaker_execution_role")["Role"]["Arn"]
```

#### Tạo đối tượng mô hình trong SageMaker

Xác định mô hình SageMaker bằng Python SDK:

```python
image_uri = get_huggingface_llm_image_uri("huggingface-neuronx", version="0.0.25")
model_id = "deepseek-ai/DeepSeek-R1-Distill-Llama-70B"
model_name = model_id.split("/")[-1].lower()

# Cấu hình mô hình từ Hugging Face
hub = {
    "HF_MODEL_ID": model_id,
    "HF_NUM_CORES": "24",
    "HF_AUTO_CAST_TYPE": "bf16",
    "MAX_BATCH_SIZE": "4",
    "MAX_INPUT_TOKENS": "3686",
    "MAX_TOTAL_TOKENS": "4096",
}

# Tạo đối tượng mô hình Hugging Face
huggingface_model = HuggingFaceModel(
    image_uri=image_uri,
    env=hub,
    role=role,
)
```

#### Triển khai mô hình trên endpoint của SageMaker

```python
endpoint_name = f"{model_name}-ep"

# Triển khai mô hình trên SageMaker Inference
predictor = huggingface_model.deploy(
    endpoint_name=endpoint_name,
    initial_instance_count=1,
    instance_type="ml.inf2.48xlarge",
    container_startup_health_check_timeout=3600,
    volume_size=512,
)
```

#### Kiểm tra endpoint

```python
response = predictor.predict(
    {
        "inputs": "Thủ đô của Pháp là gì?",
        "parameters": {
            "do_sample": True,
            "max_new_tokens": 128,
            "temperature": 0.7,
            "top_k": 50,
            "top_p": 0.95,
        }
    }
)
print(response)
```

#### Xóa endpoint sau khi kiểm tra

```python
predictor.delete_model()
predictor.delete_endpoint()
```

---

### Triển khai trên EC2 Neuron với Hugging Face Neuron Deep Learning AMI

Hướng dẫn này mô tả cách xuất, triển khai và chạy **DeepSeek-R1-Distill-Llama-70B** trên một máy `inf2.48xlarge` của AWS EC2.

#### Yêu cầu trước khi triển khai

Trước khi tiếp tục, hãy đảm bảo:
- Bạn đã đăng ký **Hugging Face Neuron Deep Learning AMI** trên AWS Marketplace.
- Bạn đã khởi chạy một máy **inf2.48xlarge** trên EC2 với AMI này.
- Bạn đã kết nối với máy thông qua SSH.

Nếu bạn chưa quen với việc khởi chạy EC2, hãy tham khảo tài liệu của AWS.

#### Triển khai mô hình trên endpoint của EC2

Chạy lệnh sau trên máy EC2 để triển khai mô hình:

```sh
docker run -p 8080:80 \
    -v $(pwd)/data:/data \
    --device=/dev/neuron0 \
    --device=/dev/neuron1 \
    --device=/dev/neuron2 \
    --device=/dev/neuron3 \
    --device=/dev/neuron4 \
    --device=/dev/neuron5 \
    --device=/dev/neuron6 \
    --device=/dev/neuron7 \
    --device=/dev/neuron8 \
    --device=/dev/neuron9 \
    --device=/dev/neuron10 \
    --device=/dev/neuron11 \
    -e HF_BATCH_SIZE=4 \
    -e HF_SEQUENCE_LENGTH=4096 \
    -e HF_AUTO_CAST_TYPE="bf16" \
    -e HF_NUM_CORES=24 \
    ghcr.io/huggingface/neuronx-tgi:latest \
    --model-id deepseek-ai/DeepSeek-R1-Distill-Llama-70B \
    --max-batch-size 4 \
    --max-total-tokens 4096
```

Quá trình này sẽ mất vài phút để tải mô hình đã biên dịch từ Hugging Face cache và khởi chạy một **Text Generation Inference (TGI) endpoint**.

#### Kiểm tra endpoint

Để xác nhận rằng mô hình đang chạy đúng, gửi yêu cầu kiểm tra:

```sh
curl localhost:8080/generate \
    -X POST \
    -d '{"inputs":"Tại sao bầu trời tối vào ban đêm?"}' \
    -H 'Content-Type: application/json'
```

#### Tạm dừng máy EC2

Để tránh phát sinh chi phí không cần thiết, hãy **tạm dừng hoặc hủy máy EC2** sau khi kiểm tra.


### Lưu ý về Chi phí

- **Giờ sử dụng Instance**: Bạn sẽ bị tính phí dựa trên số giờ sử dụng instance. Chi phí phụ thuộc vào loại instance (ví dụ: `ml.p5e.48xlarge`) và số lượng instance bạn chọn.

- **Nhập mô hình tùy chỉnh**: Nếu bạn sử dụng tính năng nhập mô hình tùy chỉnh, phí sẽ được tính theo gia số 5 phút, dựa trên mức sử dụng và kích thước của mô hình.

- **Truyền dữ liệu**: Phí có thể áp dụng cho việc truyền dữ liệu vào và ra khỏi SageMaker.

- **Lưu trữ**: Phí lưu trữ có thể áp dụng cho mô hình và dữ liệu của bạn trong Amazon S3.
