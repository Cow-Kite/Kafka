from kafka import KafkaProducer
from json import dumps

#producer 객체 생성
producer = KafkaProducer(acks=0, compression_type='gzip',
            bootstrap_servers=['localhost:9092'],
            value_serializer=lambda x : dumps(x, default=str).encode('utf-8'))

sql = []
sql.append('''CREATE TABLE 테이블명 (
    name varchar(11),
    email varchar(255),
    phone varchar(255))''')
sql.append("INSERT INTO 테이블명 VALUES('이름', '메일주소', '010-');")
sql.append("INSERT INTO 테이블명 VALUES('이름', '메일주소', '010-');")
sql.append("INSERT INTO 테이블명 VALUES('이름', '메일주소', '010-');")
sql.append("INSERT INTO 테이블명 VALUES('이름', '메일주소', '010-');")
sql.append("INSERT INTO 테이블명 VALUES('이름', '메일주소', '010-');")
sql.append("INSERT INTO 테이블명 VALUES('이름', '메일주소', '010-');")
sql.append("INSERT INTO 테이블명 VALUES('이름', '메일주소', '010-');")
sql.append("INSERT INTO 테이블명 VALUES('이름', '메일주소', '010-');")

#data를 topic에 저장
for data in sql:
    producer.send('Topic 이름', value=data)
    producer.flush()