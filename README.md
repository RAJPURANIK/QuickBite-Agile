# QuickBite — Food Delivery Demo

A small Flask-based food delivery demo created for an Agile/DevOps assignment. It demonstrates food search, a Git branching and pull-request workflow, automated tests with GitHub Actions, and deployment on Render.

## Features
- Browse a sample menu
- Search menu items by name or category
- Health endpoint at `/health`
- Automated tests using pytest
- GitHub Actions CI on pushes and pull requests

## Run locally
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000.

## Tests
```bash
pytest -v
```

## Render deployment
- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn app:app`

## Agile workflow
Suggested stories: Customer Registration, Customer Login, Search Food, Filter Food by Category, Add Food to Cart, Place Order, View Order Status.
Use a feature branch and pull request for each change, and confirm the CI workflow passes before merging.
