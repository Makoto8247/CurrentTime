import datetime
import time

def hour():
    return datetime.datetime.now().strftime("%H:%M:%S")
def day():
    return datetime.datetime.now().strftime("%Y/%m/%d")
