from google.cloud import bigquery
import logging

def load(df):
    logging.info("Loading to BigQuery started")

    client = bigquery.Client()

    table_id = "ajay-project-493013.sales_dataset.staging_sales"

    job = client.load_table_from_dataframe(df, table_id)
    job.result()

    print("Data loaded successfully into BigQuery")
    logging.info("Data loaded to staging")

def run_merge():
    print("Running MERGE...")
    logging.info("Merge started")

    client = bigquery.Client()

    query = open("sql/merge.sql").read()

    job = client.query(query)
    job.result()

    print("Merge completed")
    logging.info("Merge completed")

