# 🤖 AI App Compiler

> Convert natural language into structured app schema using a 4-stage AI pipeline.

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Live Demo](https://img.shields.io/badge/Live-Demo-green?style=flat)](https://ai-compiler-95kg.onrender.com)

## 🚀 Live Demo
👉 [https://ai-compiler-95kg.onrender.com](https://ai-compiler-95kg.onrender.com)

## ⚙️ How it Works

| Stage | Description |
|-------|-------------|
| 1️⃣ Intent Extraction | Parses user request into structured intent |
| 2️⃣ System Design | Converts intent into app architecture |
| 3️⃣ Schema Generation | Generates UI, API, DB, and Auth schemas |
| 4️⃣ Validation | Validates and fixes inconsistencies |

## 🛠️ Tech Stack
- **Backend:** Python + FastAPI
- **AI:** OpenRouter API
- **Frontend:** HTML/CSS

## 🏃 Run Locally
```bash
pip install fastapi uvicorn requests python-dotenv
uvicorn main:app --port 8080
```

## 📌 Example
**Input:** "Build a CRM with login, contacts, dashboard and role-based access"

**Output:** Complete JSON schema with UI, API, DB, and Auth definitions
