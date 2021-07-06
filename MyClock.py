import os
import time
from datetime import datetime
now=datetime.fromtimestamp(time.time())
hr=now.hour
min=now.minute
sec=now.second
print("{}:{}:{}".format(hr,min,sec))
time.sleep(1)
while True:
    now=datetime.fromtimestamp(time.time())
    time.sleep(1)
    hr=now.hour
    min=now.minute
    sec=now.second
    print("{}:{}:{}".format(hr,min,sec))
    if hr==18 and min==44 and sec==10:
        os.chdir('/root/Desktop/')
        file=open('fff.py','r')
        for x in file:
            print(x)
        break
