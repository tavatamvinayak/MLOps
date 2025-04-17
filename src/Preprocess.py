from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import pandas as pd
import joblib

def preprocess_data(df, train=True, preprocessor=None):
    numeric_features = ['tenure', 'monthly_charges']
    categorical_features = ['contract_type', 'internet_service', 'payment_method']
    
    if train:
        preprocessor = ColumnTransformer(
            transformers=[
                ('num', StandardScaler(), numeric_features),
                ('cat', OneHotEncoder(drop='first', sparse=False), categorical_features)
            ])
        
        X = preprocessor.fit_transform(df[numeric_features + categorical_features])
        joblib.dump(preprocessor, 'models/preprocessor.pkl')
    else:
        X = preprocessor.transform(df[numeric_features + categorical_features])
    
    y = df['churn'].values if train else None
    return X, y, preprocessor

if __name__ == '__main__':
    df = pd.read_csv('data/raw/churn_data.csv')
    X, y, preprocessor = preprocess_data(df)
    pd.DataFrame(X).to_csv('data/processed/X_train.csv', index=False)
    pd.Series(y).to_csv('data/processed/y_train.csv', index=False)