import random
lst = []
lst_ = []
for i in range(5):
	n = round(random.uniform(0,1000),2)
	lst.append(n)
print("lst = \n",lst)
for i in range(10):
	n = int(random.uniform(0,1000))
	lst_.append(n)
print("\nlst_ = \n",lst_)