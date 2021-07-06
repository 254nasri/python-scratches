import os
os.chdir('/root/Desktop')
file=open('lll.lst','r')
for x in file:
    new="{}{}".format(x[0:4],12345)
    print(new)
    file1 = open("ll.lst", "r+")
    new_file = file1.write(new)
