from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from etl.extract import extract
from etl.transform import transform
from etl.load import load, run_merge
from etl.validate import validate


def run_pipeline():
    df = extract()
    df = validate(df)
    df = transform(df)
    load(df)
    run_merge()


dag = DAG(
    'sales_pipeline',
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False
)

run_etl_task = PythonOperator(
    task_id='run_etl',
    python_callable=run_pipeline,
    dag=dag
)