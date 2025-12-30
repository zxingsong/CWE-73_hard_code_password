"""
FIXED DEMO — CWE-73: External Control of File Name or Path

Mitigation approach:
- Allowlist filenames (best for simple file serving)
- Ensure resolved path stays within BASE_DIR
"""

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent / "data"
ALLOWED_FILES = {"public.txt", "help.txt"}  # ✅ allowlist


def read_file_safe(user_supplied_name: str) -> str:
    # ✅ Strongest simple control: allowlist
    if user_supplied_name not in ALLOWED_FILES:
        raise ValueError("File not allowed.")

    target = (BASE_DIR / user_supplied_name).resolve()

    # ✅ Defense-in-depth: ensure the resolved target stays under BASE_DIR
    base_resolved = BASE_DIR.resolve()
    if base_resolved not in target.parents and target != base_resolved:
        raise ValueError("Path traversal detected.")

    return target.read_text(encoding="utf-8")


if __name__ == "__main__":
    print("CWE-73 demo (fixed). Allowed files:", ", ".join(sorted(ALLOWED_FILES)))
    name = input("Enter file name to read: ").strip()
    try:
        print(read_file_safe(name))
    except Exception as e:
        print(f"Blocked/Error: {e}")
