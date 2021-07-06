import os
import re
os.chdir("/root/Desktop")

file=input("Enter file directory: ")
file=open(file,'r')
print("enter name to search")
y=input()
for x in file:
    find=re.search('(.*)'+y+'(.*)',x)
    while find:
        print(find.group())
        break
