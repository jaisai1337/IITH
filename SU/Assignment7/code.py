import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
y = sym.symbols('y')
a = np.array([7, -2])
b = np.array([1, -5])
p = np.array([5, -3])
q = np.array([3, y])
Q=(a+(2*b))/(1+2)
q[1]=Q[1]
print("The Value of y =",q[1])
axes = plt.subplots( 1 )
x_values = [a[0], b[0]]
y_values = [a[1], b[1]]
plt.plot(x_values, y_values, 'bo', linestyle="-")
plt.text(a[0]-0.015, a[1]+0.25, "A")
plt.text(b[0]-0.015, b[1]+0.25, "B")
plt.plot(p[0], p[1],'o')
plt.text(p[0]-0.015, p[1]+0.25, "P")
plt.plot(q[0], q[1],'o')
plt.text(q[0]-0.015, q[1]+0.25,"Q")
plt.grid()
plt.show()