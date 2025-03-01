---
title : "Distill information"
date :  "`r Sys.Date()`" 
weight : 2 
chapter : false
pre : " <b> 2. </b> "
---
## 1. Tổng quan
DeepSeek-R1 là một mô hình AI mã nguồn mở do một công ty Trung Quốc phát triển, tập trung vào khả năng suy luận và được thiết kế để cạnh tranh trực tiếp với OpenAI o1. Trong nhiều thử nghiệm, DeepSeek-R1 cho thấy hiệu suất ngang bằng hoặc vượt qua OpenAI o1, đặc biệt là trong các tác vụ toán học và lập luận đa bước.

Tuy nhiên, OpenAI o1 có lợi thế trong một số lĩnh vực như lập trình và kiến thức thực tế. Một điểm đáng chú ý là DeepSeek-R1 có chi phí thấp hơn đáng kể và cho phép cộng đồng tùy chỉnh, trong khi OpenAI o1 là mô hình độc quyền.

## 2. Kết quả thử nghiệm chi tiết

### 2.1. Toán học
| Bài kiểm tra | DeepSeek-R1 | OpenAI o1-1217 | Nhận xét |
|-------------|------------|----------------|----------|
| AIME 2024 | **79.8%** | 79.2% | DeepSeek-R1 nhỉnh hơn trong suy luận toán học phức tạp. |
| MATH-500 | **97.3%** | 96.4% | DeepSeek-R1 thể hiện xuất sắc ở toán cấp trung học. |

### 2.2. Lập trình
| Bài kiểm tra | DeepSeek-R1 | OpenAI o1-1217 | Nhận xét |
|-------------|------------|----------------|----------|
| Codeforces | 96.3% | **96.6%** | OpenAI o1 nhỉnh hơn, nhưng không đáng kể. |
| SWE-bench Verified | **49.2%** | 48.9% | DeepSeek-R1 có lợi thế nhỏ trong suy luận kỹ thuật phần mềm. |

### 2.3. Kiến thức chung
| Bài kiểm tra | DeepSeek-R1 | OpenAI o1-1217 | Nhận xét |
|-------------|------------|----------------|----------|
| GPQA Diamond | 71.5% | **75.7%** | OpenAI o1 dẫn trước trong hiểu biết kiến thức thực tế. |
| MMLU | 90.8% | **91.8%** | OpenAI o1 nhỉnh hơn một chút về hiểu biết đa lĩnh vực. |


<div class="notices tip">
<p style="padding-bottom: 0;">- DeepSeek-R1 có khả năng giải thích quá trình suy luận của mình, điều này rất quan trọng trong các lĩnh vực đòi hỏi tính minh bạch như nghiên cứu và các quyết định phức tạp. </p>
<p style="padding-bottom: 0; padding-top: 0; border: none">- DeepSeek-R1 là mã nguồn mở, cho phép các nhà phát triển và nhà nghiên cứu tùy chỉnh và sử dụng theo mục đích của họ, trong khi mô hình của OpenAI là độc quyền. </p>
<p style="padding-top: 0; border: none">- Chi phí của DeepSeek-R1 thấp hơn đáng kể so với OpenAI o1.</p>
</div>

## 3. Distilled Models performance
![image](/images/2.Distill%20information/img.png)

**Mục đích của Distillation:**
*   **Distillation** trong AI là quá trình tạo ra các mô hình nhỏ hơn, hiệu quả hơn từ các mô hình lớn hơn, giữ lại phần lớn khả năng suy luận của chúng nhưng giảm yêu cầu về tính toán. DeepSeek đã áp dụng kỹ thuật này để tạo ra một bộ các mô hình distill từ R1, sử dụng kiến trúc Qwen và Llama.

**Các Mô Hình Distill Dựa Trên Qwen:**

*   **DeepSeek-R1-Distill-Qwen-1.5B:**
    *   Đây là mô hình distill nhỏ nhất, đạt 83.9% trên MATH-500.
    *   Hiệu suất thấp trên LiveCodeBench (16.9%), cho thấy khả năng lập trình hạn chế.
    *   Mô hình này phù hợp cho các tác vụ toán học cơ bản nhưng không mạnh về coding.
