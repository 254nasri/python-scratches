#removing parts of the naming string

import os
print("eg /root/Videos")
print()
dir=input("Enter the file directory:   ")
os.chdir(dir)
print(os.getcwd())
print()
print("files available are:")
for x in os.listdir(os.getcwd()):
    a,b=os.path.splitext(x)
    i,j,k,l =a.split(" ")
    new_name="{}_{}".format(i,l)
    print(new_name)
    os.rename(x,new_name)

