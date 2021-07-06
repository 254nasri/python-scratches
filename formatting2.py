from datetime import *
import time
x=time.time()
y=datetime.fromtimestamp(x)
print("*********************************************")
print("\t{}/{}/{}".format(y.day,y.month,y.year))
print("\t{}:{}:{}".format(y.hour,y.minute,y.second))
print("{}".format(y.time()))