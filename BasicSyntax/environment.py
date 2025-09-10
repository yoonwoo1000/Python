# 한줄 주석
# 여러줄 주석은 없습니다
'문자열'
"문자열"
'''
여러줄
문자열
작성하는
방법
'''
"""
여러줄
문자열
"""
# 가상환경 설정하기
# 가상환경 생성하기
# conda create -n 환경이름 python=버전 [-y]
#conda create -n ezen python=3.10 
# 가상환경 활성화 하기
# conda activate 환경이름
#conda activate ezen
# 가상환경 비활성화
#conda deactivate
# 가상환경 삭제하기
# conda env remove 환경이름 [-y]
#conda env remove ezen -y
# 최초 환경 구성시 conda 초기화가 필요한 경우가 있습니다
# conda init
# 최초 환경 구성시, 약관 동의 입력이 필요합니다
# 동의 : a
# VS code 설정 중 : Terminal › Integrated › Default Profile: Windows
# Command prompt 로 설정
변수 = 10
print(변수)
# 콘다 가상환경 목록 확인하기
# conda env list
# 활성화 된 콘다 환경의 파이썬 버전 확인
#python --version

# 파이썬의 라이브러리는, 온라인상의 '저장소'에서 받아서 설치합니다
# repository : 라이브러리를 받을수 있는 관리자 제공
# pip install 라이브러리이름[==버전]
# conda install 라이브러리이름[=버전]
# conda install requests : conda에서 설치
# pip install numpy : pip로 설치
#import numpy : import문으로 라이브러리 가져올수 있게 됨