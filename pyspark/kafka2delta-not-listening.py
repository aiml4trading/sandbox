import pyspark

import os
os.environ['JAVA_HOME'] = '/usr/lib/jvm/java-11-openjdk-amd64'

from delta import *

builder = pyspark.sql.SparkSession.builder.appName("MyApp") \
    .master("spark://spark:7077") \
    .config("spark.executor.memory", "2g") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

spark = spark = configure_spark_with_delta_pip(builder).getOrCreate()

spark.sparkContext.setLogLevel("DEBUG")

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

