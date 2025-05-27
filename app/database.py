"""PostgreSQL 데이터베이스 연결 정보를 반환하는 함수"""
# python 내부 모듈
import logging
import os
import psycopg2

#외부 라이브러리
from psycopg2 import OperationalError
from psycopg2.extensions import connection, cursor
from dotenv import load_dotenv

# 로깅 설정
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)

# 환경 변수 로드
load_dotenv()


def return_database_url(status: str = "dev") -> dict:
    """
    PostgreSQL 데이터베이스 연결 정보를 반환하는 함수

    node 작성자 : 최현석
    python 작성자 : 김건희

    @param status: 'dev' 또는 'prod'를 지정하여 개발/운영 데이터베이스를 구분
    @return: DB 연결 정보 딕셔너리
    @raises ValueError: 환경 변수가 누락된 경우 발생
    """
    # 환경 변수 로드
    if status == "dev":
        db_config = {
            "host": os.getenv("DEV_DB_HOST"),
            "dbname": os.getenv("DEV_DB_NAME"),
            "user": os.getenv("DEV_DB_USER"),
            "password": os.getenv("DEV_DB_PASSWORD"),
            "port": os.getenv("DEV_DB_PORT"),
        }
    else:
        db_config = {
            "host": os.getenv("DB_HOST"),
            "dbname": os.getenv("DB_NAME"),
            "user": os.getenv("DB_USER"),
            "password": os.getenv("DB_PASSWORD"),
            "port": os.getenv("DB_PORT"),
        }

    # 환경 변수 누락 체크
    missing_envs = [key for key, value in db_config.items() if not value]
    if missing_envs:
        raise ValueError(f"환경 변수 {', '.join(missing_envs)}가 설정되지 않았습니다.")

    return db_config


class DbConnect:
    """
    PostgreSQL 데이터베이스 연결 클래스 (psycopg2 기반)
    """

    def __init__(self, status: str = "dev"):
        """
        데이터베이스 연결 초기화
        """
        try:
            db_config = return_database_url(status)
            self.db: connection = psycopg2.connect(**db_config)  # DB 연결
            self.cursor: cursor = self.db.cursor()  # DB 커서
            logging.info("데이터베이스 연결이 성공적으로 설정되었습니다.")
        except OperationalError as e:
            logging.error("데이터베이스 연결 실패")
            logging.error(e)
            raise

    def get_db(self) -> connection:
        """
        현재 데이터베이스 연결 객체 반환
        """
        return self.db

    def get_cursor(self) -> cursor:
        """
        현재 데이터베이스 커서 객체 반환
        """
        return self.cursor

    def close(self):
        """
        데이터베이스 연결 및 커서 닫기
        """
        try:
            if self.cursor:
                self.cursor.close()
                logging.info("커서가 정상적으로 닫혔습니다.")
            if self.db:
                self.db.close()
                logging.info("데이터베이스 연결이 정상적으로 종료되었습니다.")
        except Exception as e:
            logging.error("데이터베이스 연결 해제 중 오류 발생: %s", e)


# FastAPI에서 사용할 DB 인스턴스 생성 (전역 객체)
db_instance = DbConnect("dev")

def get_db():
    """
    FastAPI 종속성 주입을 위한 데이터베이스 연결 반환 함수
    """
    return db_instance.get_db()


def get_cursor():
    """
    FastAPI 종속성 주입을 위한 커서 반환 함수
    """
    return db_instance.get_cursor()
