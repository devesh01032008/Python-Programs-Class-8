equation = input("Enter Equation Here = ")

if "+" in equation:
        sum = True
else:
        sum = False

def RHSandLHS(equation):
        LHS = equation.split("=")
        return LHS[0],LHS[1]


lhs,rhs = RHSandLHS(equation)
operators = ["+","-"]


if sum == True:
        terms = lhs.split("+")
        rhs = float(rhs)-float(terms[1])
else:
        terms = lhs.split("-")
        rhs = float(rhs)+float(terms[1])
answer = terms[0].split("x")
ans = rhs/float(answer[0])
print(f"Solution Of Given Equation = {ans}")
