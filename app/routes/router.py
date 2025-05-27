"""라우터 파일"""

from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    """라우터 테스트"""
    return {"message": "Hello World"}
