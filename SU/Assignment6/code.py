import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
k = sym.symbols('k')
a = np.array([5,k])
b = np.array([k,7])
p = np.array([2,4])
ap = np.transpose(a-p)
ap = ap@(a-p)
print(ap)
bp = np.transpose(b-p)
bp = bp@(b-p)
print(bp)
S= list(sym.solveset(ap-bp,k))
a[1]=a[1].subs(k,int(str(S[0])))
b[0]=b[0].subs(k,int(str(S[0])))
print("the value of k =",S[0])

axes = plt.subplots( 1 )
x_values = [a[0], p[0]]
y_values = [a[1], p[1]]
plt.plot(x_values, y_values, 'bo', linestyle="-")
plt.text(a[0]-0.015, a[1]+0.25, "A")
plt.text(b[0]-0.015, b[1]+0.25, "B")
plt.text(p[0]-0.050, p[1]-0.25, "P")
u_values = [b[0], p[0]]
v_values = [b[1], p[1]]
plt.plot(u_values, v_values, 'o', linestyle="-")
plt.grid()
plt.show()