---
title: DevOpsYoda – AI Agent for DevOps
emoji: 🧠
colorFrom: green
colorTo: gray
sdk: gradio
sdk_version: "3.50.2"
app_file: app.py
pinned: false
---
# DevOpsYoda
> ⚙️ **Note**: The section above is required for Hugging Face Spaces deployment. It defines the Space metadata including title, emoji, colors, SDK type/version, and the entry-point script (`app.py`). Without it, the Space will fail to build.

# 🧠 DevOpsYoda – AI Agent for DevOps Wisdom

**DevOpsYoda** is a smart AI assistant that simulates DevOps support by answering infrastructure-related questions, analyzing CI/CD config files, troubleshooting Kubernetes manifests, and more — all through natural language queries.

---

## 🚀 What This POC Demonstrates (AI Capabilities)

- 🔍 **RAG-based Q&A** over:
  - Jenkinsfiles, GitHub Actions YAMLs
  - Kubernetes manifests (Helm, YAML)
  - Terraform and infra-as-code snippets
  - Markdown/PDF documentation
  - CI/CD logs and failure traces

- 🧠 **AI Assistant Capabilities**:
  - Explains DevOps config files
  - Diagnoses likely issues in YAML or Dockerfiles
  - Suggests remediations or security best practices
  - Summarizes pod or pipeline failure logs
  - Can be extended to generate code (e.g., Terraform)

- 🤖 **Agentic Reasoning** *(via LangChain Agent)*:
  - Selects the right tool based on task (log summarizer, YAML linter, etc.)
  - Multi-step thinking possible with agent tools

---

## 🧪 Enhanced POC Use Case: "Ask Me Anything About Your Infra"

A developer can interact with this chatbot to:
- Debug YAML misconfigurations
- Understand CI/CD automation flows
- Validate security posture of infra setup
- Generate code snippets or summaries
- Retrieve answers from private DevOps documentation

---

## 🛠️ Tech Stack Used

| Layer           | Technology                                                 |
|----------------|-------------------------------------------------------------|
| LLM            | `mistralai/Mistral-7B-Instruct-v0.1` or `google/flan-t5-xl` |
| Embeddings     | `sentence-transformers/all-MiniLM-L6-v2`                    |
| RAG            | `LangChain + FAISS`                                         |
| Agentic Flow   | `LangChain Agents + Toolset`                                |
| UI             | `Gradio` (chat interface)                                   |
| Deployment     | `Hugging Face Spaces` (completely free tier)                |

---

## 📁 Data Folder Suggestions (`data/`)

Include these types of files to make the assistant functional:

- `jenkinsfile.txt`, `github-actions.yaml`  
- `terraform.tf`, `infra.md`  
- `k8s-deployment.yaml` (intentional issues welcome)  
- `pod-logs.txt`, `cicd-errors.log`  
- `best-practices.pdf`, `readme.md`  

---

## 💬 Sample Prompts for Demo

- “Why might this Kubernetes YAML fail to deploy?”
- “Explain this GitHub Actions pipeline”
- “Summarize these CI/CD logs”
- “Generate Terraform for an EC2 instance”
- “What’s wrong with this pod log?”

---

## 📁 Folder Structure

DevOpsYoda/
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
└── data/
├── jenkinsfile.txt
├── k8s-deployment.yaml
├── terraform-snippet.tf
├── pod-log.txt
└── best-practices.pdf


---

## 🔧 Run Locally

```bash
git clone https://github.com/yourusername/DevOpsYoda.git
cd DevOpsYoda
pip install --break-system-packages -r requirements.txt
python3 app.py

🌍 Deploy on Hugging Face (Free)
Go to https://huggingface.co/spaces

Create a new Space → Choose Gradio

Clone the repo into the Space or push via:

git remote add space https://<token>@huggingface.co/spaces/<user>/DevOpsYoda
git push --force space main

Set your OPENAI_API_KEY or use a free LLM like flan-t5-xl

📜 License
MIT License


