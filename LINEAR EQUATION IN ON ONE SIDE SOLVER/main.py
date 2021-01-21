equation = input("Enter Equation Here = ")

if "+" in equation:
<<<<<<< HEAD
	sum = True
else:
	sum = False
=======
        sum = True
else:
        sum = False
>>>>>>> 4447d2f35611eb0d565bcf57c82d5870e6cd164d

def RHSandLHS(equation):
        LHS = equation.split("=")
        return LHS[0],LHS[1]


lhs,rhs = RHSandLHS(equation)
operators = ["+","-"]


if sum == True:
<<<<<<< HEAD
	terms = lhs.split("+")
	rhs = float(rhs)-float(terms[1])
else:
	terms = lhs.split("-")
	rhs = float(rhs)+float(terms[1])
answer = terms[0].split("x")
ans = rhs/float(answer[0])
print(f"Solution Of Given Equation = {ans}")
=======
        terms = lhs.split("+")
        rhs = float(rhs)-float(terms[1])
else:
        terms = lhs.split("-")
        rhs = float(rhs)+float(terms[1])
answer = terms[0].split("x")
ans = rhs/float(answer[0])
print(f"Solution Of Given Equation = {ans}")
print("Thank You For Using It")

>>>>>>> 4447d2f35611eb0d565bcf57c82d5870e6cd164d
