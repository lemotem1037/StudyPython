# 오라클DB 연동
import cx_Oracle as ora

# 데이터소스 네임 객체 생성(접속주소, 포트번호, 서비스명)
dsn = ora.makedsn('localhost', 1521, service_name='orcl') # 오라클 주소

# DB 연결객체
conn = ora.connect(user='scott', password='tiger', dsn=dsn, encoding='utf-8') # 오라클 접속

cur = conn.cursor() # 커서생성
query = 'SELECT * FROM emp' # 쿼리문 작성 (emp 대신 memberTBL로 변견해도 자료 출력 가능)

for row in cur.execute(query):
    print(row)

cur.close()
conn.close()    