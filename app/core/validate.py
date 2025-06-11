"""도메인 및 카테고리 유효성 검사 로직"""
from fastapi import HTTPException
from app.models.models import Domain

def validate_document_rules(category, subcategory, attributes):
    valid_categories = ["사건명", "계약서", "문서id"]
    valid_subcategories = [
        "회생", "파산", "형사", "민사", "행정", "가사", "기타",
        "계약서", "합의서", "위임장", "소장", "답변서", "준비서면",
        "항소장", "판결문", "진술서", "사실확인서", "증거자료", "공문",
        "행정서류", "상담기록지", "견적서/청구서", "보고서", "서명/인장"
    ]
    if category and category not in valid_categories:
        raise HTTPException(status_code=400, detail="문서 도메인의 유효하지 않은 대분류입니다.")
    if subcategory and subcategory not in valid_subcategories:
        raise HTTPException(status_code=400, detail="문서 도메인의 유효하지 않은 소분류입니다.")
    if "content-image" not in attributes:
        raise HTTPException(status_code=400, detail="문서 도메인은 'content-image' 속성이 필요합니다.")

def validate_hr_rules(category):
    valid_categories = ["고객", "직원", "협업체"]
    if category and category not in valid_categories:
        raise HTTPException(status_code=400, detail="인적자원 도메인의 유효하지 않은 대분류입니다.")

def validate_project_rules(category, subcategory):
    valid_categories = ["신규", "버그", "개선"]
    valid_subcategories = ["워크플로우", "법률서비스", "광고"]
    if category and category not in valid_categories:
        raise HTTPException(status_code=400, detail="프로젝트 도메인의 유효하지 않은 유형입니다.")
    if subcategory and subcategory not in valid_subcategories:
        raise HTTPException(status_code=400, detail="프로젝트 도메인의 유효하지 않은 유형입니다.")

def validate_domain_rules(domain: Domain, category: str | None, subcategory: str | None, attributes: list[str]):
    if domain == Domain.document:
        validate_document_rules(category, subcategory, attributes)
    elif domain == Domain.human_resource:
        validate_hr_rules(category)
    elif domain == Domain.project:
        validate_project_rules(category, subcategory)
