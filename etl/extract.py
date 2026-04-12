import psycopg2
import pandas as pd
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def extract():
    print("Starting extraction...")

    conn = psycopg2.connect(
        host="localhost",
        database="sales_db",
        user="postgres",
        password="123456"
    )

    query = "SELECT * FROM sales;"

    df = pd.read_sql(query, conn)

    print(df.head())
    print("\nTotal rows:", len(df))

    conn.close()

    return df