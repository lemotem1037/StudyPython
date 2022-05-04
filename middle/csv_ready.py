# csv 파일 읽기
# from asyncore import read
# from codecs import namereplace_errors
import csv
from operator import delitem
from unicodedata import name

file_name = './busanbus_2021.csv'

f = open(file_name, mode='r', encoding='cp949')   #('./'+file=name)
reader = csv.reader(f, delimiter=',') # 구분자가, 일경우

next(reader) # 제목 줄 있을 때 필요없을 경우 
for line in reader:
    print(line)

    f.close() ## 필수! 


