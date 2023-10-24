import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    res = pd.merge(visits, transactions, on='visit_id', how='left')
    res = res[res['transaction_id'].isna()].groupby(['customer_id'], as_index=False).count().rename(columns={'visit_id': 'count_no_trans'})

    return res[['customer_id', 'count_no_trans']]
