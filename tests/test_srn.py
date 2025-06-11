"""SRN 생성 및 조회 단위 테스트"""
from fastapi.testclient import TestClient
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from application import app
from urllib.parse import quote

client = TestClient(app)

def test_create_and_get_srn():
    # SRN 생성 요청
    payload = {
        "domain": "doc",
        "region": "kr-daegu-1",
        "category": "사건명",
        "subcategory": "형사",
        "attributes": ["content-image", "legal"]
    }
    response = client.post("/rns/srn", json=payload)
    assert response.status_code == 200
    srn_data = response.json()

    # SRN 조회 요청 (URL 인코딩 필수)
    encoded_srn = quote(srn_data["srn"], safe="")
    get_response = client.get(f"/rns/srn/{encoded_srn}")
    assert get_response.status_code == 200
    assert get_response.json()["srn"] == srn_data["srn"]
