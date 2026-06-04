import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

def call_ai(prompt):
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "nvidia/nemotron-3-super-120b-a12b:free",
            "messages": [{"role": "user", "content": prompt}]
        }
    )
    data = response.json()
    print("API Response:", data)
    if "choices" not in data:
        raise Exception(str(data))
    text = data["choices"][0]["message"]["content"].strip()
    if text.startswith("```"):
        text = text.split("```")[1]
        if text.startswith("json"):
            text = text[4:]
    return text.strip()

def stage1_intent(user_prompt):
    prompt = f"""Extract the intent from this app request. Return ONLY valid JSON, nothing else.
{{"app_type": "", "features": [], "roles": [], "entities": []}}
Request: {user_prompt}"""
    return json.loads(call_ai(prompt))

def stage2_design(intent):
    prompt = f"""Create system design. Return ONLY valid JSON, nothing else.
{{"pages": [], "api_endpoints": [], "database_tables": [], "auth_roles": []}}
Intent: {json.dumps(intent)}"""
    return json.loads(call_ai(prompt))

def stage3_schema(intent, design):
    prompt = f"""Generate complete app schema. Return ONLY valid JSON, nothing else.
{{"ui_schema": {{}}, "api_schema": {{}}, "db_schema": {{}}, "auth_schema": {{}}}}
Intent: {json.dumps(intent)}
Design: {json.dumps(design)}"""
    return json.loads(call_ai(prompt))

def stage4_validate(schema):
    prompt = f"""Validate and fix this schema. Return ONLY valid JSON with same structure, nothing else.
Schema: {json.dumps(schema)}"""
    return json.loads(call_ai(prompt))

def run_pipeline(user_prompt):
    try:
        print("Stage 1: Intent Extraction...")
        intent = stage1_intent(user_prompt)
        print("Stage 2: System Design...")
        design = stage2_design(intent)
        print("Stage 3: Schema Generation...")
        schema = stage3_schema(intent, design)
        print("Stage 4: Validation...")
        final = stage4_validate(schema)
        return {"success": True, "output": final}
    except Exception as e:
        return {"success": False, "error": str(e)}