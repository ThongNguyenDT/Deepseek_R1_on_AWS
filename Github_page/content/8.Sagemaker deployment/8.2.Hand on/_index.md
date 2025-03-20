---
title: "Hand on"
date :  "`r Sys.Date()`" 
weight: 2
chapter: false
pre: " <b> 8.2. </b> "
---
**Deploying DeepSeek-R1 on AWS SageMaker: A Step-by-Step Guide**

DeepSeek-R1 is now available on **Amazon SageMaker JumpStart**, making it easy to deploy and integrate into your applications. This guide provides detailed steps for deploying the model on AWS SageMaker, along with cost considerations.  

---

### Deploying DeepSeek-R1 via SageMaker JumpStart

You can deploy the **DeepSeek-R1** model using the **SageMaker JumpStart UI** or via the **SageMaker Python SDK**.

#### Deploying via SageMaker JumpStart UI

1. **Access SageMaker Studio**  
   - Open the **AWS Management Console**, navigate to **SageMaker**, and select **Studio**.  
   - If this is your first time using it, you’ll need to create a **domain**.  

2. **Open JumpStart**  
   - In SageMaker Studio, select **JumpStart** from the navigation panel.  
   - The JumpStart model browser will display available models, including details about providers and capabilities.  

   ![SageMaker JumpStart UI](https://docs.aws.amazon.com/sagemaker/latest/dg/images/studio-jumpstart.png)

3. **Search for DeepSeek-R1**  
   - Use the search bar to find **DeepSeek-R1** and open its model card.  

4. **Review Model Details**  
   The model details page includes:  
   - **Model name**  
   - **Provider information**  
   - **Task category** (e.g., Text Generation)  
   - **Bedrock Ready** badge (if available), indicating compatibility with **Amazon Bedrock**.  

5. **Deploy the Model**  
   - Click **Deploy** to initiate deployment.  

6. **Configure Deployment Settings**  
   - **Endpoint name**: Use the auto-generated name or provide a custom name.  
   - **Instance type**: Select an appropriate instance type (default: `ml.p5e.48xlarge`).  
   - **Instance count**: Specify the number of instances (default: 1).  

   > ⚠️ Choosing the right instance type and count is crucial for balancing cost and performance.  

7. **Review and Deploy**  
   - Double-check all configurations and click **Deploy**.  
   - Deployment can take a few minutes. Once complete, the endpoint status will change to **InService**, indicating it is ready for inference requests.  

---

#### Deploying via SageMaker Python SDK

1. **Install the SageMaker Python SDK**  
   - Ensure you have the necessary AWS permissions and install the SageMaker SDK:  

   ```python
   !pip install --force-reinstall --no-cache-dir sagemaker==2.235.2
   ```

2. **Deploy DeepSeek-R1 using Python**  

   ```python
   from sagemaker.serve.builder.model_builder import ModelBuilder
   from sagemaker.serve.builder.schema_builder import SchemaBuilder
   from sagemaker.jumpstart.model import ModelAccessConfig
   from sagemaker.session import Session
   import logging

   sagemaker_session = Session()
   execution_role_arn = sagemaker_session.get_caller_identity_arn()
   js_model_id = "deepseek-llm-r1"
   gpu_instance_type = "ml.p5e.48xlarge"

   sample_input = {
       "inputs": "Hello, I'm a language model,",
       "parameters": {"max_new_tokens": 128, "top_p": 0.9, "temperature": 0.6},
   }
   sample_output = [{"generated_text": "Hello, I'm a language model, and I'm here to help you with your English."}]

   schema_builder = SchemaBuilder(sample_input, sample_output)
   model_builder = ModelBuilder(
       model=js_model_id,
       schema_builder=schema_builder,
       sagemaker_session=sagemaker_session,
       role_arn=execution_role_arn,
       log_level=logging.ERROR
   )

   model = model_builder.build()
   predictor = model.deploy(model_access_configs={js_model_id: ModelAccessConfig(accept_eula=True)}, accept_eula=True)
   predictor.predict(sample_input)
   ```

3. **Run Additional Inference Requests**  

   ```python
   new_input = {
       "inputs": "What is Amazon doing in Generative AI?",
       "parameters": {"max_new_tokens": 64, "top_p": 0.8, "temperature": 0.7},
   }
   prediction = predictor.predict(new_input)
   print(prediction)
   ```

### Deploying via SageMaker on Neuron

This guide walks through the deployment of DeepSeek-R1-Distill-Llama-70B on an AWS Neuron instance, such as AWS Trainium 2 and AWS Inferentia 2.

#### Prerequisites

Before deploying the model, ensure you meet the following requirements:
- A configured AWS SageMaker Domain.
- Adequate quota in SageMaker (increase the default quota for `ml.inf2.48xlarge` to 1 for endpoint usage).
- A JupyterLab space available for development.

#### Setting Up the SageMaker Session

Instantiate a SageMaker session to determine the current AWS region and execution role:

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

#### Creating the SageMaker Model Object

Define the SageMaker model using the Python SDK:

```python
image_uri = get_huggingface_llm_image_uri("huggingface-neuronx", version="0.0.25")
model_id = "deepseek-ai/DeepSeek-R1-Distill-Llama-70B"
model_name = model_id.split("/")[-1].lower()

# Hub Model Configuration
hub = {
    "HF_MODEL_ID": model_id,
    "HF_NUM_CORES": "24",
    "HF_AUTO_CAST_TYPE": "bf16",
    "MAX_BATCH_SIZE": "4",
    "MAX_INPUT_TOKENS": "3686",
    "MAX_TOTAL_TOKENS": "4096",
}

# Create Hugging Face Model Class
huggingface_model = HuggingFaceModel(
    image_uri=image_uri,
    env=hub,
    role=role,
)
```

#### Deploying the Model to a SageMaker Endpoint

```python
endpoint_name = f"{model_name}-ep"

# Deploy the model to SageMaker Inference
predictor = huggingface_model.deploy(
    endpoint_name=endpoint_name,
    initial_instance_count=1,
    instance_type="ml.inf2.48xlarge",
    container_startup_health_check_timeout=3600,
    volume_size=512,
)
```

#### Testing the Endpoint

```python
response = predictor.predict(
    {
        "inputs": "What is the capital of France?",
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

#### Cleaning Up Resources

Once testing is complete, delete the endpoint to avoid unnecessary costs:

```python
predictor.delete_model()
predictor.delete_endpoint()
```

---

### Deploying on EC2 Neuron with the Hugging Face Neuron Deep Learning AMI

This guide details how to export, deploy, and run DeepSeek-R1-Distill-Llama-70B on an `inf2.48xlarge` AWS EC2 instance.

#### Prerequisites

Before proceeding, ensure:
- You have subscribed to the **Hugging Face Neuron Deep Learning AMI** on the AWS Marketplace.
- You have launched an `inf2.48xlarge` instance in EC2 with this AMI.
- You are connected to the instance via SSH.

If you need guidance on launching an EC2 instance, refer to AWS documentation.

#### Deploying the Model on an EC2 Endpoint

Execute the following command on your EC2 instance to deploy the model:

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

This process will take a few minutes as it downloads the compiled model from the Hugging Face cache and launches a **Text Generation Inference (TGI) endpoint**.

#### Testing the Endpoint

To verify that the model is running correctly, send a test request:

```sh
curl localhost:8080/generate \
    -X POST \
    -d '{"inputs":"Why is the sky dark at night?"}' \
    -H 'Content-Type: application/json'
```

#### Pausing the EC2 Instance

To avoid unnecessary costs, pause or terminate the EC2 instance after testing.


---


### Cost Considerations

Deploying **DeepSeek-R1** on SageMaker incurs several costs:

- **Instance Hours**  
  - Pricing depends on the **instance type** (e.g., `ml.p5e.48xlarge`) and the **number of instances** you use.  
  - High-performance instances have higher costs but provide **lower latency** and handle **larger workloads**.  

- **Custom Model Import**  
  - If you import a **custom model**, charges are based on **5-minute increments** and depend on **model size** and usage.  

- **Data Transfer Fees**  
  - Charges may apply when **transferring data** in and out of SageMaker.  

- **Storage Costs**  
  - You may incur **storage fees** for model artifacts and datasets stored in **Amazon S3**.  

---

### Important Considerations


- **Amazon Bedrock Guardrails**  
  - When deploying DeepSeek-R1, use **Amazon Bedrock Guardrails** to:  
    - Prevent **harmful content generation**.  
    - Evaluate **model safety** using **ApplyGuardrail API** for both input and output filtering.  

- **Avoiding Unexpected Charges**  
  - To prevent unnecessary costs, **delete your SageMaker endpoint** when no longer in use:  

    ```python
    predictor.delete_model()
    predictor.delete_endpoint()
    ```

- **Optimizing Cost vs. Performance**  
  - Adjust **instance type** and **instance count** based on **workload demands** for optimal cost-efficiency.  

