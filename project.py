import math as m
number = int(input("Enter the number you want to make perfect square = "))
a = m.sqrt(number)
if a==int(number):
	print("It's already a perfect square")
	print(a)
else:
	b = input("Enter add/sub for nearest perfect square = ")
	if b=="sub":
		c = int(a)*int(a)
		result = number-c
		print(f"{result} should be subtracted from {number} to obtain a perfect square of {int(a)}")
		f = open("main.txt","a")
		f.write((f"{result} should be subtracted from {number} to obtain a perfect square of {int(a)}\n"))
	elif b=="add":
		c = (int(a)+1)*(int(a)+1)
		result = c-number
		print(f"{result} should be add to {number} to obtain a perfect square of {int(a)+1}")
		f = open("main.txt","a")
		f.write(f"{result} should be add to {number} to obtain a perfect square of {int(a)+1}\n")
	else:
		while b!="add" or  b!="sub":
			b = input("Enter your choices = ")
			if b=="sub":
				c = int(a)*int(a)
				result = number-c
				print(f"{result} should be subtracted from {number} to obtain a perfect square of {int(a)}")
				f = open("main.txt","a")
				f.write((f"{result} should be subtracted from {number} to obtain a perfect square of {int(a)}\n"))
			elif b=="add":
				c = (int(a)+1)*(int(a)+1)
				result = c-number
				print(f"{result} should be add to {number} to obtain a perfect square of {int(a)+1}")
				f = open("main.txt","a")
				f.write(f"{result} should be add to {number} to obtain a perfect square of {int(a)+1}\n")
