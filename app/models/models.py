"""데이터 모델 정의"""
from pydantic import BaseModel
from enum import Enum
from typing import Optional

# SRN의 도메인 종류
class Domain(str, Enum):
    document = "doc"
    human_resource = "hr"
    project = "prj"

# SRN 생성 요청 구조
class SRNCreateRequest(BaseModel):
    domain: Domain
    region: str
    category: Optional[str] = None  # 대분류 (생략 가능)
    subcategory: Optional[str] = None  # 소분류 (생략 가능)
    attributes: list[str]  # 예: ["content-image", "legal"]

# SRN 응답 구조
class SRNInfo(BaseModel):
    srn: str
    url: str
    attributes: list[str]
