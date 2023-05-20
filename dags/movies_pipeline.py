from datetime import datetime, timedelta
from textwrap import dedent
import requests

from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    "movies_pipeline",
    default_args={
        "depends_on_past": False,
        "email": ["airflow@example.com"],
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    description="A simple DAG",
    schedule_interval='@once',
    start_date=datetime.now(),
    catchup=False,
    tags=["movies"],
) as dag:

    t1 = BashOperator(
        task_id="fetch_movies_data",
        bash_command="python /opt/airflow/dags/extract.py",
    )
