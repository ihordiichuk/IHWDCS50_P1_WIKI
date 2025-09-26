# CS50W Project 1 — Wiki

A simple Wikipedia-like encyclopedia built with **Django**, where entries are stored as Markdown files in `entries/` and rendered to HTML.

## Prerequisites

- **Python 3.10+** (3.12 OK)
- **pip** (and optionally `python3 -m venv` for a virtual environment)

> macOS/Linux: use `python3`  
> Windows: use `py`

---

## Quick Start

### 1) Clone your repo

```bash
git clone <YOUR_REPO_URL>
cd <PATH_TO_PROJECT_ROOT>  # contains manage.py, encyclopedia/, entries/, wiki/
```

### 2) Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux
# .venv\Scripts\Activate.ps1 # Windows PowerShell
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Run migrations

```bash
python3 manage.py migrate
```

### 5) Start the server

```bash
# Locally
python3 manage.py runserver

# In CS50 Codespaces
python3 manage.py runserver 0.0.0.0:8000
```

- Locally open: <http://127.0.0.1:8000>  
- In Codespaces: use **Open in Browser** on Port 8000

---

## Dependencies

Minimal `requirements.txt`:

```txt
Django>=4.2
markdown2>=2.4
```

---

## Troubleshooting (Codespaces)

- **CSRF 403 error** → add in `wiki/settings.py`:

```py
CSRF_TRUSTED_ORIGINS = ["https://*.app.github.dev", "https://*.githubpreview.dev"]
```
