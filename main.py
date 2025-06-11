"""
FastAPI 애플리케이션을 실행하는 엔트리포인트 스크립트입니다.
포트 지정 파일
작성자 : 김건희
"""
import uvicorn
# from application import application  # application.py에서 생성한 FastAPI 앱을 가져옵니다.

if __name__ == "__main__":

    uvicorn.run(
        "application:application",  # application.py에서 application 인스턴스를 가져옴
        host="0.0.0.0",  # 모든 네트워크 인터페이스에서 접근 가능
        port=9494,  # 포트 9494에서 애플리케이션 실행
        reload=True,  # 코드 변경 시 자동으로 애플리케이션 리로드 (개발 환경용)
        log_level="info",  # 로그 레벨 설정
    )
