import os
path = "//storage//emulated//0//"

python = []
html = []
# r=root, d=directories, f = files
for r,d,f in os.walk(path):
    for file in f:
        if file.endswith(".py"):
            python.append(file)
        if  file.endswith(".html"):
        	html.append(file)
print(python,html)
