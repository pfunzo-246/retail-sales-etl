import pandas as pd

#extracting files from csv
sales_data = pd.read_csv("data/sales.csv")

#display sales data
print(sales_data)

#checking the data quality
#identifying missing values
print("\nChecking for missing values:")
print(sales_data.isnull().sum())

#identifying duplicate records
print("\nChecking for duplicate records:")
print(sales_data.duplicated().sum()) 

#identifying data types
print("\nChecking data types:")
print(sales_data.dtypes)

#changing order date into datetime format
sales_data["order_date"] = pd.to_datetime(sales_data["order_date"])

print("\nChecking updated data types:")
print(sales_data.dtypes) 

#calculate total sales amount
sales_data["total_amount"] = sales_data["quantity"] * sales_data["unit_price"]

print("\nSales data with total amount")
print(sales_data[["order_id", "product", "quantity", "unit_price", "total_amount"]])

#calculate total revenue
total_revenue = sales_data["total_amount"].sum()

print("\nTotal Sales Revenue:")
print(f"R{total_revenue:,.2f}")

#saving the changed sales data
sales_data.to_csv("data/clean_sales.csv", index=False)

print("\nCleaned sales data saved successfully!") 