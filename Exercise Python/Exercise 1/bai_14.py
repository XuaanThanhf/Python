import numpy as np 
import random
print("Nhap vao so m: ")
m = int(input())
A  = np.random.randint(100, size=(5, 8))

print("The original list : \n" + str(A)) 
res = any(m in sub for sub in A)  
print( str(m) + " Is present in Matrix ? : " + str(res)) 


#SV: Nguyễn Xuân Thành
#MSV: 1811505410131
#Exercise 1 còn thiếu bài đủ.