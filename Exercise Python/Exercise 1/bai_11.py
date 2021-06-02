import numpy as np
a = np.eye(5)
a_t = np.transpose(a)
print(a)
if a.all()  == a_t.all():
	print("a la identity matrix.")
else:
	print("a khong phai la identity matrix.")