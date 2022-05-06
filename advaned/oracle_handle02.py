# 오라클DB 연동
from sqlite3 import connect
import cx_Oracle as ora

# DB 함수
def myconn():
    # 데이터소스 네임 객체 생성(접속주소, 포트번호, 서비스명)
    dsn = ora.makedsn('localhost', 1521, service_name='orcl') # 오라클 주소
    # DB 연결객체
    conn = ora.connect(user='scott', password='tiger', dsn=dsn, encoding='utf-8') # 오라클 접속
    return conn


def test01(conn):
    cur = conn.cursor() # 커서생성
    query = 'SELECT * FROM emp' # 쿼리문 작성

    for row in cur.execute(query):
      print(row)

    cur.close()
    conn.close()

def test02(conn):
    cur = conn.cursor() # 커서생성
    query = 'SELECT * FROM emp' # 쿼리문 작성
    cur.execute(query)
    
    while True:
        row = cur.fetchone()   # fetchone 원이 아닐 때 까지 무한반복(while)
        if row is None: break
        print(row)

    cur.close()
    conn.close()



if __name__ == '__main__':
    print('---- SQL조회 기본 실행 ----')
    test01(myconn())
    print('---- SQL조회 fetchon 사용 ----')
    test02(myconn())