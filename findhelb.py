import os
import re
os.chdir("/root/Desktop")
file=open('helb.lst','r')
print("please enter your ID/Registration number to check if you qualified for 2019/2020 HELB loan")
regno=input()
for x in file:
        searchme=re.search('(.*) '+regno+' (.*)' ,x)
        while searchme:
            print("\n\n-----------------------------------------------------QUALIFIED--------------------------------------------------------------------\n\n")
            print(searchme.group())
            print("\n\n------------------------------------------------------------------------------------------------------------------------------------\n\n")
            break
