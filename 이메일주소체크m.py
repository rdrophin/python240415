import re

def check_email(email):
    # 이메일 주소를 검증하는 정규식 패턴
    #r: raw string notation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    #pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    # 이메일 주소가 정규식 패턴과 일치하는지 확인
    if re.match(pattern, email):
        return True
    else:
        return False

# 이메일 주소 테스트
email1 = "example@email.com"
email2 = "invalid_email.com"

print("이메일 주소 1:", email1)
print("이메일 주소 1 체크 결과:", check_email(email1))

print("이메일 주소 2:", email2)
print("이메일 주소 2 체크 결과:", check_email(email2))
