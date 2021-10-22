import pyspark

import os
os.environ['JAVA_HOME'] = '/usr/lib/jvm/java-11-openjdk-amd64'

from delta import *

spark = pyspark.sql.SparkSession.builder \
    .master("spark://spark:7077") \
    .setLogLevel("DEBUG")
    .getOrCreate()


df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "twitterquote") \
    .load()


query1 = df.writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", "/tmp/dt_kafka/_checkpoints/etl-from-json") \
    .start("/tmp/dt_kafka")

