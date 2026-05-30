
from fastapi import FastAPI
app=FastAPI(title='Telco Churn API')

@app.get('/health')
def health():
    return {'status':'ok'}

@app.get('/')
def root():
    return {'message':'Telco Churn API'}
