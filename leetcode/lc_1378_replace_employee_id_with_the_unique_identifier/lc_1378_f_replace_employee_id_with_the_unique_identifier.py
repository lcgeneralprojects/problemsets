import pandas as pd


def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    # return pd.merge(employees, employee_uni, how='left', on='id')[['unique_id', 'name']]
    return employees.set_index('id').join(employee_uni.set_index('id'))
