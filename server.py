import socket
import os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '192.168.43.183'
port = 1255
s.bind((host,port))
s.listen()
socketclient, address = s.accept()
print("got connection from", address)
while True:
    msg = socketclient.recv(1024)
    msg = msg.decode("utf-8")
    print(msg)
##    if msg=="shutdown":
##        os.system("shutdown -s -t 00")
    if msg=="quit":
        s.close()

    
    
