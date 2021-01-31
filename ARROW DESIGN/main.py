import time
import os
d = 15
for i in range(16):
	print(" "*i,"*"," "*i,"*"," "*i,"*")
	time.sleep(0.05)

for i in range(16):
	print(" "*d,"*"," "*d,"*"*1," "*d,"*")
	d = d-1
	time.sleep(0.05)

os.system("clear")
os.system("python"+" main.py")
