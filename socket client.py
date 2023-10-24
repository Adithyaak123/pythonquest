import socket
c=socket.socket()
c.connect(("localhost",9999))
name=input("enter your name")
c.send(name.encode())
print(c.recv(100).decode())