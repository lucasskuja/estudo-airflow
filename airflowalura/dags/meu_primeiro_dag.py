from airflow.models import DAG
from airflow.utils.date import days_ago

with DAG(
    dag_id = 'meu_primeiro_dag',
    start_date = days_ago(1),
    schedule_interval = '@daily'
) as dag:
    