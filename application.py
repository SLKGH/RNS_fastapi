"""환경설정 파일"""
# Python Library
from fastapi import FastAPI
# from apscheduler.schedulers.asyncio import AsyncIOScheduler

# CORS
from fastapi.middleware.cors import CORSMiddleware

# Route
from app.routes.router import router

# FastAPI 앱 생성 (lifespan 설정 포함)
app = FastAPI(
    # lifespan=lifespan
    )

# CORS 설정 적용
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://star-workflow.com",
        "http://localhost:3000",
        "http://localhost:3001",
        "http://localhost:5173"
    ], # 특정 도메인을 허용하려면 ["http://example.com"]으로 변경
    allow_credentials=True,
    allow_methods=["*"],  # 허용할 HTTP 메서드를 제한하려면 ["GET", "POST"] 등으로 설정
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(router)

# 앱 객체를 외부에서 참조 가능하도록 노출
application = app
