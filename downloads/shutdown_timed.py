#Delta
import os
import time

time = input("in how much seconds do you want do shutdown: ")
time = int(time)

time.sleep(time)

os.system("shutdown /s /t 0")