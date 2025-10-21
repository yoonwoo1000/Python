from service.user import join

name, uID, pw, email = "이젠", "ezen", "1234", "ezen@ezen.com"
result = join(name, uID, pw, email)
if result:
    print("회원가입이 진행되었습니다")
else:
    print("회원가입이 실패했습니다")
