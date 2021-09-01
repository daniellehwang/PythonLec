from socket import *

# 소켓을 생성
clientSock = socket(AF_INET, SOCK_STREAM)
# 서버의 주소로 접속/연결 (강원랜드 주소, 506호 게임방)
clientSock.connect(('127.0.0.1', 9000))

#서버에 보내고 받는다
while True:
    s = input('전송 문자열 >> ')
    if s == '<stop>':
        clientSock.close()
        break
    clientSock.send(s.encode())
    s = clientSock.recv(1024).decode('utf-8')
    print('서버로부터 수신 : ' + s)