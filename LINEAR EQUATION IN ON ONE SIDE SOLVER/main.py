equation = input("Enter Equation Here = ")


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
