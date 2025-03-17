---
title: "Hand on"
date :  "`r Sys.Date()`" 
weight: 2
chapter: false
pre: " <b> 7.2. </b> "
---
Detailed Guide to Deploying the DeepSeek-R1 Model on Amazon Bedrock

![Amazon Bedrock Console](https://aws.amazon.com/bedrock/developer-experience/)

### Introduction

DeepSeek-R1 is an advanced large language model (LLM) developed by DeepSeek AI, now available on Amazon Bedrock Marketplace and Amazon SageMaker JumpStart. This model supports complex tasks such as problem-solving and programming, enabling businesses to seamlessly integrate AI into their applications. This guide provides a step-by-step walkthrough for deploying DeepSeek-R1 on Amazon Bedrock.

### Step 1: Access the Amazon Bedrock Console

1. **Log in to the AWS Management Console**: Use your AWS account credentials to log in.

2. **Navigate to Amazon Bedrock**: In the search bar, type "Bedrock" and select **Amazon Bedrock** from the results.

   ![Search for Amazon Bedrock](https://aws.amazon.com/bedrock/developer-experience/)

3. **Access the Model Catalog**: In the left navigation pane, select **Model catalog** under **Foundation models**.

   ![Model Catalog](https://aws.amazon.com/bedrock/developer-experience/)

4. **Filter and Select DeepSeek-R1**: Use the provider filter to choose **DeepSeek**, then select the **DeepSeek-R1** model.

   ![Select DeepSeek-R1](https://aws.amazon.com/bedrock/developer-experience/)

### Step 2: Deploy the Model

1. **Initiate Deployment**: On the DeepSeek-R1 detail page, click **Deploy**.

2. **Configure Deployment Details**:

   - **Endpoint name**: Enter a name for the endpoint (1-50 alphanumeric characters).

   - **Number of instances**: Specify the number of instances (1-100).

   - **Instance type**: Choose an appropriate instance type. For optimal performance with DeepSeek-R1, it's recommended to use GPU-based instances like `ml.g6.2xlarge`.

     > **Note**: Ensure you have sufficient quotas for the selected instance type.

3. **Advanced Settings (Optional)**:

   - **Deploy within a VPC**: If you wish to deploy within a Virtual Private Cloud (VPC), expand the **Advanced settings** section and configure as needed.

   - **IAM Service Role**: Amazon Bedrock Marketplace automatically creates a service role to access Amazon S3 buckets where the model weights are stored. You can also choose to use an existing role.

     ![Advanced Settings](https://aws.amazon.com/bedrock/developer-experience/)

4. **Complete Deployment**: Click **Deploy** to start the deployment process. This may take a few minutes to complete.

   > **Note**: Once deployed, your model will be available on a real-time endpoint via Amazon SageMaker. Costs will be incurred based on the chosen hardware infrastructure. Refer to [Amazon SageMaker pricing](https://aws.amazon.com/sagemaker-ai/pricing/realtime-endpoint) for more details.

### Step 3: Test the Model in the Playground

1. **Open the Playground**: After deployment, click **Open in playground** to access the interactive interface.

   ![Amazon Bedrock Playground](https://aws.amazon.com/bedrock/developer-experience/)

2. **Experiment with Prompts**: Here, you can test various prompts and adjust model parameters such as `temperature` and `maximum length`.

   > **Tip**: When using DeepSeek-R1 with Bedrock's `InvokeModel` and the Playground Console, it's recommended to use DeepSeek's chat template for optimal results. For example: `<|begin of sentence|><|User|>content for inference<|Assistant|>`.

### Step 4: Perform Inference with Guardrails

1. **Create Guardrails**: You can create guardrails through the Amazon Bedrock console or API. Guardrails help prevent harmful content and assess the model based on safety criteria.

   > **Reference**: See code examples for creating guardrails in the [GitHub repository](https://github.com/aws/amazon-bedrock-samples).

2. **Apply Guardrails**: Use Amazon Bedrock's `ApplyGuardrail` API to apply guardrails to the deployed DeepSeek-R1 model. This process includes:

   - **Input Evaluation**: Assessing user input before sending it to the model.

   - **Output Evaluation**: Assessing the model's output before returning it to the user.

   > **Note**: If the input or output violates the guardrail, the system will return a warning message.

   ![Amazon Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/)

### Step 5: Clean Up

To avoid unintended charges, delete the deployment when it's no longer needed:

1. **Access Marketplace Deployments**: In the Amazon Bedrock console, under **Foundation models**, select **Marketplace deployments**.

2. **Delete the Endpoint**: Locate the endpoint you wish to delete, select it, then choose **Delete** from the **Actions** menu.

3. **Confirm Deletion**: In the confirmation dialog, type `confirm` and click **Delete** to permanently remove the endpoint.

   ![Delete Deployment](https://aws.amazon.com/bedrock/developer-experience/)

### Important Notes

- **Access Permissions**: To deploy DeepSeek-R1, ensure you have access to appropriate instances, such as `ml.g6.2xlarge`.

- **Quotas**: Verify that your account has sufficient quotas for the selected instance type.

- **Safety**: It's advisable to deploy the model with guardrails to ensure safety and compliance with responsible AI policies.

