
import matplotlib.pyplot as plt
import numpy as np
 
Y = np.loadtxt('underDampMacOS.txt')
X = np.loadtxt('x.txt', delimiter=',')
 
plt.plot(X, Y)
plt.title('UnderDamp')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()