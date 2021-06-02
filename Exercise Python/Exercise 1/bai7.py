import numpy as np
print("Nhap vao so m: ")
m = int(input())
print("Nhap vao so n: ")
n = int(input())
a = np.eye(5)
b  = np.random.randint(100, size=(m, n))
c = np.arange(12).reshape(m, n) #m,n là ước số của 12
print("Identity matrix: ",a)
print("\nNgau nhien: ",b)
print("\nTang dan: ",c)