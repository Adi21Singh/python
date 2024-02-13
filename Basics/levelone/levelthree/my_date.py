import time
import calendar


print(time.localtime())

localtime = time.asctime(time.localtime(time.time()))
print(localtime)