# DEZoomcamp_course_project
![Model](https://github.com/AAKvashnin/DEZoomcamp_course_project/blob/main/Architecture.drawio.png)


Pipeline:
1) Take fraud transaction data from Kaggle https://www.kaggle.com/datasets/jainilcoder/online-payment-fraud-detection
2) Load data to Yandex Cloud Object Storage
3) Load data from Object Storage to DWH schema on Postgres
4) Load data from DWH to DataMart schema on Postgres
5) Visualize DataMart data in Yandex DataLens

Scripts:
 airflow - docker config
 terraform - configs for Yandex cloud resources
 airflow/pgscript - initial script to create tables (DWH and datamart)
 airflow/dags - airflow dag and pySpark applications

Instructions to deploy:
1) Deploy cloud infrastructure - bucket + compute virtual machine
2) Start virtual machine, connect via ssh
3) git clone https://github.com/AAKvashnin/DEZoomcamp_course_project
4) Configure secrets (.s3fs, .kaggle, .aws)
5) Inside virtual machine install s3fs (apt-get install s3fs)
6) Mount s3fs folder
s3fs dtc-data-lake /zoomcamp/zoomcamp/datalake -o passwd_file=$HOME/.passwd-s3fs -o url=https://storage.yandexcloud.net
7) Build & start docker (docker-compose build --no-cache && docker-compose up)
8) Wait docker to start
9) Connect airflow and configure spark_local Connection
10) Connect airflow and start dag, wait until its completion (port 8081 of virtual machine)
11) Open Data Lens and see the results ()