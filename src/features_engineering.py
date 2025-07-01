import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

CUSTOMER_ID_COL = 'CustomerId'  # update as needed
AMOUNT_COL = 'Amount'           # update as needed
DATETIME_COL = 'TransactionStartTime'  # update as needed

def extract_datetime_features(df):
    df = df.copy()
    df['transaction_datetime'] = pd.to_datetime(df[DATETIME_COL])
    df['transaction_hour'] = df['transaction_datetime'].dt.hour
    df['transaction_day'] = df['transaction_datetime'].dt.day
    df['transaction_month'] = df['transaction_datetime'].dt.month
    df['transaction_year'] = df['transaction_datetime'].dt.year
    return df

def create_aggregate_features(df):
    agg = df.groupby(CUSTOMER_ID_COL).agg(
        total_transaction_amount=(AMOUNT_COL, 'sum'),
        avg_transaction_amount=(AMOUNT_COL, 'mean'),
        transaction_count=(AMOUNT_COL, 'count'),
        std_transaction_amount=(AMOUNT_COL, 'std')
    ).reset_index()
    return agg

class FeatureEngineer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        X = extract_datetime_features(X)
        agg = create_aggregate_features(X)
        X = X.merge(agg, on=CUSTOMER_ID_COL, how='left')
        return X