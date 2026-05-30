# Telco Customer Churn MLOps

End-to-end MLOps project using Telco Customer Churn dataset.

## Features
- EDA
- Baseline + Logistic Regression + Random Forest
- FastAPI inference
- Unit tests
- Docker ready
- GitHub Actions CI

## Run
python src/train.py
uvicorn api.app:app --reload
pytest tests/
