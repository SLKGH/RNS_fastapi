"""SRN 생성 및 조회 API"""
from fastapi import APIRouter, HTTPException
from app.models.models import SRNCreateRequest, SRNInfo
from app.core.validate import validate_domain_rules
import uuid

router = APIRouter()

# SRN 정보를 메모리에 저장하는 임시 저장소
SRN_STORE: dict[str, SRNInfo] = {}

# SRN 생성 엔드포인트
@router.post("/rns/srn", response_model=SRNInfo)
def create_srn(req: SRNCreateRequest):
    # 유효성 검사 수행
    validate_domain_rules(req.domain, req.category, req.subcategory, req.attributes)

    # SRN 구성: uuid로 고유 식별자 생성
    uid = str(uuid.uuid4())[:8]
    category = req.category or "_"
    subcategory = req.subcategory or "_"
    srn = f"srn:{req.domain.value}:{req.region}:{category}/{subcategory}/{uid}"
    url = f"https://cdn.star-workflow.com/resource/{uid}"

    srn_info = SRNInfo(srn=srn, url=url, attributes=req.attributes)
    SRN_STORE[srn] = srn_info
    return srn_info

# SRN 조회 엔드포인트
@router.get("/rns/srn/{srn_id:path}", response_model=SRNInfo)
def get_srn_info(srn_id: str):
    print("요청된 srn_id:", srn_id)
    print("현재 저장된 SRN 목록:", list(SRN_STORE.keys()))
    if srn_id not in SRN_STORE:
        raise HTTPException(status_code=404, detail="SRN이 존재하지 않습니다.")
    return SRN_STORE[srn_id]
