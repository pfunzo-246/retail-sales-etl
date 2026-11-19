from sqlalchemy import create_engine
#database connection
username= "root"
password= "" 
host= "localhost"
port= 3308
database= "retail_sales_etl"

#creating database connection
connection_string = (
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
)

engine = create_engine(connection_string)
print("Database connection configured successfully") 