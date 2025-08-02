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

| Layer           | Technology                          |
|----------------|--------------------------------------|
| LLM            | `OpenAI GPT-3.5 Turbo`               |
| Embeddings     | `OpenAIEmbeddings`                   |
| RAG            | `LangChain + FAISS`                  |
| UI             | `Gradio` (chat interface)            |
| Deployment     | Local or Hugging Face Spaces         |

---

💸 **Cost and Hosting Information**

### 🧠 Inference

This POC uses **OpenAI GPT-3.5-Turbo** via API.  
You **must provide your own API key** via a `.env` file.

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
✅ Summary
Component	Service	Free?	Notes
LLM Inference	OpenAI	❌ No	Requires API key and will incur usage cost
Embeddings	OpenAI	❌ No	Included in OpenAI's usage
Vector Store	FAISS	✅ Yes	In-memory, open-source
UI	Gradio	✅ Yes	Free and lightweight
Hosting	Hugging Face	✅ Yes*	Free CPU tier available; good for demos

📁 Data Folder Suggestions (data/)
Include these types of files to make the assistant functional:

jenkinsfile.txt, github-actions.yaml

terraform.tf, infra.md

k8s-deployment.yaml (intentional issues welcome)

pod-logs.txt, cicd-errors.log

best-practices.pdf, readme.md

💬 Sample Prompts for Demo
“Why might this Kubernetes YAML fail to deploy?”

“Explain this GitHub Actions pipeline”

“Summarize these CI/CD logs”

“Generate Terraform for an EC2 instance”

“What’s wrong with this pod log?”

📁 Folder Structure
bash
Copy
Edit
DevOpsYoda/
├── app.py
├── requirements.txt
├── .gitignore
├── .env                  # Not committed
├── README.md
└── data/
    ├── jenkinsfile.txt
    ├── k8s-deployment.yaml
    ├── terraform-snippet.tf
    ├── pod-log.txt
    └── best-practices.pdf
🔧 Run Locally
bash
Copy
Edit
git clone https://github.com/yourusername/DevOpsYoda.git
cd DevOpsYoda
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
Then, create a .env file with your OpenAI key:

bash
Copy
Edit
echo "OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" > .env
Start the app:

bash
Copy
Edit
python app.py
Go to http://127.0.0.1:7860 to interact.

🌍 Optional: Deploy on Hugging Face Spaces
Gradio-based UI works seamlessly on Spaces

Push this repo to your Hugging Face Space

Ensure .env or Secret token is configured (for OpenAI access)

bash
Copy
Edit
git remote add space https://<token>@huggingface.co/spaces/<user>/DevOpsYoda
git push --force space main
📜 License
MIT License – Free to use, fork, or adapt
