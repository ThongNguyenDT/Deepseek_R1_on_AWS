import os
import re
from datetime import datetime


def parse_md_input(md_input):
    lines = md_input.strip().split('\n')
    structure = []
    stack = []
    for line in lines:
        match = re.match(r'^(\d+\.(.*))\s+(.*)', line.strip())
        if match:
            number = line.strip().split(' ')[0].strip()
            name = line.strip()[len(number) + 1:].strip()
            level = number.count('.')
            while stack and stack[-1]['level'] >= level:
                stack.pop()

            entry = {'number': number, 'name': name, 'children': [], 'level': level}

            if stack:
                stack[-1]['children'].append(entry)
            else:
                structure.append(entry)

            stack.append(entry)
    return structure


def create_folders(base_path, structure, md=True):
    for item in structure:
        name = item['name']
        if item['name'][-1] == '?': name = item['name'][:-1]
        folder_path = os.path.join(base_path, f"{item['number']}{name}")
        os.makedirs(folder_path, exist_ok=True)
        if md:
            create_md_files(folder_path, item['name'], item['number'])

        if item['children']:
            create_folders(folder_path, item['children'], md)


def create_md_files(folder_path, title, number):
    content = f"""---
title: "{title}"
date :  "`r Sys.Date()`" 
weight: {number.split('.')[-2]}
chapter: false
pre: " <b> {number} </b> "
---
Coming soon"""

    for lang in ['_index.md', '_index.vi.md']:
        with open(os.path.join(folder_path, lang), 'w', encoding='utf-8') as f:
            f.write(content)


if __name__ == "__main__":
    md_input = """
    0. Homepage
    1. Introduction
    2. Distill information
    3. Local deployment
    4. Interface
        4.1. web chat
        4.2. mobile app
    5. vLLM deployment
    5.1. About vLLM
    5.2. Hand on
    6. vLLM with Neuron
    6.1. About AWS Neuron
    6.2. Hand on
    7. Bedrock deployment
    7.1. Why Bedrock?
    7.2. Hand on
    8. Sagemaker deployment
    8.1. why need Sagemaker?
    8.2. Hand on
    9. EKS deployment
    9.1. Why need EKS?
    9.2. Hand On
    10. RAG with Opensearch
    10.1. What is RAG?
    10.2. How To use Deepseek as RAG?
    10.3. Hand on
    11. Agent
    11.1. What is agent?
    11.2. sample agent
    12. ECS deployment
    """

    base_path = "./static"
    os.makedirs(base_path, exist_ok=True)
    structure = parse_md_input(md_input)
    create_folders(base_path, structure, False)
    print("Folder structure and markdown files generated successfully!")
