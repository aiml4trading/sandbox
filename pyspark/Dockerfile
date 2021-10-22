FROM jupyter/pyspark-notebook 
COPY kafka2delta.py kafka2delta.py
COPY iex_producer.py iex_producer.py
COPY delta-core_2.12-1.0.0.jar delta-core_2.12-1.0.0.jar
COPY spark-sql-kafka-0-10_2.12-3.1.2.jar spark-sql-kafka-0-10_2.12-3.1.2.jar
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt 
ENTRYPOINT jupyter notebook