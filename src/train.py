import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, roc_auc_score
import pandas as pd
import joblib
from preprocess import preprocess_data

def train_model():
    df = pd.read_csv('data/raw/churn_data.csv')
    X, y, preprocessor = preprocess_data(df)
    
    mlflow.set_experiment("churn_prediction")
    
    with mlflow.start_run():
        # Hyperparameter tuning
        param_grid = {
            'n_estimators': [100, 200],
            'max_depth': [5, 10, None],
            'min_samples_split': [2, 5]
        }
        
        model = RandomForestClassifier(random_state=42)
        grid_search = GridSearchCV(model, param_grid, cv=5, scoring='roc_auc')
        grid_search.fit(X, y)
        
        best_model = grid_search.best_estimator_
        
        # Metrics
        y_pred = best_model.predict(X)
        accuracy = accuracy_score(y, y_pred)
        roc_auc = roc_auc_score(y, best_model.predict_proba(X)[:, 1])
        
        # Log to MLflow
        mlflow.log_params(grid_search.best_params_)
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("roc_auc", roc_auc)
        mlflow.sklearn.log_model(best_model, "model")
        
        # Save model
        joblib.dump(best_model, 'models/model.pkl')
        
        return best_model, preprocessor

if __name__ == '__main__':
    train_model()