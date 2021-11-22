#Drawing a triangle given 3 sides
import numpy as np
import matplotlib.pyplot as plt

def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB
import numpy as np
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if


# given triangle vertices
A=[1,4]
B=[3,-2]
C=[-3,16]

area=((A[0]*(B[1]-C[1]))+(B[0]*(C[1]-A[1])+(C[0]*(A[1]-B[1]))))
print("Traditional Method")
print("Area of the triangle is :", area)

#Triangle vertices
A = np.array([1,4]) 
B = np.array([3,-2]) 
C = np.array([-3,16]) 

Ar = np.linalg.det([A-B,A-C])
print("Matrices Method")
print("Area of the triangle is :",round(Ar/2))
if(Ar == 0):
  print("Since the area is ", Ar, "the given points form a straight line.")
else:
  print("Since the area is ", Ar, "the given points form a Triangle.")

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.7), A[1] * (1 - 0.1) , 'A')

plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 + 0.2), B[1] * (1) , 'B')

plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (0 + 0.8), C[1] * (1 - 0) , 'C')
# plt.fill_between(A, B, C)



plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.show()
