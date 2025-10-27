# flask 프레임워크에 의존성이 있어서 flask 설치시 같이 설치
# werkzeug 라이브러리
from werkzeug.utils import secure_filename
# secure_filename : 안전한 파일명
import os
# WAS : 보안, 파일, 폴더 권한
# "../../../text.txt" : 상위 폴더 접근 시도
# fullPath = os.path.join(폴더,파일명)
# "파일명\x00.jpg" : Null 바이트 공격
# "<script>코드작성</script>.jpg" : XSS 공격
fileName = "../../../text.txt"
safeName = secure_filename(fileName)
print(safeName)
fileName = "filename\x00.jpg"
safeName = secure_filename(fileName)
print(safeName)
fileName = "<script>code...</script>.jpg"
safeName = secure_filename(fileName)
print(safeName)
# 한글은 안전하지 않은 문자열로 취급됩니다
fileName = "고양이.jpg"
safeName = secure_filename(fileName)
print(safeName)