# 파일 입출력 1 - 파일 쓰기

# mode = w 새로생성쓰기 a 추가쓰기 r 읽기
f = open(file='C:/STUDY/StudyPython/temp.txt', mode='w', encoding='utf-8')  # 절대경로 

f.write('안녕하세요.\n')
f.write('저는 lemotem입니다.\n')
f.write('초보 개발자죠.\n')

f.close()  # open을 쓸 때 close는 필수!!
print('파일 생성완료')