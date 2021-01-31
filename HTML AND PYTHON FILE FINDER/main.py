import os
path = os.getcwd()
python = []
html = []
# r=root, d=directories, f = files
for r,d,f in os.walk(path):
    for file in f:
        if file.endswith(".py"):
            python.append(str(r)+str(d)+str(file))
        if  file.endswith(".html"):
        	html.append(str(r)+str(d)+str(file))
for file in python:
	print(file,"\n")
for file in html:
	print(html,"\n")
