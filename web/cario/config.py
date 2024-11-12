import os

# MySQL을 사용할 경우 데이터베이스 URI 설정
# 로컬 MySQL 서버에 연결 (사용자 이름, 비밀번호, 데이터베이스 이름 설정)
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/shopping_db0'

# 데이터베이스 연결 추적 비활성화 (성능 향상)
SQLALCHEMY_TRACK_MODIFICATIONS = False
