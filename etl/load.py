from google.cloud import bigquery

def load(df):
    print("Loading data into BigQuery...")

    client = bigquery.Client()

    table_id = "ajay-project-493013.sales_dataset.staging_sales"

    job = client.load_table_from_dataframe(df, table_id)
    job.result()

    print("Data loaded successfully into BigQuery")