# DEZoomcamp_course_project
![Model](https://github.com/AAKvashnin/DEZoomcamp_course_project/blob/main/Architecture.drawio.png)


Pipeline:
1) Take fraud transaction data from Kaggle https://www.kaggle.com/datasets/jainilcoder/online-payment-fraud-detection
2) Load data to Yandex Cloud Object Storage
3) Load data from Object Storage to DWH schema on Postgres
4) Load data from DWH to DataMart schema on Postgres
5) Visualize DataMart data in Yandex DataLens

Instructions to deploy: