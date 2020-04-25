import socket
recvSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sendSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

RecvIP = '127.0.0.1'
RecvPort = 4000
recvSocket.bind((RecvIP, RecvPort))

SendIP = '127.0.0.1'
SendPort = 3000

print('-----------------------------------------')
print(RecvIP+':'+str(RecvPort))
print('-----------------------------------------')

def Send():
    while True:
        data = input('')
        print('Send '+ SendIP+':'+str(SendPort)+ ' >> ' + data)
        sendSocket.sendto(data.encode('utf-8'), (SendIP, SendPort))

def Rcvd():
    while True:
        data, addr = recvSocket.recvfrom(1024)
        print('Rcvd '+str(RecvPort)+' >> ' + data.decode('utf-8'))
        print(addr)

import threading
t1 = threading.Thread(target=Send)
t2 = threading.Thread(target=Rcvd)
t1.start()
t2.start()