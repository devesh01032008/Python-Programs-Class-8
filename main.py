X = input("Enter A File Name You Want To Read = ")
if X =="":
	X = "main.txt"
	f = open(X,"a")
	f.write("Enter a file name please")
	f.close()
	file = open(X,"r")
	content = file.read()
	Word = input("Enter The Word You Want To Fund Out = ")
	if Word in content:
		print(True,"It is at index ",content.find(Word))
	else:
		print(False)
else:	
	file = open(X,"r")
	content = file.read()
	Word = input("Enter The Word You Want To Fund Out = ")
	if Word in content:
		print(True,"It is at index ",content.find(Word))
	else:
		print(False)