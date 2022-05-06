# DB 연동 - INSERT INTO
from __future__ import division
from tkinter import INSERT
import cx_Oracle as ora

def myconn():
    dsn = ora.makedsn('localhost', 1521, service_name='orcl')
    conn = ora.connect(user='scott', password='tiger', dsn=dsn, encoding='utf-8')
    return conn

def get_list(conn):
    cur = conn.cursor()
    for row in cur.execute('SELECT * FROM divtbl'):
        print(row)

    cur.close()
    conn.close()

def set_list(conn, tup):
    cur = conn.cursor()
    query = f"INSERT INTO divtbl VALUES (:1, :2)" # 직접 값을 삽입시 ('{tup[0]}', '{tup[1]}') sql Inject 보안 문제 발생 + 사용효율성 
    cur.execute(query)
    conn.commit()   # 완전저장
    cur.close()
    conn.close()

if __name__ == '__main__':
    print('DIVTBL 데이터 조회')
    get_list(myconn())
    print('DIVTBL 신규 입력')
    division, names = input('(division,names) 입력 (구분자 \' \') >').split(' ')
    tup = (division, names)
    set_list(myconn(), tup)

    print('입력 후 DIVTBL 데이터 조회')
    get_list(myconn())
