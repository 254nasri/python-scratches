import socket
import os
sock=socket.socket()
sock.bind(("127.0.0.1",7))

sock.listen(1)
print("listening on port 6:")
conn,addr=sock.accept()
print(addr[0]+" connected")
while True:
    command=input("@user>")
    conn.send(command.encode())
    file=conn.recv(1024)
    file=file.decode()
    print(file)