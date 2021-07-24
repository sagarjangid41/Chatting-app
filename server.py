import socket
import threading
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "system_ip"
port = port_number
s.bind((ip,port))
s.listen()
c, addr = s.accept()
k, addr = s.accept()
#message1 = c.recv(1024)
#print(message1)
#k.send(message1)
def sws():
    while True:
        message1 = c.recv(1024)
        k.send(message1)
threading.Thread(target=sws).start()
while True:
    message1 = k.recv(1024)
    c.send(message1)
