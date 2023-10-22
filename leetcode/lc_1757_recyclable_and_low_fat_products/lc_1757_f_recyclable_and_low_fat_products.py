# SELECT product_id FROM Products
# WHERE low_fats = 'Y' AND recyclable = 'Y';

# Let's do pandas as well
import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products.loc[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y'), ['product_id']]