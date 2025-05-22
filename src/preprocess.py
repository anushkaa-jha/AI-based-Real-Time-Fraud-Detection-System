import pandas as pd

def preprocess_data(df):
    df = df.copy()
    df['type'] = df['type'].astype('category').cat.codes
    features = ['amount', 'oldbalanceOrg', 'newbalanceOrig', 'type']
    X = df[features]
    y = df['isFraud']
    return X, y
