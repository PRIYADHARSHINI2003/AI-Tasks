import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(1.1, 10, 100)
y = x*x + np.log(x/2)
plt.clf()
plt.plot(x,x,"r")
plt.title("PLOT")
plt.ylabel("y = x^2+log(x/2)")
plt.xlabel("x")
plt.plot(x,y,'.')
plt.show()
