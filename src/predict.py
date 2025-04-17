import joblib
import pandas as pd
from preprocess import preprocess_data

def make_prediction(input_data):
    model = joblib.load('models/model.pkl')
    preprocessor = joblib.load('models/preprocessor.pkl')
    
    df = pd.DataFrame([input_data])
    X, _, _ = preprocess_data(df, train=False, preprocessor=preprocessor)
    
    prediction = model.predict_proba(X)[:, 1]
    return prediction[0]