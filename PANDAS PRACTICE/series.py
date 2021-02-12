import os
os.system("pip install pandas")
import pandas as pd 
ser = pd.Series([6,5,7,5,4], index = ("a","b","c","d","e"))
ser2 = pd.Series({0:5,1:20,2:40,3:25},index=[3,2,1,0])
ser2 = pd.Series({0:5,1:20,2:40,3:25})
ser3 = pd.Series([1,23,4,5,6])
ser3[-3:]
ser3[0:3]
ser3[2:5]
