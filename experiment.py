import os
import time
os.system("clear")
time.sleep(2)
print("Note : Only use x and y in equation !")
time.sleep(1)
equation = input("Enter Your Equation = ")
time.sleep(1)
print("You Entered "+equation)

def Split(x):
	return equation.split("=")

splited_equation = Split(equation)
lhs = splited_equation[0]
rhs = splited_equation[1]
if "+" in lhs:
	sum = True
elif "-" in lhs:
	sum = False

if sum==True:
	time.sleep(2)
	lhs_x = lhs.split("x")
	solution = int(rhs)/int(lhs[0])
	print("Solution When y is constant is = ",solution)
	time.sleep(2)
	lhs_terms = lhs.split("+")
	lhs_y = lhs_terms[1].split("y")
	solution_2 = int(rhs)/(int(lhs_y[0]))
	print("Solution When x is constant is = ",solution_2)
	time.sleep(2)
elif sum==False:
	time.sleep(2)
	lhs_x = lhs.split("x")
	solution = int(rhs)/int(lhs[0])
	print("Solution When y is constant is = ",solution)
	time.sleep(2)
	lhs_terms = lhs.split("-")
	lhs_y = lhs_terms[1].split("y")
	solution_2 = int(rhs)/(int(lhs_y[0]))
	print("Solution When x is constant is = ",-(solution_2))
	time.sleep(2)


print("Thank you \n")
