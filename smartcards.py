import os
import re
os.chdir('/root/Desktop')
print("input your reg no search your name in the list")
name=input()
list=open('smartcards.txt','r')
for x in list:
    searchname=re.search('(.*)'+name+'(.*)',x)
    while searchname:
        print("********************************************************************************")
        print(searchname.group())
        print("********************************************************************************")
        break
