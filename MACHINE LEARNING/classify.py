# Automatically installing packages

import os
os.system("pip install sklearn")
os.system("pip install numpy")

# importing sklearn modules
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import mean_squared_error
import numpy as np

#Datasets loades
iris = datasets.load_iris()
iris_X = iris.data
iris_Y = iris.target
print(iris.DESCR)

# Model created

clf = KNeighborsClassifier()
clf.fit(iris_X,iris_Y)

#Printed
print(clf.predict([[3,4,3,4]]))

# Program ends
