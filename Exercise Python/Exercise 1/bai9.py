import numpy as np
from numpy import *
import random
print("Nhap vao so m: ")
m = int(input())
print("Nhap vao so n: ")
n = int(input())
A = np.random.randint(100, size=(m, n))
C = np.insert(A,n, 20, axis=1)
D = np.insert(C,m, 10, axis=0)
E = delete(C,n,axis=1)
F = delete(D,m,axis=0)
print("A = \n", A)
print("\nC =\n", C)
print("\nD =\n", D)
print("\nSize: ", np.size(D, 1), "x", np.size(D, 0))
print("\nE =\n", E)
print("\nF =\n", F)