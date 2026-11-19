from db_connection import engine 

try:
    with engine.connect() as connection:
        print("Successfully connected to MySQL")
except Exception as error:
    print("Database connection failed")
    print(error)