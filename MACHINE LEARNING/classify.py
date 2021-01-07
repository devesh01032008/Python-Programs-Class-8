from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import mean_squared_error
import numpy as np
iris = datasets.load_iris()
iris_X = iris.data
iris_Y = iris.target
print(iris.DESCR)

clf = KNeighborsClassifier()
clf.fit(iris_X,iris_Y)

print(clf.predict([[3,4,3,4]]))
