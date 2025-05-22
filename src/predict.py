import joblib
import numpy as np

model = joblib.load('models/fraud_detector.pkl')

def predict_fraud(data):
    features = np.array([[data['amount'], data['oldbalanceOrg'], data['newbalanceOrig'], data['type']]])
    pred = model.predict(features)
    return 'Fraudulent' if pred[0] == 1 else 'Legitimate'
