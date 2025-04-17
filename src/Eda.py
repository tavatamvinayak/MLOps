import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def perform_eda(df, output_path='eda_report'):
    # Basic statistics
    print(df.describe())
    
    # Correlation matrix
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.savefig(f'{output_path}/correlation_matrix.png')
    
    # Churn distribution
    plt.figure(figsize=(6, 4))
    sns.countplot(x='churn', data=df)
    plt.savefig(f'{output_path}/churn_distribution.png')

if __name__ == '__main__':
    df = pd.read_csv('data/raw/churn_data.csv')
    perform_eda(df)