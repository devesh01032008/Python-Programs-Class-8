number = input("Enter Number = ")
list = []

def CubeEach(number):
	for digit in number:
		length = len(number)
		cube = int(digit)**length
		list.append(cube)
def ListAdd(list):
	sum = 0
	for item in list:
		sum = sum+int(item)
	if str(sum)==number:
		print("Yes it is armstrong number")
	else:
		print("No it is not armstrong number")
CubeEach(number)
ListAdd(list)
