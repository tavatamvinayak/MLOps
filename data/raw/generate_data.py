
import pandas as pd
import numpy as np

np.random.seed(42)
n_samples = 10000

data = {
    'customer_id': range(1, n_samples + 1),
    'tenure': np.random.randint(1, 72, n_samples),
    'monthly_charges': np.random.uniform(20, 120, n_samples),
    'contract_type': np.random.choice(['Month-to-month', 'One year', 'Two year'], n_samples),
    'internet_service': np.random.choice(['DSL', 'Fiber optic', 'No'], n_samples),
    'payment_method': np.random.choice(['Electronic check', 'Mailed check', 'Bank transfer', 'Credit card'], n_samples),
    'churn': np.random.choice([0, 1], n_samples, p=[0.73, 0.27])
}
df = pd.DataFrame(data)
df.to_csv('data/raw/churn_data.csv', index=False)
