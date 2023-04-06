# pyspark --packages org.postgresql:postgresql:42.6.0 --driver-memory 4G --executor-memory 4G --num-executors 2
import pyspark.sql.functions as F
from  pyspark.sql.types import IntegerType
from  pyspark.sql.types import DecimalType
from pyspark.sql import SparkSession


df=spark.read.format("jdbc").option("url","jdbc:postgresql:online_fraud").\
                                         option("dbtable","dwh.online_transaction").option("user","root").\
                                         option("password","root").option("driver", "org.postgresql.Driver").load()

datamart_df=df.groupBy(F.col("step"),F.col("type"),F.col("isfraud")).agg(F.sum(F.col("amount")).alias("amount"),\
                                                                         F.count(F.col("step")).alias("cnt"),\
                                                                         F.countDistinct(F.col("nameOrig")).alias("cntDistOrig"),\
                                                                         F.countDistinct(F.col("nameDest")).alias("cntDistDest")\
                                                                         )

datamart_df.write.mode("overwrite").format("jdbc").option("url","jdbc:postgresql:online_fraud").\
            option("dbtable","datamart.agg_trans").option("user","root").\
            option("password","root").option("driver", "org.postgresql.Driver").option("truncate","true").save()