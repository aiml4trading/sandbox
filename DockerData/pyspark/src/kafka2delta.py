import pyspark

import os
# os.environ['JAVA_HOME'] = '/usr/lib/jvm/java-11-openjdk-amd64'

from delta import *

spark = pyspark.sql.SparkSession.builder \
    .master("spark://spark:7077") \
    .getOrCreate()

spark.sparkContext.setLogLevel("DEBUG")

df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "twitterquote") \
    .load()

# query1 = df.writeStream \
#     .format("delta") \
#     .outputMode("append") \
#     .start("/tmp/dt_kafka")

query1 = df.writeStream.format("delta").option("checkpointLocation", "/tmp/checkpoint").start("/data/events")
    # .option("checkpointLocation", "/tmp/dt_kafka/_checkpoints/etl-from-json") \

query1.awaitTermination()

