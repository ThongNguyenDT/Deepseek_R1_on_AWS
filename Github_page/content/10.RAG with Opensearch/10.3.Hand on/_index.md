---
title: "Hand on"
date :  "`r Sys.Date()`" 
weight: 3
chapter: false
pre: " <b> 10.3. </b> "
---


**_Deploying DeepSeek-R1 Distill with Amazon OpenSearch Service and Amazon SageMaker for RAG Applications_**

This guide provides a detailed walkthrough on deploying **DeepSeek-R1 Distill** as a **Retrieval-Augmented Generation (RAG)** application using **Amazon OpenSearch Service** in combination with **Amazon SageMaker**. Python scripts, CLI tools, and IAM configurations are employed to ensure a professional, well-structured, and easy-to-understand deployment, with precise technical terminology.

---

### 1. Prerequisites

- **Git:** Required for cloning the sample repository:
  ```bash
  git clone https://github.com/Jon-AtAWS/opensearch-examples.git
  ```
- **Python:** Use Python 3.13. Create a virtual environment to manage dependencies.
- **AWS Account:** Must have permissions to create an OpenSearch Service domain and set up a SageMaker endpoint.
- **IDE:** Visual Studio Code or a similar IDE for development and source code management.
- **AWS CLI or Boto3:** AWS CLI must be configured with valid credentials.

---

### 2. Deploying DeepSeek on Amazon SageMaker

- Deploy the **DeepSeek-R1** model on SageMaker to create an inference endpoint.
- Refer to the document “Deploying DeepSeek-R1 Distill Model on AWS using Amazon SageMaker AI” for detailed configuration, requirements, and deployment steps.

---

### 3. Creating an Amazon OpenSearch Service Domain

An **OpenSearch Service domain** is equivalent to an OpenSearch cluster. Domains include configurations, instance types, instance counts, and storage resources specified by the user. Domains can be created via the AWS console, AWS CLI, or AWS SDKs.

#### Steps to create an OpenSearch Service domain via the console:

1. Go to https://aws.amazon.com and click **Sign In to the Console**.
2. Under **Analytics**, select **Amazon OpenSearch Service**.
3. Click **Create domain**.
4. Name the domain (e.g., `movies` used in this guide).
5. Choose the **Standard create** method.
   - **Note:** For a quick production setup with best practices, select **Easy create**. This guide uses **Standard create** for development and testing.
6. Select the **Dev/test** template.
7. Choose the **Domain with standby** deployment option.
8. Select the latest OpenSearch version.
9. Skip **Data nodes**, **Warm and cold data storage**, **Dedicated master nodes**, **Snapshot configuration**, and **Custom endpoint** settings for this guide.
10. For simplicity, choose **Public access** under **Network** settings.
11. Under **Fine-grained access control**, enable it and set up a **Master user** with a username and password.
12. Skip **SAML authentication** and **Amazon Cognito authentication**.
13. Under **Access policy**, select **Only use fine-grained access control**. Fine-grained access control will handle authentication instead of a domain access policy.
14. Skip other settings and click **Create**.
    - Domain creation typically takes 15–30 minutes, depending on the configuration.
    - Once the domain is created, select it to view the configuration details. Note down the **domain endpoint** under **General information** (e.g., `https://search-my-domain.us-east-1.es.amazonaws.com`) for later use.
- After creation, save the **Amazon Resource Name (ARN)** and **Endpoint URL** for use in subsequent steps.

---

### 4. Downloading and Preparing the Codebase

Perform the following steps in your local environment:

1. **Clone the repository and navigate to the project folder:**
   ```bash
   cd opensearch-examples/opensearch-deepseek-rag
   ```

2. **Create a virtual environment and install dependencies:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   Update the following variables with appropriate values:
   ```bash
   export DEEPSEEK_AWS_REGION='<your AWS region>'
   export SAGEMAKER_MODEL_INFERENCE_ARN='<SageMaker endpoint ARN>'
   export SAGEMAKER_MODEL_INFERENCE_ENDPOINT='<SageMaker endpoint URL>'
   export OPENSEARCH_SERVICE_DOMAIN_ARN='<OpenSearch domain ARN>'
   export OPENSEARCH_SERVICE_DOMAIN_ENDPOINT='<OpenSearch API endpoint>'
   export OPENSEARCH_SERVICE_ADMIN_USER='<admin username>'
   export OPENSEARCH_SERVICE_ADMIN_PASSWORD='<admin password>'
   ```

The codebase is organized into separate Python scripts for easy navigation and maintenance.

---

### 5. Setting Up IAM Roles

#### 5.1. Role Allowing OpenSearch to Invoke SageMaker Endpoint

- Check the `create_invoke_role.py` file.
- Run the script:
  ```bash
  python create_invoke_role.py
  ```
- Save the role ARN and configure the environment variable `INVOKE_DEEPSEEK_ROLE` as instructed by the script.

#### 5.2. Role Allowing Users to Create Connectors in OpenSearch

- Check the `create_connector_role.py` file.
- Run the script:
  ```bash
  python create_connector_role.py
  ```
- Save the role ARN and configure the environment variable `CREATE_DEEPSEEK_CONNECTOR_ROLE`.

#### 5.3. Configuring Security for OpenSearch Service

- Check the `setup_opensearch_security.py` file.
- Run the script:
  ```bash
  python setup_opensearch_security.py
  ```
- This sets up fine-grained access control, mapping IAM roles to `ml_full_access` permissions.

---

### 6. Creating a Connector

The connector defines a connection from OpenSearch to the inference endpoint on SageMaker.

1. Check `create_connector.py`.
2. Run the script:
   ```bash
   python create_connector.py
   ```
3. Save the `DEEPSEEK_CONNECTOR_ID` from the output.

---

### 7. Creating an OpenSearch Model

1. Check `create_deepseek_model.py`.
2. Run the script:
   ```bash
   python create_deepseek_model.py
   ```
3. Save the `DEEPSEEK_MODEL_ID` from the output.

---

### 8. Verifying the Setup

1. Log in to **OpenSearch Dashboards** using the domain console URL and admin credentials.
2. In **Dev Tools**, run the following command:
   ```json
   POST _plugins/_ml/models/<your model ID>/_predict
   {
     "parameters": {
       "inputs": "Hello"
     }
   }
   ```
3. Verify the response to confirm model functionality.

---

### 9. Setting Up the RAG Pipeline

- **RAG:** Integrates knowledge base retrieval with LLM prompting.
- **Search Pipelines:** Uses hybrid search, reranking, and RAG within OpenSearch.
- Vector search via k-NN is enabled for semantic retrieval.

---

### 10. Running RAG Queries

1. Check `run_rag.py`.
2. Run the script:
   ```bash
   python run_rag.py
   ```
3. The output includes retrieved documents and DeepSeek-generated responses.

---

### 11. Cleaning Up Resources

- Delete SageMaker endpoints, CloudFormation stacks, and OpenSearch domains to avoid unnecessary costs.