import socket
from time import sleep
import pymysql
import sys
import time

# 서버 IP주소, 맨날 바뀜
HOST = '192.168.1.52'
PORT = 9999        

# mysql 연동
conn  = pymysql.connect(
    host = 'localhost',
    user='root',
    password='1234',
    db='pinkseat_server',
    charset='utf8'
)


def connect_pi(PORT):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    client_socket, addr = server_socket.accept()
    
    # 접속한 클라이언트의 주소
    print('Connected by', addr)
    
    try:
        while True:
            cur = conn.cursor()
            # DB 읽어오기
            cur.execute('select * from pinkseat_server.pinkseat_seat_seat_info')
            rows = cur.fetchall() # 전체 row
            stat_row = str(rows[5][2]) # 좌석상태 row
            alarm_row = str(rows[5][4]) # 알람요청 row


            # 클라이언트한테 좌석상태 받기
            data = client_socket.recv(1024)
            
            # 사람 인식
            if data.decode() == '1':
                print('seat_stat', repr(data.decode()))
                cur.execute('update pinkseat_server.pinkseat_seat_seat_info set seat_stat=1 where seat_stat=0')
                conn.commit() # DB 업데이트 저장

        
            # 알람요청 보내기
            client_socket.send(alarm_row.encode())    
            if alarm_row == '1': 
                sleep(0.5)
                # 알람요청 1상태를 0으로 저장
                print(1)
                cur.execute('update pinkseat_server.pinkseat_seat_seat_info set alarm=0 where alarm=1')
                conn.commit() # DB 업데이트 저장
                client_socket.send(alarm_row.encode()) # 업데이트 내용 보내기
            
    finally:
        cur.close()
        conn.close()
        client_socket.close()
        server_socket.close()


if __name__ == '__main__':
    connect_pi(9999)