# Naver(Googl) weppage 긁어오기2
import requests as req

res = req.get('https://www.naver.com/') 
# print(res.status_code)
print(res.content)