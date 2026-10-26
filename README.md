# AI App Compiler — Natural Language to Full-Stack Application Schema Pipeline

[![Live Demo](https://img.shields.io/badge/Render-Live_Demo-green?style=flat&logo=render)](https://ai-compiler-95kg.onrender.com)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat&logo=python)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-009688?style=flat&logo=fastapi)](https://fastapi.tiangolo.com)
[![OpenRouter](https://img.shields.io/badge/OpenRouter-API-blueviolet?style=flat)](https://openrouter.ai/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An agentic multi-stage LLM compilation pipeline that translates high-level natural language application descriptions into deterministic, production-ready system schemas covering UI layout, REST endpoints, database tables, and role-based access control.

---

## 🚀 Live Deployment
- **Live URL:** [https://ai-compiler-95kg.onrender.com](https://ai-compiler-95kg.onrender.com)

---

## 💡 How It Works (The 4-Stage Pipeline)

Rather than asking an LLM to generate an entire application in one shot—which frequently suffers from hallucinations, missing foreign keys, or incomplete specifications—**AI App Compiler** executes a chained 4-stage pipeline where each stage builds upon and refines the previous stage's structured output:

```mermaid
flowchart TD
    UserPrompt["Natural Language Prompt\n(e.g., 'Build a CRM with leads, team roles & reports')"] --> Stage1

    subgraph Pipeline["4-Stage LLM Compilation Engine"]
        Stage1["Stage 1: Intent Extraction\n• App Type\n• High-Level Features\n• User Roles & Entities"]
        Stage2["Stage 2: Architectural System Design\n• Frontend Pages\n• API Route Contracts\n• Database Tables & Keys\n• Auth Permissions Matrix"]
        Stage3["Stage 3: Full-Stack Schema Synthesis\n• ui_schema\n• api_schema\n• db_schema\n• auth_schema"]
        Stage4["Stage 4: Validation & Self-Correction\n• Structural Consistency\n• Foreign Key Integrity\n• JSON Schema Compliance"]

        Stage1 --> Stage2
        Stage2 --> Stage3
        Stage3 --> Stage4
    end

    Stage4 --> FinalOutput[("Validated Application Schema\n(JSON Specification)")]
```

---

## 🛠️ Architecture & Technologies

- **Backend Framework**: [FastAPI](https://fastapi.tiangolo.com) with asynchronous routing and [Pydantic](https://docs.pydantic.dev) validation contracts.
- **LLM Gateway**: [OpenRouter API](https://openrouter.ai/) supporting multi-model execution and high-concurrency requests.
- **Frontend Playground**: Zero-dependency dark-mode web console with real-time JSON syntax-highlighted schema inspector.
- **Environment & Secrets**: `python-dotenv` with strict `.gitignore` isolation preventing accidental credential exposure.

---

## 📁 Repository Structure

```text
ai-compiler/
├── templates/
│   └── index.html      # Dark-mode interactive web playground
├── .env.example        # Safe template for environment variables
├── .gitignore          # Excludes .env, pycache, and virtual environments
├── main.py             # FastAPI entrypoint serving web UI and /generate API
├── pipeline.py         # 4-stage prompt chaining and OpenRouter integration
└── requirements.txt    # Python runtime dependencies
```

---

## 🚀 Quick Start

### 1. Clone & Set Up Virtual Environment

```bash
git clone https://github.com/sujitha611/ai-compiler.git
cd ai-compiler

python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file based on the template:

```bash
cp .env.example .env
```

Edit `.env` and add your OpenRouter API key:

```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

### 4. Run the Application

```bash
python main.py
```

The web console will be available at **`http://localhost:8000`**.

---

## 🔌 API Reference

### Generate Schema
- **Endpoint**: `POST /generate`
- **Headers**: `Content-Type: application/json`
- **Request Body**:
  ```json
  {
    "prompt": "Build an inventory management system with warehouses, low-stock alerts, and manager vs clerk permissions"
  }
  ```
- **Response**:
  ```json
  {
    "success": true,
    "output": {
      "ui_schema": { "pages": [...] },
      "api_schema": { "endpoints": [...] },
      "db_schema": { "tables": [...] },
      "auth_schema": { "roles": [...] }
    }
  }
  ```

---

## 👤 Author

**Battu Jaya Sujitha**
- GitHub: [@sujitha611](https://github.com/sujitha611)
- Repository: [ai-compiler](https://github.com/sujitha611/ai-compiler)
