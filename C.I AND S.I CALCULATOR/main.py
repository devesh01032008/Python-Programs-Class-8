p = int(input("Enter principle = "))
r = int(input("Enter rate of interest = "))
t = int(input("Enter Time = "))
c = input("Enter to find put interest = ")
if c == "":
	si = p*r*t/100
	print("Interest at simple = ",si,"Amount at simple interest = ",p+si)
	ci = p*((1+r/100)**t)
	print("Interest at compound = ",ci-p,"Amount at compound interest = ",ci)
	profit = ci-si
	
elif c =="si":
	si = p*r*t/100
	print("Interest at simple = ",si,"Amount at simple interest = ",p+si)
elif c=="ci":
	ci = p*((1+r/100)**t)
	print("Interest at compound = ",ci-p,"Amount at compound interest = ",ci)
else:
	raise Exception
