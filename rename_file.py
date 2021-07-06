import os
print("eg /root/Videos")
print()
dir=input("Enter the file directory:   ")
os.chdir(dir)
print(os.getcwd())
print()
print("files available are:")
for x in os.listdir(os.getcwd()):
    print(x)
print()
file=input("Enter filename to rename:  ")
print()
while file in os.listdir(os.getcwd()):
    file_rename=input("how do you wish to rename file:  ")
    print()
    choice=input("do you wish to rename "+file+" to "+file_rename+" ?    y/n    ")
    print()
    if choice=="y":
        os.rename(os.getcwd()+"/"+file,os.getcwd()+"/"+file_rename)
        print("Operation Successful")
        print()
        break
    else:
        print("Operation Cancelled")
        break

