import json, time
from kafka import KafkaProducer
from kafka.errors import KafkaError
from random import uniform

producer = KafkaProducer(bootstrap_servers=['172.24.41.211:8080'], 
						 value_serializer=lambda v: json.dumps(v).encode('utf-8'))
while True:
	producer.send('parqueadero_centro', {'time': time.strftime("%X"), 'Tipo': 'moto',’Disponibilidad’: true, ‘Valor’: ‘3500’, ‘id’:’1111’ )
producer.send('parqueadero_centro', {'time': time.strftime("%X"), 'Tipo': 'carro',’Disponibilidad’: true, ‘Valor’: ‘3500’, ‘id’:’1112’ )
producer.send('parqueadero_centro', {'time': time.strftime("%X"), 'Tipo': 'cicla',’Disponibilidad’: true, ‘Valor’: ‘2000’, ‘id’:’1113’ )
producer.send('parqueadero_centro', {'time': time.strftime("%X"), 'Tipo': 'carro',’Disponibilidad’: false, ‘Valor’: ‘2500’, ‘id’:’1114’ )

producer.flush()
	time.sleep(10)
