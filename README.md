# Event Registration Service

Simple FastAPI-based event registration service.


Run locally:

```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows PowerShell
# .\.venv\Scripts\Activate.ps1
pip install -r src/requirements.txt
uvicorn src.main:app --reload
```

Docker:

```bash
docker build -t serc-app .
docker run -p 8000:8000 serc-app
```

API endpoints:
- `GET /health`
- `POST /register` - JSON body per `src/schemas.py`
- `GET /registrations`
- `GET /registrations/{id}`
# VBIT-FDP
Dev program for fac