*   **DeepSeek-R1-Distill-Qwen-7B:**
    *   Điểm số cao trên MATH-500 (92.8%), thể hiện khả năng suy luận toán học mạnh mẽ.
    *   Hiệu suất ở mức trung bình trên GPQA Diamond (49.1%), cho thấy sự cân bằng giữa suy luận toán học và kiến thức thực tế.
    *   Hiệu suất không cao trên LiveCodeBench (37.6%) và CodeForces (1189 rating), cho thấy không phù hợp cho các tác vụ coding phức tạp.
*   **DeepSeek-R1-Distill-Qwen-14B:**
    *   Hiệu suất tốt trên MATH-500 (93.9%), thể hiện khả năng xử lý các bài toán toán học phức tạp.
    *   Điểm 59.1% trên GPQA Diamond cũng cho thấy khả năng suy luận dựa trên kiến thức thực tế.
    *   Hiệu suất trên LiveCodeBench (53.1%) và CodeForces (1481 rating) cho thấy vẫn còn chỗ để cải thiện trong các tác vụ coding và lập trình.
*   **DeepSeek-R1-Distill-Qwen-32B:**
    *   Mô hình lớn nhất trong các mô hình Qwen, đạt điểm cao nhất trên AIME 2024 (72.6%), đánh giá khả năng suy luận toán học đa bước nâng cao.
    *   Hiệu suất xuất sắc trên MATH-500 (94.3%) và GPQA Diamond (62.1%), thể hiện sức mạnh trong cả suy luận toán học và kiến thức thực tế.
    *   Kết quả trên LiveCodeBench (57.2%) và CodeForces (1691 rating) cho thấy mô hình linh hoạt nhưng không tối ưu cho các tác vụ lập trình so với các mô hình chuyên về coding.

**Các Mô Hình Distill Dựa Trên Llama:**

*   **DeepSeek-R1-Distill-Llama-8B:**
    *   Hiệu suất tốt trên MATH-500 (89.1%) và ở mức trung bình trên GPQA Diamond (49.0%), cho thấy khả năng xử lý suy luận toán học và kiến thức thực tế.
    *   Điểm thấp trên các benchmark về coding như LiveCodeBench (39.6%) và CodeForces (1205 rating), cho thấy giới hạn trong các tác vụ liên quan đến lập trình so với các mô hình dựa trên Qwen.
*   **DeepSeek-R1-Distill-Llama-70B:**
    *   Mô hình distill lớn nhất, đạt hiệu suất hàng đầu trên MATH-500 (94.5%), tốt nhất trong tất cả các mô hình distill.
    *   Đạt điểm 86.7% trên AIME 2024, là lựa chọn tuyệt vời cho suy luận toán học nâng cao.
    *   Hiệu suất tốt trên LiveCodeBench (57.5%) và CodeForces (1633 rating), cho thấy có khả năng coding tốt hơn hầu hết các mô hình khác. Trong lĩnh vực này, nó tương đương với o1-mini hoặc GPT-4o của OpenAI.

**Tổng quan:**

*   Các mô hình distill dựa trên **Qwen** tập trung vào **hiệu quả và khả năng mở rộng**, cung cấp sự cân bằng giữa hiệu suất và yêu cầu tính toán.
*   Các mô hình distill dựa trên **Llama** ưu tiên **hiệu suất cao** và khả năng suy luận nâng cao, đặc biệt xuất sắc trong các tác vụ đòi hỏi độ chính xác về toán học và kiến thức thực tế.


<div class="notices custom">
        <ul>
            <li>Các mô hình distill dựa trên <strong>Qwen</strong> tập trung vào <strong>hiệu quả và khả năng mở rộng</strong>, cung cấp sự cân bằng giữa hiệu suất và yêu cầu tính toán.</li>
            <li>Các mô hình distill dựa trên <strong>Llama</strong> ưu tiên <strong>hiệu suất cao</strong> và khả năng suy luận nâng cao, đặc biệt xuất sắc trong các tác vụ đòi hỏi độ chính xác về toán học và kiến thức thực tế.</li>
        </ul>
</div>

## 4. Operate cost
Đây là so sánh chi tiết về chi phí giữa DeepSeek-R1 và OpenAI o1:


