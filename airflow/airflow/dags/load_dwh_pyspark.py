import pyspark.sql.functions as F
from  pyspark.sql.types import IntegerType
from  pyspark.sql.types import DecimalType
from  pyspark.sql import SaveMode


df=spark.read.csv("/datalake/onlinefraud.csv",header=True)

dwh_df=df.select(F.col("step").cast(IntegerType()).alias("step"), F.col("type"), \
                 F.col("amount").cast(DecimalType(20,2)), F.col("nameOrig"),\
                 F.col("oldbalanceOrg").cast(DecimalType(20,2)).alias("oldbalanceOrig"),\
                 F.col("newbalanceOrig").cast(DecimalType(20,2)),\
                 F.col("nameDest"), F.col("oldbalanceDest").cast(DecimalType(20.2)),\
                 F.col("newbalanceDest").cast(DecimalType(20.2)),\
                 F.col("isFraud").cast(IntegerType()))



dwh_df.write.mode("append").format("jdbc").option("url","jdbc:postgresql://airflow_postgres_1/online_fraud").\
            option("dbtable","dwh.online_transaction").option("user","root").\
            option("password","root").option("driver", "org.postgresql.Driver").option("truncate","false").save()