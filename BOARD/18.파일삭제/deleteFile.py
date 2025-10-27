import os

# 파일이 있는지 확인
if not os.path.exists('text.txt') :
    print('text.txt 파일이 없습니다')
else :
    print('text.txt 파일이 있습니다')
    try :
        os.remove('text.txt')
        print('text.txt 파일을 삭제했습니다')
    except Exception as e :
        print(e)
        print('text.txt 파일을 삭제하지 못했습니다')

if not os.path.exists('고양이.jpg') :
    print('고양이.jpg 파일이 없습니다')
else :
    print('고양이.jpg 파일이 있습니다')

if not os.path.exists('교안.ppt') :
    print('교안.ppt 파일이 없습니다')
else :
    print('교안.ppt 파일이 있습니다')