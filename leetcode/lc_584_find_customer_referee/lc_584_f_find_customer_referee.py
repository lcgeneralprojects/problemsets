# # Write your MySQL query statement below
# SELECT name FROM Customer
# WHERE referee_id <> 2 OR referee_id IS NULL

# Let's try pandas
import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    return customer.loc[(customer['referee_id'].isna()) | (customer['referee_id'] != 2), ['name']]