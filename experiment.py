#importing modules

import os
os.system("clear")
number= int(input("Enter The Number \n"))

for numbers in range(1,number):
	remainder = number%numbers
	if remainder == 0:
		print("The Number is divisble by "+str(numbers))
	else:
		print("It is A prime number")
