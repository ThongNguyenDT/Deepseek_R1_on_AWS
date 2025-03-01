---
title : "Distill information"
date :  "`r Sys.Date()`" 
weight : 2 
chapter : false
pre : " <b> 2. </b> "
---

## 1. Overview
DeepSeek-R1 is an open-source AI model developed by a Chinese company, focusing on reasoning capabilities and designed to compete directly with OpenAI o1. In various tests, DeepSeek-R1 demonstrated performance on par with or exceeding OpenAI o1, especially in mathematical tasks and multi-step reasoning.

However, OpenAI o1 holds an advantage in certain areas such as programming and general knowledge. Notably, DeepSeek-R1 is significantly more cost-effective and allows community customization, whereas OpenAI o1 remains a proprietary model.

## 2. Detailed Test Results

### 2.1. Mathematics
| Test       | DeepSeek-R1 | OpenAI o1-1217 | Remarks                                                                    |
|------------|:-----------:|:--------------:|:---------------------------------------------------------------------------|
| AIME 2024  |  **79.8%**  |     79.2%      | DeepSeek-R1 excels in complex mathematical reasoning.                      |
| MATH-500   |  **97.3%**  |     96.4%      | DeepSeek-R1 performs exceptionally well in high school-level mathematics.  |

### 2.2. Programming
| Test                | DeepSeek-R1 | OpenAI o1-1217 | Remarks                                                               |
|:--------------------|:-----------:|:--------------:|-----------------------------------------------------------------------|
| Codeforces          |   96.3%     |   **96.6%**    | OpenAI o1 has a slight edge, but the difference is minor.             |
| SWE-bench Verified  |  **49.2%**  |     48.9%      | DeepSeek-R1 has a slight advantage in software engineering reasoning. |

### 2.3. General Knowledge
| Test          | DeepSeek-R1 | OpenAI o1-1217 | Remarks                                                     |
|---------------|:-----------:|:--------------:|-------------------------------------------------------------|
| GPQA Diamond  |   71.5%     |   **75.7%**    | OpenAI o1 leads in factual knowledge.                       |
| MMLU          |    90.8%    |   **91.8%**    | OpenAI o1 has a slight advantage in multi-domain knowledge. |

<div class="notices tip">
<p style="padding-bottom: 0;">- DeepSeek-R1 can explain its reasoning process, which is crucial for fields requiring transparency, such as research and complex decision-making.</p>
<p style="padding-bottom: 0; padding-top: 0; border: none">- DeepSeek-R1 is open-source, allowing developers and researchers to customize and use it as needed, whereas OpenAI's model is proprietary.</p>
<p style="padding-top: 0; border: none">- DeepSeek-R1 is significantly more cost-effective than OpenAI o1.</p>
</div>

## 3. Distilled Models Performance
![image](/images/2.Distill%20information/img.png)

**Purpose of Distillation:**
* **Distillation** in AI refers to the process of creating smaller, more efficient models from larger ones, retaining most of their reasoning capabilities while reducing computational requirements. DeepSeek has applied this technique to create a series of distilled models from R1, utilizing the Qwen and Llama architectures.

**Distilled Models Based on Qwen:**

* **DeepSeek-R1-Distill-Qwen-1.5B:**
    * The smallest distilled model, achieving 83.9% on MATH-500.
    * Low performance on LiveCodeBench (16.9%), indicating limited programming capabilities.
    * Suitable for basic mathematical tasks but not strong in coding.
* **DeepSeek-R1-Distill-Qwen-7B:**
    * High score on MATH-500 (92.8%), demonstrating strong mathematical reasoning.
    * Moderate performance on GPQA Diamond (49.1%), balancing math and factual knowledge.
    * Not optimized for complex coding tasks (LiveCodeBench 37.6%, CodeForces 1189 rating).
* **DeepSeek-R1-Distill-Qwen-14B:**
    * Strong performance on MATH-500 (93.9%), handling complex mathematical problems.
    * Score of 59.1% on GPQA Diamond, showing reasoning based on factual knowledge.
    * Performance on LiveCodeBench (53.1%) and CodeForces (1481 rating) indicates room for improvement in coding tasks.
* **DeepSeek-R1-Distill-Qwen-32B:**
    * The largest Qwen-based model, achieving the highest score on AIME 2024 (72.6%), excelling in advanced multi-step reasoning.
    * Outstanding results on MATH-500 (94.3%) and GPQA Diamond (62.1%), showing strength in both mathematical reasoning and factual knowledge.
    * Results on LiveCodeBench (57.2%) and CodeForces (1691 rating) indicate flexibility but not optimal coding performance.

**Distilled Models Based on Llama:**

* **DeepSeek-R1-Distill-Llama-8B:**
    * Strong performance on MATH-500 (89.1%) and moderate on GPQA Diamond (49.0%).
    * Lower scores on coding benchmarks like LiveCodeBench (39.6%) and CodeForces (1205 rating), indicating limitations in programming tasks.
* **DeepSeek-R1-Distill-Llama-70B:**
    * The largest distilled model, excelling in MATH-500 (94.5%), the best among all distilled models.
    * Achieved 86.7% on AIME 2024, making it an excellent choice for advanced mathematical reasoning.
    * Strong coding performance (LiveCodeBench 57.5%, CodeForces 1633 rating), comparable to OpenAI o1-mini or GPT-4o.

<div class="notices custom">
<ul>
<li>Qwen-based distilled models focus on **efficiency and scalability**, balancing performance and computational cost.</li>
<li>Llama-based distilled models prioritize **high performance** and advanced reasoning, excelling in tasks requiring mathematical and factual accuracy.</li>
</ul>
</div>

## 4. Operating Cost

| Cost Type     | DeepSeek-R1               | OpenAI o1                 |
|---------------|---------------------------|---------------------------|
| Cached Input  | $0.14 per million tokens  | $7.50 per million tokens  |
| Input         | $0.55 per million tokens  | $15.00 per million tokens |
| Output        | $2.19 per million tokens  | $60.00 per million tokens |

* DeepSeek-R1 is **significantly cheaper** across all cost categories.
* Example: Output costs for DeepSeek-R1 are **$2.19 per million tokens**, compared to **$60.00 per million tokens** for OpenAI o1.
* This makes DeepSeek-R1 a better option for **cost-sensitive applications**, including large-scale AI projects or startups with limited budgets.

## 5. DeepSeek Deployment Requirements

| Model                         | n_param | weight size | vRAM/ neuron RAM | Speed (response_token/second) |
|-------------------------------|:-------:|:-----------:|:----------------:|:-----------------------------:|
| DeepSeek-R1                   |  671B   |             |    ~1,342 GB     |                               |
| DeepSeek-R1-Distill-Qwen-1.5B |  1.8B   |   1.1 GB    |     ~0.7 GB      |     218.42 (RTX 6000 ada)     |
| DeepSeek-R1-Distill-Qwen-7B   |  7.6B   |   4.7 GB    |     ~3.3 GB      |                               |
| DeepSeek-R1-Distill-Qwen-14B  |  14.8B  |   9.0 GB    |     ~6.5 GB      |                               |
| DeepSeek-R1-Distill-Qwen-32B  |  32.8B  |    19 GB    |     ~14.9 GB     |                               |
| DeepSeek-R1-Distill-Llama-8B  |  8.0B   |   4.9 GB    |     ~3.7 GB      |                               |
| DeepSeek-R1-Distill-Llama-70B |  70.6B  |    42 GB    |    ~32.7 GB      |                               |



