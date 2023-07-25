import pymysql
from kafka import KafkaConsumer
from json import loads

#mysql에 접속
mysql_con = pymysql.connect(
    host='localhost',
    user='root',
    password='mysql비밀번호',
    db='DB이름',
    charset='utf8'
)

#KafkaConsumer 객체 생성
consumer = KafkaConsumer('토픽이름', bootstrap_servers='localhost:9092',
enable_auto_commit=True, auto_offset_reset='earliest',
value_deserializer=lambda x : loads(x).encode().decode('utf-8'),
consumer_timeout_ms=1000)

#커서 가져오기
cursor = mysql_con.cursor()

#consumer에 있는 message 
for message in consumer: 
    sql = message.value
    cursor.execute(sql) #message DB에 적용

mysql_con.commit()
mysql_con.close()