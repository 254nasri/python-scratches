import os
os.chdir('/root/Desktop')
for x in os.listdir(os.getcwd()):
    y=x[1:30]
    os.rename(x,y)
