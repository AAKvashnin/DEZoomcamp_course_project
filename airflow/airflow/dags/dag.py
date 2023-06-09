from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator
import kaggle
from pathlib import Path
import boto3


def download_dataset(ds:str, dwpath:str, filename:str,**context):
    kaggle.api.dataset_download_files(ds,dwpath,force=True,unzip=True)

def write_cloud(dwpath:str, filename:str, bucket:str, **context):
    path = Path(f"{dwpath}/{filename}")
    session = boto3.session.Session()
    s3 = session.client(
        service_name='s3',
        endpoint_url='https://storage.yandexcloud.net'
    )
    s3.upload_file(path.as_posix(), bucket, path.as_posix())

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

   load_datalake = PythonOperator(
           task_id='load_datalake',
           python_callable=write_cloud,
           op_kwargs={
                'dwpath': '/tmp',
                'filename':'onlinefraud.csv',
                'bucket':'dtc-data-lake'}
       )

   load_dwh=SparkSubmitOperator(
           application='/usr/local/airflow/dags/load_dwh_pyspark.py',
           task_id='load_dwh',
           conn_id='spark_local',
           packages='org.postgresql:postgresql:42.6.0'
       )

   load_datamart=SparkSubmitOperator(
              application='/usr/local/airflow/dags/load_datamart_pyspark.py',
              task_id='load_datamart',
              conn_id='spark_local',
              packages='org.postgresql:postgresql:42.6.0'
          )

   extract_data >> load_datalake >> load_dwh >> load_datamart