import pandas as pd
from db_connection import engine

sales_data = pd.read_csv("data/clean_sales.csv")

sales_data.to_sql(
    name="sales",
    con=engine,
    if_exists="append",
    index=False
)

print("Sales data successfully loaded into MySQL") 