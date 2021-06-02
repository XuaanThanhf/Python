print("Nhap vao so phan tu: ")
p = int(input())
lst = []
for i in range(0,p,1):
	print("Nhap phan tu thu ",i)
	n = input()
	lst.append(n)
print("lst = \n", lst)
lst.insert(0,0)
print("\nlst = \n", lst)
