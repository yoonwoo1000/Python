import os
ori_name = '고양이.jpg'
# 파일명과 확장자 분리
result = ori_name.split('.')
print("파일명 : ", result[0])
print("확장자 : ", result[1])
# os 라이브러리에서 제공하는 확장자 분리 메소드
(name, ext) = os.path.splitext(ori_name)
print("파일명 : ", name)
print("확장자 : ", ext)
#파일명에 . 가 있으면???
ori_name = '내.작은.고양이.jpg'
(name, ext) = os.path.splitext(ori_name)
print("파일명 : ", name)
print("확장자 : ", ext)
# 게시판에서 파일을 첨부해서 flask에서 받음
# 원본 파일명 / 확장자
# DB에 파일명과 파일 종류를 저장
# + 실제로 저장된 파일의 이름
# -> flask에서 받은 파일의 이름을 변경해서 저장
import uuid
uuid_name = str(uuid.uuid4()) + ext
print(uuid_name)
# 해당 파일이름의 파일이 폴더에 있는지 확인
if not os.path.exists(uuid_name) :
    print("파일을 저장해도 됩니다")
else :
    print("같은 이름의 파일이 있습니다")
    print("파일명을 다시 생성해야 합니다")
# 해당 파일이름의 파일이 폴더에 있는지 확인
uuid_name = 'asdf.txt'
if not os.path.exists(uuid_name) :
    print("파일을 저장해도 됩니다")
else :
    print("같은 이름의 파일이 있습니다")
    print("파일명을 다시 생성해야 합니다")