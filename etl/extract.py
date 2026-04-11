import psycopg2
import pandas as pd

# Database connection
conn = psycopg2.connect(
    host="localhost",
    database="sales_db",
    user="postgres",
    password="123456"   # change this
)

# Query
query = "SELECT * FROM sales;"

# Load into DataFrame
df = pd.read_sql(query, conn)

# Print data
print(df.head())
print("\nTotal rows:", len(df))

# Close connection
conn.close()