import os
os.system("pip install matplotlib && pip3 install matplotlib")
import matplotlib.pyplot as plt
from math import *
x = [i for i in range(91)]
x2 = [i for i in range(91)]
y = [sin(i) for i in range(91)]
y2 = [0 for i in range(91)]
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.plot(x2,y2)
plt.plot(x,y)
plt.show()
