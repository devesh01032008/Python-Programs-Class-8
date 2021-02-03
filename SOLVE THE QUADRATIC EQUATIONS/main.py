import cmath
a = int(input("Enter The value of ax2 = " ))
b = int(input("Enter the value of bx = " ))
c = int(input("Enter the value of c = "))
d = b**2-4*a*c
x1 = ((-b)+(cmath.sqrt(d)))/2*a
x2 = ((-b)-(cmath.sqrt(d)))/2*a
print(f"The Solutiom of given quadratic equation is {x1},{x2}  ")

