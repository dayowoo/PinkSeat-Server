from socket import socket, AF_INET, SOCK_STREAM


def connect_server(my_port):
    server_socket = socket(AF_INET, SOCK_STREAM)
    
    server_socket.bind(('192.168.1.52', my_port)) # '', my_port=9999 안에 서버의 아이피값을 입력합니다.
    server_socket.listen()
    print('server started')

    client_socket, cli_addr = server_socket.accept()
    print('Connected by', cli_addr)


    while True:
        # 클라이언트가 보낸 메시지를 수신하기 위해 대기합니다. 
        data = client_socket.recv(1024)
    
        # 빈 문자열을 수신하면 루프를 중지합니다. 
        if not data:
            break
    
        # 수신받은 문자열을 출력합니다.
        print('Received from', cli_addr, data.decode())
    
        # 문자열을 클라이언트로 전송해줍니다.
        client_socket.sendall('App Btn Down'.encode())
 
    # 소켓을 닫습니다.
    client_socket.close()
    server_socket.close()

if __name__ == '__main__':
	connect_server(9999)