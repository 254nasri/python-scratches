import os
new=os.chdir('/root/Desktop')
print(os.getcwd())
file=open("white","r")
content=file.read()
new=content.replace(" ","")
print(new)
file1=open("white","w")
new_file=file1.write(new)
