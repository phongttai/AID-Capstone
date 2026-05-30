
import json,joblib
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from preprocess import load_clean_data

X,y=load_clean_data('data/WA_Fn-UseC_-Telco-Customer-Churn.csv')
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=0.2,random_state=42)

models={
'baseline':DummyClassifier(strategy='most_frequent'),
'logistic':LogisticRegression(max_iter=5000),
'random_forest':RandomForestClassifier(n_estimators=200,random_state=42)
}
results={}
best=None;best_acc=0
for n,m in models.items():
    m.fit(Xtr,ytr)
    acc=accuracy_score(yte,m.predict(Xte))
    results[n]=float(acc)
    if acc>best_acc:
        best_acc=acc;best=m

joblib.dump(best,'model.joblib')
json.dump(results,open('metrics.json','w'),indent=2)
print(results)
