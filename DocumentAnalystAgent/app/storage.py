import json
import os

summary_store = {}

SUMMARY_FILE = "summary.json"

def get_summary():
    if os.path.exists(SUMMARY_FILE):
        with open(SUMMARY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def update_summary(key: str, val: str):
    summary = get_summary()

    summary[key] = val
    save_summary(summary)
    return summary

def save_summary(summary: dict):
    with open(SUMMARY_FILE, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

def delete_key(key: str):
    summary = get_summary()
    summary.pop(key, None)
    save_summary(summary)
    return summary
    