import socket
s=socket.socket()
s.bind(("localhost",9999))
s.listen() #enable server to accept connection requests
print("waiting for connection")
while True:
    c,address=s.accept()
    name=c.recv(100).decode()
    print("connected with",address,name)
    c.send("thank you for connecting".encode())