import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = '192.168.43.183'
port = 1255
s.connect((host,port))
while True:
    msg = input("Enter message: ")
    s.send(msg.encode("utf-8"))
    if msg=="quit":
        s.close()
        break
