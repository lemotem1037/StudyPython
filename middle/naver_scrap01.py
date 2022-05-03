# Naver wep page 긁어오기
from urllib.request import Request, urlopen

req = Request('https://www.naver.com/')
res = urlopen(req)   # urlope이라는 함수 실행
print(res.status)

