"""라우터 파일"""

from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    """라우터 테스트"""
    return {"message": "Hello World"}

#"""파일 업로드 데이터 삽입 및 업데이트 처리 함수"""
# import logging
# from typing import Dict
# from app.database import DbConnect  # 기존 DB 연결 클래스 사용

# # 로깅 설정
# logger = logging.getLogger(__name__)

# async def file_upload_query(upload_file: Dict[str, str]) -> bool:
#     """
#     파일 업로드 데이터 삽입 및 업데이트 처리 함수

#     @param upload_file: 업로드할 파일의 데이터 객체
#     @return: 처리 성공 여부 (boolean)
#     """
#     try:
#         # 데이터 객체 구조 분해 할당
#         category = upload_file["category"]
#         fieldname = upload_file["fieldname"]
#         fileuuid = upload_file["fileuuid"]
#         uploader = upload_file["uploader"]
#         transname = upload_file["transname"]
#         originalname = upload_file["originalname"]
#         checksum = upload_file["checksum"]
#         encoding = upload_file["encoding"]
#         mimetype = upload_file["mimetype"]
#         path = upload_file["path"]
#         size = upload_file["size"]
#         buffer = upload_file["buffer"]

#         # 데이터베이스 연결
#         db = DbConnect()
#         cursor = db.get_cursor()

#         # 기존 데이터 조회 (checksum과 transname이 일치하는 데이터 확인)
#         query = """
#         SELECT transname FROM file_upload
#         WHERE checksum = %s AND transname = %s
#         ORDER BY create_at DESC
#         """
#         cursor.execute(query, (checksum, transname))
#         existing_data = cursor.fetchone()

#         if existing_data:
#             # 기존 데이터가 존재하면 업데이트 수행
#             update_query = """
#             UPDATE file_upload
#             SET category=%s, fieldname=%s, fileuuid=%s, uploader=%s,
#                 transname=%s, originalname=%s, checksum=%s, encoding=%s,
#                 mimetype=%s, path=%s, size=%s, buffer=%s
#             WHERE checksum=%s
#             """
#             cursor.execute(update_query, (
#                 category, fieldname, fileuuid, uploader,
#                 transname, originalname, checksum, encoding,
#                 mimetype, path, size, buffer, checksum,
#             ))
#         else:
#             # 데이터가 없으면 새로 삽입
#             insert_query = """
#             INSERT INTO file_upload (category, fieldname, fileuuid, uploader,
#                                      transname, originalname, checksum, encoding,
#                                      mimetype, path, size, buffer)
#             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#             """
#             cursor.execute(insert_query, (
#                 category, fieldname, fileuuid, uploader,
#                 transname, originalname, checksum, encoding,
#                 mimetype, path, size, buffer,
#             ))

#         # 변경사항 저장
#         db.get_db().commit()
#         db.close()

#         logger.info("파일 업로드 성공: %s",transname)
#         return True  # 성공적으로 삽입 또는 업데이트되었음

#     except Exception as error:
#         logger.error("파일 업로드 실패: %s", error)
#         return False  # 에러 발생 시 False 반환
