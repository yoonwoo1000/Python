import pandas as pd

# conda create -n web python=3.10 numpy pandas html5lib lxml -y
# html5 문서를 읽기 위한 라이브러리
# pip install html5lib / conda install html5lib
# 파싱 라이브러리
# pip install lxml     / conda install lxml
"""
html.parser : 파이썬 표준 라이브러리에 포함되어 있어 별도 설치가 필요 없으며 기본적인 HTML 파싱에 적합하다.
lxml : 매우 속도가 빠르고 정확한 파서로, 잘못된 HTML도 유연하게 처리할 수 있다(설치 필요).
html5lib : HTML5 표준에 맞춰 가장 충실하게 파싱하며, 사람처럼 문서를 읽어들인다(설치 필요).
lxml-xml / xml : XML 문서를 파싱할 때 사용하는 전문 파서이다(설치 필요).
"""
url = "http://192.168.0.25:5500/stock.html"
tables = pd.read_html(url, encoding="utf-8")
if tables:
    print("웹문서에서 테이블을 찾았습니다")
else:
    print("웹문서에 테이블이 없습니다")
for table in tables:
    print("-" * 30, "\n", table, "\n", type(table))
