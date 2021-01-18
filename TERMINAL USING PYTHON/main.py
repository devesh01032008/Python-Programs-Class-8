import os
while True:
        cmd = input("Enter The Command = ")
        if cmd != "exit()":
                os.system(cmd)
        else:
                os.system("exit")
                break
print("Thank You For Using This Terminal")
