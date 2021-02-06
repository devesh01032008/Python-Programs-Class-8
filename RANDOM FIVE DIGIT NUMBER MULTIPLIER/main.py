import os
os.system("clear")
from random import randint
from time import sleep

list_of_num  = []
list_of_num_2 = []

for i in range(5):
	digit = randint(1,6)
	list_of_num.append(digit)

for i in range(5):
	digit_2 = randint(1,6)
	list_of_num_2.append(digit_2)


number = ""
number_2 = ""


for digit in range(5):
	number = str(list_of_num[digit])+number

for digit in range(5):
	number_2 = str(list_of_num_2[digit])+number_2

number = int(number)
number2 = int(number_2)

sleep(1)
print("Random Number Taken Is = ",number)
sleep(1)
print("Random Number Taken Is = ",number2)
sleep(1)
print("Multiplication Of Number is ",number*number2)
sleep(1)
print("\nThank You \n")
sleep(1)
