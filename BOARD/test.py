import service.board as boardService
if boardService.checkFileAllow('.ppt') :
    print('허용하는 확장자입니다')
else :
    print('허용하지 않는 형식입니다')
if boardService.isImage('.mp3') :
    print('이미지파일 형식 입니다')
else :
    print('이미지파일 형식이 아닙니다')