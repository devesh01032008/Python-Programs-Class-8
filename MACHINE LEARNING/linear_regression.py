import os
os.sytem("pip3=pip")
os.system("pip install sklearn")
os.system("pip install numpy")

from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

import numpy as np


diabetes = datasets.load_diabetes()


"""
dict_keys(['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename'])
"""


diabetes_X = diabetes.data
diabetes_Y = diabetes.target


train_X = np.array(diabetes_X[:-30])
train_Y = np.array(diabetes_Y[:-30])


test_X = np.array(diabetes_X[-30:])
test_Y = np.array(diabetes_Y[-30:])


model = LinearRegression()
model.fit(train_X,train_Y)
pred_Y = model.predict(test_X)

print(mean_squared_error(test_Y,pred_Y))
print(model.coef_)
print(model.intercept_)
