# HRMS - Department Module (Simple)

This is a minimal, beginner-friendly Flask project that implements the Department module:
- Add Department
- Edit Department
- Soft-delete (mark inactive)
- Search departments
- Simple dashboard with counts

## Quick start (run locally)

1. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate    # Windows: venv\Scripts\activate
   ```
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Initialize the database:
   ```bash
   export FLASK_APP=app.py       # Windows: set FLASK_APP=app.py
   flask db init
   flask db migrate -m "init"
   flask db upgrade
   ```
4. Run the app:
   ```bash
   python app.py
   ```
5. Open http://127.0.0.1:5000 in your browser.

## Deploying (short)
- Push to GitHub.
- Use Render (https://render.com) or Railway to deploy a Python web service.
- On Render, connect GitHub, set start command `gunicorn wsgi:app`, add environment vars if using Postgres.

## Files included
- app.py, wsgi.py, config.py, models.py
- templates/ (HTML)
- static/ (empty)
- requirements.txt, README.md
