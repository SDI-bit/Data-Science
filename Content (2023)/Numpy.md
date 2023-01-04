# Numpy
![numpylogo](https://user-images.githubusercontent.com/55890376/209995233-2d1a3edc-a683-47ad-becf-fb22547e7adb.svg)

[NumPy](https://numpy.org/) stands for Numerical Python. It is a Python library used for working with an array. In Python, we use the list for purpose of the array but it’s slow to process. NumPy array is a powerful N-dimensional array object and its use in linear algebra, Fourier transform, and random number capabilities. [More info](https://numpy.org/doc/stable/user/absolute_beginners.html)

## Installation
```
pip install numpy
```
## Import
```
import numpy as np
```

## functions
### numpy.array
An array, any object exposing the array interface, an object whose __array__ method returns an array, or any (nested) sequence. If object is a scalar, a 0-dimensional array containing object is returned. default dtype is float

```
import numpy as np
#1D array
a = np.array([1, 2, 3])

#2D array
b = np.array([[1, 2], [3, 4]])

#3D array
c = np.array([[1,2,-1],[1,-1,2],[1,1,1]])
```
### numpy.matrix
Returns a matrix from an array-like object, or from a string of data.
```
a = np.matrix([[1, 2], [3, 4]])
>>> [[1 2]
 [3 4]]
```
### numpy.dot
Dot product of two arrays. 
```
a = [[1, 0], [0, 1]]
b = [[4, 1], [2, 2]]
np.dot(a, b)
>>> array([[4, 1],
       [2, 2]])
```
### numpy.linalg.inv
Compute the (multiplicative) inverse of a matrix. Provided matrix is not singular i.e. det(A)!=0

```
A_inverse = np.linalg.inv([[1,2,-1],[1,-1,2],[1,1,1]])
>>>[[ 1.          1.         -1.        ]
    [-0.33333333 -0.66666667  1.        ]
    [-0.66666667 -0.33333333  1.        ]]
```
### numpy.linalg.solve
Solve a linear matrix equation, or system of linear scalar equations.
```
a = np.array([[1, 2], [3, 5]])
b = np.array([1, 2])
x = np.linalg.solve(a, b)
array([-1.,  1.])
```


## how system of equations are solved
![download](https://user-images.githubusercontent.com/55890376/209999186-e47bbe7b-3b54-407c-ba32-c725c983dd64.png)
1. `A_inverse = numpy.linalg.inv(A)` We take inverse of matrix A 
2.  `C = numpy.dot(A-inverse,B)` dot product of inverse of A and B
3. `print(C)` print the resultant matrix 


## 3 variable equation solver (without np.linalg.solve)
```
# A X = B
# X = A^-1 B
import numpy as np
'''
Solving system of lineear equation
x + 2y - z = 2
x - y + 2z = 5
x + y + z  = 6
'''
A = np.matrix(np.array(
    [[1,2,-1],
     [1,-1,2],
     [1,1,1]]
    ))

B = np.matrix(np.array(
    [[2],
     [5],
     [6]]
    ))

print("Matrix A",A,"\n",sep="\n")
print("Matrix B",B,"\n",sep="\n")

A_inverse = np.linalg.inv(A)  # storing inverse of A ,provided A is not singular matrix i.e.  det(A)!=0
print("Matrix A invese",A_inverse,"\n",sep="\n")

X = np.dot(A_inverse,B)  # X = Ainv x B
print("Solution of system of equation\n",X)
```
### [Output](https://github.com/SDI-bit/Data-Science/edit/main/Content%20(2023)/NumPy.md#3-variable-equation-solver-without-nplinalgsolve)
  ![image](https://user-images.githubusercontent.com/55890376/210096454-63b3373a-b843-482b-9504-c70dfb7544b3.png)

## 3 variable equation solver (using np.linalg.solve)
```
'''
Solving system of lineear equation
x + 2y - z = 2
x - y + 2z = 5
x + y + z  = 6
'''
import numpy as np
A = np.matrix(np.array(
    [[1,2,-1],
     [1,-1,2],
     [1,1,1]]
    ))

B = np.matrix(np.array(
    [[2],
     [5],
     [6]]
    ))

print("MAtrix A",A,sep="\n")
print("Matrix B",B,sep="\n")

X = np.linalg.solve(A, B)
print("Solution of linear equation \n",X)
```
### [Output](https://github.com/SDI-bit/Data-Science/edit/main/Content%20(2023)/NumPy.md#3-variable-equation-solver-using-nplinalgsolve)
  ![image](https://user-images.githubusercontent.com/55890376/210096524-149d193d-2e7d-46a5-bf79-d596cd2916e7.png)
  
## 4 variable equation solver (using np.linalg.solve)
```
"""
Solving system of lineear equation
  w + x -3y + z = 2
-5w + 3x - 4y + z = 0
  w +    2y - z = 1
  w + 2x        = 12
"""

import numpy as np
A = np.array(
    [[1,1,-3,1],
     [-5,3,-4,1],
     [1,0,2,-1],
     [1,2,0,0]])

B = np.array(
    [[2],
    [0],
    [1],
    [12]])

print("MAtrix A\n",A,"\n",sep="\n")
print("Matrix B\n",B,"\n",sep="\n")

X = np.linalg.solve(A,B)
print("Solution of sys of linear equation\n",X)
```
### [Output](https://github.com/SDI-bit/Data-Science/edit/main/Content%20(2023)/NumPy.md#4-variable-equation-solver-using-nplinalgsolve)
  ![image](https://user-images.githubusercontent.com/55890376/210096891-a7ad6a4b-2d25-459b-965a-0de5d9baa4cf.png)

## Custom equation solver
```
import numpy as np
n = int(input("enter no of variables : "))
a=[]
b=[]

print("Input Matrix A")
for i in range(0,n):
    print("Enter equation ",i+1,"variable coefficients\n")
    for j in range(0,n):
        a.append(int(input()))

print("\nInput Matrix  B\n")        
for i in range(0,n):
    b.append(int(input()))

A = np.array(a).reshape(n,n)
B = np.array(b).reshape(n,1)
print("\n    Matrix A   \n")
print(A)
print("\n    Matrix B   \n")
print(B)

if np.linalg.det(A)!=0:
    X = np.linalg.solve(A,B)
    print("\nsolution of system of equation\n")
    print(X)
else:
    print("Matrix A is singular matrix \nNo solution")
```
### [Output](https://github.com/SDI-bit/Data-Science/edit/main/Content%20(2023)/NumPy.md#custom-equation-solver)
  ![Screenshot_20221230_233617](https://user-images.githubusercontent.com/55890376/210100578-16dfbed3-4506-4aa2-bf72-e09034683aee.png)
