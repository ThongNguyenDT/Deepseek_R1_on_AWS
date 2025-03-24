---
title: "Hand On"
date :  "`r Sys.Date()`" 
weight: 2
chapter: false
pre: " <b> 9.2. </b> "
---


Trong hướng dẫn này, chúng ta sẽ sử dụng mô hình DeepSeek-R1-Distill-Llama-8B, một phiên bản nhẹ hơn yêu cầu ít tài nguyên hơn so với mô hình đầy đủ với 671 tỷ tham số. Nếu muốn triển khai mô hình đầy đủ, bạn có thể thay thế mô hình trong cấu hình vLLM.

### Các Yêu Cầu Triển khai

Chúng ta sẽ sử dụng AWS CloudShell để thiết lập môi trường, giúp đơn giản hóa quá trình triển khai.

1. **Kiểm Tra Hạn Ngạch Dịch Vụ AWS**: Đảm bảo tài khoản AWS của bạn có đủ hạn ngạch để khởi chạy các phiên bản EC2 cần thiết, đặc biệt là các phiên bản GPU như G hoặc P. Bạn có thể kiểm tra hạn ngạch tại [AWS EC2 Instance Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/ec2.html).

2. **Cài Đặt `kubectl`**: Công cụ dòng lệnh để tương tác với Kubernetes.

3. **Cài Đặt Terraform**: Công cụ để quản lý hạ tầng dưới dạng mã.

4. **Cài Đặt Finch hoặc Docker**: Công cụ để xây dựng và quản lý container.


### Hướng dẫn chi tiết từng bước

#### Bước 1: Clone repository
Đầu tiên, clone repo GitHub chứa các file cấu hình cần thiết:

```bash
git clone https://github.com/aws-samples/deepseek-using-vllm-on-eks
cd deepseek-using-vllm-on-eks
```

#### Bước 2: Khởi tạo và áp dụng cấu hình TerraForm
Sử dụng TerraForm để tạo cluster EKS, VPC, và repository ECR. Chạy các lệnh sau:

```bash
terraform init
terraform apply -auto-approve
```

Sau đó, cấu hình kubectl để kết nối với cluster EKS:

```bash
$(terraform output configure_kubectl | jq -r)
```

File `nodepool_automode.tf` trong repo giúp kích hoạt chế độ auto mode cho node pools, cho phép AWS tự động quản lý việc mở rộng và chọn instance, tối ưu hóa hiệu suất và chi phí.

#### Bước 3: Triển khai model DeepSeek với vLLM
Bạn có thể triển khai với hỗ trợ GPU hoặc Neuron (Inferentia). Dưới đây là hướng dẫn cho từng trường hợp:

##### Triển khai với GPU
Chạy lệnh sau để kích hoạt hỗ trợ GPU:

```bash
terraform apply -auto-approve -var="enable_deep_seek_gpu=true" -var="enable_auto_mode_node_pool=true"
```

##### Triển khai với Neuron (Inferentia)
Trước tiên, xây dựng và đẩy image vLLM cho Neuron:

1. Xuất URI repository ECR cho Neuron:

```bash
export ECR_repo_neuron=$(terraform output ecr_repository_uri_neuron | jq -r)
```

2. Clone repo vLLM:

```bash
git clone https://github.com/vllm-project/vllm
```

3. Xây dựng và đẩy image:

```bash
finch build --platform linux/amd64 -f Dockerfile.neuron -t $ECR_repo_neuron:0.1 .
aws ecr get-login-password | finch login --username AWS --password-stdin $ECR_repo_neuron
finch push $ECR_repo_neuron:0.1
```

4. Áp dụng cấu hình TerraForm với hỗ trợ Neuron:

```bash
terraform apply -auto-approve -var="enable_deep_seek_gpu=true" -var="enable_deep_seek_neuron=true" -var="enable_auto_mode_node_pool=true"
```

AWS Neuron là SDK tối ưu hóa cho các chip Inferentia và Trainium, phù hợp cho suy luận hiệu quả, đặc biệt với các mô hình lớn.

#### Bước 4: Kiểm tra trạng thái Pod và Node
Đảm bảo các pod đang chạy đúng:

```bash
kubectl get po -n deepseek
```

Kiểm tra node:

```bash
kubectl get nodes -l owner=data-engineer
```

Nếu pod đang chờ (pending), kiểm tra log để tìm lỗi:

```bash
kubectl logs deployment.apps/deepseek-gpu-vllm-chart -n deepseek
```

hoặc

```bash
kubectl logs deployment.apps/deepseek-neuron-vllm-chart -n deepseek
```

Tham khảo [AWS EC2 Instance Quotas](https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-instance-quotas.html) nếu gặp vấn đề về giới hạn instance.

#### Bước 5: Thiết lập proxy cục bộ để tương tác với mô hình
Cho Neuron (cổng 8080):

```bash
kubectl port-forward svc/deepseek-neuron-vllm-chart -n deepseek 8080:80 > port-forward-neuron.log 2>&1 &
```

Cho GPU (cổng 8081):

```bash
kubectl port-forward svc/deepseek-gpu-vllm-chart -n deepseek 8081:80 > port-forward-gpu.log 2>&1 &
```

Kiểm tra mô hình với lệnh curl:

```bash
curl -X POST "http://localhost:8080/v1/chat/completions" -H "Content-Type: application/json" --data '{
"model": "deepseek-ai/DeepSeek-R1-Distill-Llama-8B",
"messages": [{
"role": "user",
"content": "What is Kubernetes?"
}]
}'
```

File `helm.tf` trong repo tùy chỉnh Helm chart cho vLLM, hỗ trợ cấu hình tài nguyên, node selector, và tolerations cho model DeepSeek.

#### Bước 6: Xây dựng và triển khai Chatbot UI
1. Xuất URI repository ECR:

```bash
export ECR_repo=$(terraform output ecr_repository_uri | jq -r)
```

2. Xây dựng image Chatbot UI:

```bash
finch build --platform linux/amd64 -t $ECR_repo:0.1 chatbot-ui/application/.
```

3. Đăng nhập và đẩy image:

```bash
aws ecr get-login-password | finch login --username AWS --password-stdin $ECR_repo
finch push $ECR_repo:0.1
```

4. Cập nhật manifest deployment với image và mật khẩu ngẫu nhiên:

```bash
sed -i "s#__IMAGE_DEEPSEEK_CHATBOT__#$ECR_repo:0.1#g" chatbot-ui/manifests/deployment.yaml
sed -i "s|__PASSWORD__|$(openssl rand -base64 12 | tr -dc A-Za-z0-9 | head -c 16)|" chatbot-ui/manifests/deployment.yaml
```

5. Áp dụng manifest:

```bash
kubectl apply -f chatbot-ui/manifests/ingress-class.yaml
kubectl apply -f chatbot-ui/manifests/deployment.yaml
```

6. Lấy URL Chatbot UI:

```bash
echo http://$(kubectl get ingress/deepseek-chatbot-ingress -n deepseek -o json | jq -r '.status.loadBalancer.ingress[0].hostname')
```

7. Lấy thông tin đăng nhập:

```bash
echo -e "Username=$(kubectl get secret deepseek-chatbot-secrets -n deepseek -o jsonpath='{.data.admin-username}' | base64 --decode)\nPassword=$(kubectl get secret deepseek-chatbot-secrets -n deepseek -o jsonpath='{.data.admin-password}' | base64 --decode)"
```
