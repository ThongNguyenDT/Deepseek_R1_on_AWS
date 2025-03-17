---
title: "Hand on"
date :  "`r Sys.Date()`" 
weight: 2
chapter: false
pre: " <b> 7.2. </b> "
---
Hướng dẫn Triển khai Mô hình DeepSeek-R1 trên Amazon Bedrock

![Amazon Bedrock Console](https://aws.amazon.com/bedrock/developer-experience/)

### Giới thiệu

DeepSeek-R1 là một mô hình ngôn ngữ lớn (LLM) tiên tiến, được phát triển bởi DeepSeek AI, hiện có sẵn trên Amazon Bedrock Marketplace và Amazon SageMaker JumpStart. Mô hình này hỗ trợ các tác vụ phức tạp như giải toán và lập trình, giúp doanh nghiệp dễ dàng tích hợp AI vào ứng dụng của mình. Bài viết này sẽ hướng dẫn chi tiết các bước triển khai DeepSeek-R1 trên Amazon Bedrock.

### Bước 1: Truy cập Amazon Bedrock Console

1. **Đăng nhập vào AWS Management Console**: Sử dụng thông tin tài khoản AWS của bạn để đăng nhập.

2. **Tìm kiếm dịch vụ Amazon Bedrock**: Trong thanh tìm kiếm, nhập "Bedrock" và chọn **Amazon Bedrock** từ kết quả.

   ![Tìm kiếm Amazon Bedrock](https://aws.amazon.com/bedrock/developer-experience/)

3. **Truy cập Model Catalog**: Trong bảng điều khiển bên trái, chọn **Model catalog** dưới mục **Foundation models**.

   ![Model Catalog](https://aws.amazon.com/bedrock/developer-experience/)

4. **Lọc và chọn mô hình DeepSeek-R1**: Sử dụng bộ lọc nhà cung cấp để chọn **DeepSeek**, sau đó chọn mô hình **DeepSeek-R1**.

   ![Chọn DeepSeek-R1](https://aws.amazon.com/bedrock/developer-experience/)

### Bước 2: Triển khai Mô hình

1. **Bắt đầu triển khai**: Trên trang chi tiết của DeepSeek-R1, nhấn **Deploy**.

2. **Cấu hình chi tiết triển khai**:

   - **Endpoint name**: Nhập tên cho endpoint (từ 1-50 ký tự chữ và số).

   - **Number of instances**: Xác định số lượng instances (từ 1-100).

   - **Instance type**: Chọn loại instance phù hợp. Để có hiệu suất tối ưu với DeepSeek-R1, nên sử dụng các instance dựa trên GPU như `ml.g6.2xlarge`.

     > **Lưu ý**: Đảm bảo bạn có đủ hạn ngạch (quota) cho loại instance đã chọn.

3. **Cài đặt nâng cao (tùy chọn)**:

   - **Triển khai trong VPC**: Nếu muốn triển khai trong Virtual Private Cloud (VPC), mở rộng phần **Advanced settings** và cấu hình theo nhu cầu.

   - **IAM Service Role**: Amazon Bedrock Marketplace tự động tạo một service role để truy cập vào các bucket Amazon S3 nơi lưu trữ trọng số của mô hình. Bạn cũng có thể chọn sử dụng một role hiện có.

     ![Cài đặt Nâng cao](https://aws.amazon.com/bedrock/developer-experience/)

4. **Hoàn tất triển khai**: Nhấn **Deploy** để bắt đầu quá trình triển khai. Quá trình này có thể mất vài phút để hoàn tất.

   > **Lưu ý**: Sau khi triển khai, mô hình của bạn sẽ được triển khai lên endpoint thời gian thực của Amazon SageMaker. Chi phí sẽ được tính dựa trên hạ tầng phần cứng đã chọn. Tham khảo [giá của Amazon SageMaker](https://aws.amazon.com/sagemaker-ai/pricing/realtime-endpoint) để biết thêm chi tiết.

### Bước 3: Kiểm tra Mô hình trong Playground

1. **Mở Playground**: Sau khi triển khai hoàn tất, nhấn **Open in playground** để truy cập giao diện tương tác.

   ![Amazon Bedrock Playground](https://aws.amazon.com/bedrock/developer-experience/)

2. **Thử nghiệm với các prompts**: Tại đây, bạn có thể thử nghiệm với các prompts khác nhau và điều chỉnh các tham số của mô hình như `temperature` và `maximum length`.

   > **Mẹo**: Khi sử dụng DeepSeek-R1 với `InvokeModel` của Bedrock và Playground Console, hãy sử dụng mẫu chat của DeepSeek để có kết quả tối ưu. Ví dụ: `<|begin of sentence|><|User|>nội dung cần suy luận<|Assistant|>`.

### Bước 4: Thực hiện Inference với Guardrails

1. **Tạo Guardrail**: Bạn có thể tạo guardrail thông qua Amazon Bedrock console hoặc API. Guardrails giúp ngăn chặn nội dung có hại và đánh giá mô hình dựa trên các tiêu chí an toàn.

   > **Tham khảo**: Xem thêm ví dụ mã để tạo guardrail trong [GitHub repository](https://github.com/aws/amazon-bedrock-samples).

2. **Áp dụng Guardrail**: Sử dụng API `ApplyGuardrail` của Amazon Bedrock để áp dụng guardrails cho mô hình DeepSeek-R1 đã triển khai. Quá trình này bao gồm:

   - **Kiểm tra đầu vào**: Đánh giá input từ người dùng trước khi gửi đến mô hình.

   - **Kiểm tra đầu ra**: Đánh giá output từ mô hình trước khi trả về cho người dùng.

   > **Lưu ý**: Nếu input hoặc output vi phạm guardrail, hệ thống sẽ trả về thông báo cảnh báo.

   ![Amazon Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/)

### Bước 5: Dọn dẹp (Clean Up)

Để tránh các chi phí không mong muốn, hãy xóa deployment khi không còn sử dụng:

1. **Truy cập Marketplace Deployments**: Trong Amazon Bedrock console, dưới mục **Foundation models**, chọn **Marketplace deployments**.

2. **Xóa Endpoint**: Tìm endpoint bạn muốn xóa, chọn nó, sau đó trong menu **Actions**, chọn **Delete**.

3. **Xác nhận xóa**: Trong hộp thoại xác nhận, nhập `confirm` và nhấn **Delete** để xóa vĩnh viễn endpoint.

   ![Xóa Deployment](https://aws.amazon.com/bedrock/developer-experience/)

### Lưu ý Quan trọng

- **Quyền truy cập**: Để triển khai DeepSeek-R1, bạn cần quyền truy cập vào các instance phù hợp, như `ml.g6.2xlarge`.

- **Hạn ngạch (Quota)**: Đảm bảo tài khoản của bạn có đủ hạn ngạch cho loại instance đã chọn.

- **An toàn**: Nên triển khai mô hình với guardrails để đảm bảo an toàn và tuân thủ các chính sách AI có trách nhiệm.

- **Chi phí**: Việc lựa chọn loại instance và số lượng instances phù hợp rất quan trọng để tối ưu hóa chi phí và hiệu suất.

> **Tham khảo thêm**: [DeepSeek-R1 Model Now Available in Amazon Bedrock]()