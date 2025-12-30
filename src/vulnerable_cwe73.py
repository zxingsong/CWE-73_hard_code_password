"""
VULNERABLE DEMO — CWE-73: External Control of File Name or Path

This example is intentionally vulnerable.
It accepts a user-controlled filename and reads from disk without validation,
allowing path traversal (e.g., ../../secrets.txt).
"""

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent / "data"


def read_file(user_supplied_name: str) -> str:
    # ❌ Vulnerable: attacker can supply ../../something to escape BASE_DIR
    target_path = BASE_DIR / user_supplied_name
    return target_path.read_text(encoding="utf-8")


if __name__ == "__main__":
    print("CWE-73 demo (vulnerable).")
    print("Try: public.txt")
    print("Try attack: ../../README.md (or similar)")
    name = input("Enter file name to read: ").strip()
    try:
        print(read_file(name))
    except Exception as e:
        print(f"Error: {e}")
