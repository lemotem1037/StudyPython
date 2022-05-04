# 파일 입출력 2 - 파일 읽기

f = open(file='./temp.txt', mode='r', encoding='utf-8')

# t = f.read()
while True:
    line = f.readline()    #
    if not line:
        break

    print(line, end='')  #end=''삽입 또는 \n 제거

print(line)

f.close() ## 필수! 잊지말고 닫아주가
print('파일 읽기 완료')