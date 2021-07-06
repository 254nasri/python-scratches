import os
os.chdir('/root/Desktop')
for x in os.listdir(os.getcwd()):
    char='c'
    new='{}{}'.format(char,x)
    os.rename(x,new)

