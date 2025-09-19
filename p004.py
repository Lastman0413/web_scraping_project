# 정규식(re:regular expression)

# 주민등록번호
# 901201-1111111

# 이메일 주소
# nadocoding@gmail.com
# nadocoding@gmail@gmail.com

# 차량 번호
# 11가 1234
# 123가 1234

# IP 주소
# 192.168.0.1

# 웹 스크래핑에 필요한 정규식

import re
# abcd, book, desk
# ca?e
# care, cafe, case, cave
# caae, cabe, cace, cade, ... (대입)

p = re.compile("ca.e")  # 정규식 사용 
# . (ca.e) : 하나의 문자를 의미 -> care, cafe, case (o) | caffe (x)
# ^ (^de)  : 문자열의 시작 -> desk, destination (o) | fade (x)
# $ (se$)  : 문자열의 끝 -> case, base (o) | face (x)

m = p.match("cafe")
# print(m.group()) # 매치되지 않으면 에러가 발생

if m:
    print(m.group())
else:
    print("매칭되지 않음")