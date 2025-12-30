"""
INSECURE DEMO — Hardcoded password (commonly CWE-798)

This is intentionally insecure.
Fix: load secrets from environment variables or a secrets manager.
"""

import os


# ❌ Insecure: hardcoded credential
DB_PASSWORD = "SuperSecretPassword123"


def connect_insecure():
    # This is just a demo print—do not hardcode secrets in real code.
    return f"Connecting with password length={len(DB_PASSWORD)} (INSECURE)"


def connect_secure():
    # ✅ Better: use environment variable
    pw = os.getenv("DB_PASSWORD")
    if not pw:
        raise RuntimeError("DB_PASSWORD env var not set.")
    return f"Connecting with password length={len(pw)} (SECURE)"


if __name__ == "__main__":
    print(connect_insecure())
    try:
        print(connect_secure())
    except Exception as e:
        print(f"Secure connect blocked: {e}")
