FROM python:3.8
# WORKDIR /opt/application/
# ENV PYSPARK_MAJOR_PYTHON_VERION=3
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt 
RUN pyspark --packages io.delta:delta-core_2.12:1.0.0 --conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" --conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog"
ENTRYPOINT pyspark