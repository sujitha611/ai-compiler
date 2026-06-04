# AI App Compiler

Convert natural language into structured app schema using a 4-stage AI pipeline.

## How it works
1. **Stage 1 - Intent Extraction**: Parses user request into structured intent
2. **Stage 2 - System Design**: Converts intent into app architecture  
3. **Stage 3 - Schema Generation**: Generates UI, API, DB, and Auth schemas
4. **Stage 4 - Validation**: Validates and fixes inconsistencies

## Tech Stack
- Python + FastAPI (Backend)
- OpenRouter API (AI)
- HTML/CSS (Frontend)

## Run Locally
```bash
pip install fastapi uvicorn requests python-dotenv
uvicorn main:app --port 8080
```

## Example Output
Input: "Build a CRM with login, contacts, dashboard and role-based access"
Output: Complete JSON schema with UI, API, DB, and Auth definitions
