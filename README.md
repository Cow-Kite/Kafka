# Kafka-MySQL
Kafka-MySQL 연동

Jookeeper & Kafka 실행
1. Jookeeper 실행: /tools/zookeeper/bin/zkServer.sh start
2. Kafka 실행: /tools/kafka/bin/kafka-server-start.sh -daemon /tools/kafka/config/server.properties

필요한 라이브러리 설치
1. kafka-python: pip install kafka-python
2. pymysql: pip install pymysql

Producer & Consumer
1. Producer.py: sql 구문을 Topic에 저장하는 역할
2. Consumer.py: Topic에 있는 Message를 불러오는 역할, pymysql 라이브러리를 활용해 Message를 DB에 적용