# CWE-73 (External Control of File Name or Path) — Python Demo
This repository contains a **small, runnable Python demo** showing:

- ✅ **Vulnerable example** of **CWE-73** (path traversal via user-controlled filename/path)
- ✅ **Fixed example** using an **allowlist + path resolution checks**
- (Optional) A **separate** example of **hardcoded password** (commonly CWE-798 concept) because the repo name mentions it

## What is CWE-73?
**CWE-73: External Control of File Name or Path** occurs when an application uses **user-controlled input**
to build a filename/path **without validating or constraining it**.
Attackers can exploit this to access unintended files (e.g., using `../../` path traversal).

## Why it matters
Impacts can include:
- Reading sensitive files (configuration, credentials, logs)
- Overwriting files (if using write operations)
- Escalating to further compromise depending on what is exposed

---

# Repo Layout

# CWE-73 (External Control of File Name or Path) — Python Demo
This repository contains a **small, runnable Python demo** showing:

- ✅ **Vulnerable example** of **CWE-73** (path traversal via user-controlled filename/path)
- ✅ **Fixed example** using an **allowlist + path resolution checks**
- (Optional) A **separate** example of **hardcoded password** (commonly CWE-798 concept) because the repo name mentions it

## What is CWE-73?
**CWE-73: External Control of File Name or Path** occurs when an application uses **user-controlled input**
to build a filename/path **without validating or constraining it**.
Attackers can exploit this to access unintended files (e.g., using `../../` path traversal).

## Why it matters
Impacts can include:
- Reading sensitive files (configuration, credentials, logs)
- Overwriting files (if using write operations)
- Escalating to further compromise depending on what is exposed

---

# Repo Layout


---

# How to run

## Run the vulnerable CWE-73 demo
From the repo root:
```bash
python src/vulnerable_cwe73.py
