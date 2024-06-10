# 1. 먼저 데이터베이스를 연결하는 과정

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# MySQL 데이터베이스 URL 설정
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:1111@localhost:3306/codingtest"

engine = create_engine(SQLALCHEMY_DATABASE_URL) # DB엔진 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # 데이터베이스와의 상호작용을 관리하는 세션 객체를 생성하는 세션 팩토리



Base = declarative_base() # orm 모델을 위한 베이스 클래스
# orm은 데이터베이스와 객체 지향 프로그래밍인 python 사이의 불일치를 해소
