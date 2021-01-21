equation = input("Enter Equation Here = ")

if "+" in equation:
	add = True
else:
	sub = True
def RHSandLHS(equation):
	LHS = equation.split("=")
	return LHS[0],LHS[1]


lhs,rhs = RHSandLHS(equation)
operators = ["+","-"]


for operator in operators:
	terms = lhs.split(operator)
	if len(terms) == 2:
		print(terms)
	else:
		break
if add = True:
	diff = float(rhs) - terms[1]
	print(diff)
else:
	sum = float(rhs) + terms[1]
	print(sum)
