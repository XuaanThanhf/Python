import numpy as np
import random
print("Nhap vao so M: ")
m = int(input())
print("Nhap vao so N: ")
n = int(input())
print("Nhap vao so L: ")
l = int(input())

A = np.random.randint(100, size=(m, n))
B = np.random.randint(100, size=(m, l))
C = np.concatenate((A, B),1)

D = np.transpose(A) #Create transpose of a
E = np.transpose(B) #Create transpose of a
F = np.concatenate((D, E))
G = np.transpose(F)
print("A = \n", A)
print("\nB = \n", B)
print("\nC = \n", C)
print("\nD = \n", D)
print("\nE = \n", E)
print("\nF = \n", F)
print("\nG = \n", G)