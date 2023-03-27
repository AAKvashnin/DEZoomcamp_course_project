from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator
import kaggle

def download_dataset(ds:str, dwpath:str, filename:str,**context):
 kaggle.api.dataset_download_files(ds,dwpath,force=True,unzip=True)

with DAG(dag_id='dag',
         default_args={'owner': 'airflow'},
         schedule_interval='@daily', # Интервал запусков
         start_date=days_ago(1) # Начальная точка запуска
    ) as dag:

   extract_data = PythonOperator(
           task_id='extract_data',
           python_callable=download_dataset,
           op_kwargs={
               'ds': 'jainilcoder/online-payment-fraud-detection',
               'dwpath': '/tmp',
               'filename':'onlinefraud.csv'}
       )
   extract_data