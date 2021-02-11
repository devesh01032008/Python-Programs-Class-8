#importing modules
from time import sleep
import os
os.system("clear")
sleep(1)
number= int(input("Enter The Number \n"))
num=1
sleep(1)
while num!=number:
	remainder = number%num
	if remainder == 0:
		print("The Number is divisble by "+str(num))
	num = num+1
sleep(1)
