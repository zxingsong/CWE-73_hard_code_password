"""
FIXED DEMO — CWE-73: External Control of File Name or Path

Mitigations:
- Allowlist permitted filenames
- Ensure resolved path stays inside BASE_DIR
"""

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent / "data"
ALLOWED_FILES = {"public.txt", "help.txt"}


def read_file_safe(user_supplied_name: str) -> str:
    if user_supplied_name not in ALLOWED_FILES:
        raise ValueError("File not allowed")

    target = (BASE_DIR / user_supplied_name).resolve()
    base = BASE_DIR.resolve()

    if base not in target.parents and target != base:
        raise ValueError("Path traversal detected")

    return target.read_text(encoding="utf-8")


if __name__ == "__main__":
    print("CWE-73 demo (fixed)")
    name = input("Enter file name: ").strip()
    try:
        print(read_file_safe(name))
    except Exception as e:
        print(f"Blocked: {e}")
