question = "Who are you?"
answer = "root"
length = len(question)
print(question)
while True:
    user_answer = input("Enter Your User Name : ")
    if user_answer.lower() == answer:
        password = "root"
        user_password = input("Enter Your Password : ")
        if user_password.lower() == password:
        	print("Welcome "+answer)
        	choice = input("Do you want to Add Account : ")
        	if choice == "yes":
        		username = input("Enter New  Username :")
        		password = input("Enter New Password : ")
        		print("Thank You For Adding Account ")
        		f = open("user.txt","a")
        		f.write(f"Username : {username}\nPassword : {password}\n")
  
        	else:
        		break
    elif user_answer == "quit":
    	break
    else:
    	print("Wrong Username . Please Enter A Valid Username")
