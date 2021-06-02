import numpy as np 
import random
A  = np.random.randint(100, size=(5, 8))
B  = np.random.randint(100, size=(5, 8))
C  = np.random.randint(100, size=(8, 5))

print('A = \n', A)
print("\nB = \n", B)
print("\nC = \n", C)
print("\nA * 2 = \n", A * 2)
print('\nA – B = \n', A - B)
print('\nA * B = \n', A.dot(C))
print("\nRank of matrix A: ", np.linalg.matrix_rank(A))