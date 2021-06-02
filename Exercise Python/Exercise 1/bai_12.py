#Viết chương trình python nhập vào ma trận có kích cỡ (3xM)x(6xM)
import numpy as np
print("Nhap vao so m: ")
m = int(input())
A = np.arange(36).reshape(3, 6,m)
print("A = n", A)
print("B = \n", np.reshape(A, (9, 2,m)))
