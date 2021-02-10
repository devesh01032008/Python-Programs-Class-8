#importing modules

import os
import time
os.system("clear")
time.sleep(1)

# Declaring Variables

binary_num = input("Enter Number in Binary\n")
binary_num = list(binary_num)
length = len(binary_num)
decimal_num = 0
time.sleep(1)

# Checking if it is bianry

for I in binary_num:
	I = int(I)
	if I == 1 or I == 0:
		binary = True
	else:
		binary = False
		raise Exception("Not a binary Number")


# Making Logic

for i in binary_num:
	decimal_num = decimal_num +(int(i)*2**(length-1))
	length = length-1

# printing answer

print("Answer in Decimal = "+str(decimal_num))
time.sleep(1)

# Program ends
