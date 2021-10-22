from time import sleep
from json import dumps
from kafka import KafkaProducer
import pyEX as p
import os

os.environ['IEX_API_VERSION'] = 'iexcloud-sandbox'

c = p.Client(api_token='Tpk_d1e7ba224d0641f2bd3d2f575148250e', version='stable')

sym='TWTR'

producer = KafkaProducer(bootstrap_servers=['kafka:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

for e in range(1000):
    d = c.quote(symbol=sym)
    print(d)
    data = {'price' : d}
    producer.send('twitterquote', value=data)
    sleep(50)