**Chi tiết các loại chi phí:**

*   **Chi phí đầu vào (Cached Input):**
    *   **DeepSeek-R1:** $0.14 trên 1 triệu tokens
    *   **OpenAI o1:** $7.50 trên 1 triệu tokens
    *   **Giải thích:** Chi phí này áp dụng cho các văn bản đầu vào lặp lại hoặc đã được xử lý trước đó. DeepSeek-R1 có lợi thế lớn về chi phí trong trường hợp này.

*   **Chi phí đầu vào (Input):**
    *   **DeepSeek-R1:** $0.55 trên 1 triệu tokens
    *   **OpenAI o1:** $15.00 trên 1 triệu tokens
    *   **Giải thích:** Chi phí này áp dụng cho các văn bản đầu vào mới, chưa từng được xử lý trước đó. DeepSeek-R1 tiếp tục có chi phí thấp hơn đáng kể.

*   **Chi phí đầu ra (Output):**
    *   **DeepSeek-R1:** $2.19 trên 1 triệu tokens
    *   **OpenAI o1:** $60.00 trên 1 triệu tokens
    *   **Giải thích:** Đây là chi phí cho văn bản được tạo ra bởi mô hình để đáp lại các đầu vào. DeepSeek-R1 có mức giá rẻ hơn rất nhiều so với OpenAI o1.

**Phân tích chi phí:**

*   Sự khác biệt về chi phí giữa hai mô hình là rất lớn, với **DeepSeek-R1 rẻ hơn đáng kể** trên tất cả các hạng mục.
*   **Ví dụ:** Chi phí cho output của DeepSeek-R1 chỉ là **$2.19** trên 1 triệu token, trong khi của OpenAI o1 là **$60.00** trên 1 triệu token.
*   Điều này có thể giúp các tổ chức tiết kiệm đáng kể chi phí, đặc biệt là khi chạy các hoạt động AI quy mô lớn hoặc các dự án khởi nghiệp với ngân sách hạn chế.
*   DeepSeek-R1 có thể là một lựa chọn tốt hơn cho các ứng dụng **nhạy cảm về chi phí**.

**Bảng so sánh tóm tắt (chi phí trên 1 triệu tokens):**

| Loại chi phí         | DeepSeek-R1 | OpenAI o1 |
|----------------------|:-----------:|:---------:|
| Đầu vào (cache hit)  |    $0.14    |   $7.50   |
| Đầu vào (cache miss) |    $0.55    |  $15.00   |
| Đầu ra               |    $2.19    |  $60.00   |

**Lưu ý:**

*   Chi phí của DeepSeek-R1 được đề cập ở đây là chi phí cho mô hình **deepseek-reasoner**.
*   Các giá trên có thể thay đổi, nên tham khảo trang giá chính thức của DeepSeek để có thông tin mới nhất.
*   DeepSeek cung cấp tính năng **context caching** để giảm chi phí cho các đầu vào lặp lại trong các cuộc hội thoại nhiều lượt.

## 5. Yêu cầu triền khai Deepseek

| Model                         | n_param | weight size | vRAM/ neuron RAM | Speed (response_token/second) |
|-------------------------------|:-------:|:-----------:|:----------------:|:-----------------------------:|
| DeepSeek-R1                   |  671B   |             |    ~1,342 GB     |                               |
| DeepSeek-R1-Distill-Qwen-1.5B |  1.8B   |   1.1 GB    |     ~0.7 GB      |     218.42 (RTX 6000 ada)     |
| DeepSeek-R1-Distill-Qwen-7B   |  7.6B   |   4.7 GB    |     ~3.3 GB      |                               |
| DeepSeek-R1-Distill-Qwen-14B  |  14.8B  |   9.0 GB    |     ~6.5 GB      |                               |
| DeepSeek-R1-Distill-Qwen-32B  |  32.8B  |    19 GB    |     ~14.9 GB     |                               |
| DeepSeek-R1-Distill-Llama-8B  |  8.0B   |   4.9 GB    |     ~3.7 GB      |                               |
| DeepSeek-R1-Distill-Llama-70B |  70.6B  |    42 GB    |    ~32.7 GB      |                               |
