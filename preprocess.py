
import pandas as pd

def load_clean_data(path):
    df=pd.read_csv(path)
    df['TotalCharges']=pd.to_numeric(df['TotalCharges'],errors='coerce')
    df=df.dropna()
    y=(df['Churn']=='Yes').astype(int)
    X=df.drop(['customerID','Churn'],axis=1)
    X=pd.get_dummies(X,drop_first=True)
    return X,y
