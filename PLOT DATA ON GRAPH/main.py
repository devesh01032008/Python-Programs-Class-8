X = [i for i in range(11)]
Y = [i*i for i in range(11)]
x_label = "Devesh"
y_label = "Sharma"
import matplotlib.pyplot as plt
plt.plot(list(X),list(Y))
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.show()
