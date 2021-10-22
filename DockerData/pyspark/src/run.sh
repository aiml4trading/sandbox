spark-submit --master "spark://spark:7077" --jars "/home/jovyan/delta-core_2.12-1.0.0.jar,/home/jovyan/spark-sql-kafka-0-10_2.12-3.1.2.jar"  --packages io.delta:delta-core_2.12:1.0.0 --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2 --conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" --conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog" /src/kafka2delta.py 
