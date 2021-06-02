import numpy as np
print("Nhap vao so m: ")
m = int(input())
print("Nhap vao so n: ")
n = int(input())
a  = np.random.randint(100, size=(m, n))
a_t = np.transpose(a) #Create transpose of a
print("Ma tran a: ",a)
print("\nTranspose matrix a: \n",a_t)