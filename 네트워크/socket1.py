# 1. 전화기 필요(socket, 소켓)
# 2. ip, port 필요(192.168.1.45, 3000)
# 3. 전화기 생성 binding (ip + port)
import socket
recvSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sendSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#AF_INET : ipv4
#SOCK_DGRAM : UDP

#수신 설정
RecvIP = '127.0.0.1'
RecvPort = 3000 #다른 프로그램과 동시 사용 시 바인딩 에러
recvSocket.bind((RecvIP, RecvPort))

#송신 설정 ( 받는쪽이 바인딩 해놔야 함. )
SendIP = '127.0.0.1'
SendPort = 4000

print('-----------------------------------------')
print(RecvIP+':'+str(RecvPort))
print('-----------------------------------------')

#sendto의 내 컴퓨터에서 보내는 Port는 임의로 발생 시킴.
def Send():
    while True:
        data = input('')
        print('Send '+ SendIP+':'+str(SendPort)+ ' >> ' + data)
        sendSocket.sendto(data.encode('utf-8'), (SendIP, SendPort))

def Rcvd():
    while True:
        data, addr = recvSocket.recvfrom(1024)  # 1KB
        print('Rcvd '+str(RecvPort)+' >> ' + data.decode('utf-8'))
        print(addr)
        

import threading
t1 = threading.Thread(target=Send)
t2 = threading.Thread(target=Rcvd)
t1.start()
t2.start()
