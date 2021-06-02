import random
lst_ = []
for i in range(10):
	n = int(random.uniform(0,1000))
	lst_.append(n)
print("Cách 1: ")
print("\nlst_ = \n",lst_)
print("\nSample: \n",random.sample(lst_, 5),"\n")

#Cách 2:
lst = random.sample(range(10, 1000), 5)
lst_f = [x/10 for x in lst]
print("Cách 2: ")
print("\nlst =\n",lst)
print("\nSample: \n",lst_f,"\n")


#Cách 3:
import random

def get_float_list(start, stop, size):
    result = []
    unique_set = set()
    for i in range(size):
        x = round(random.uniform(start, stop),2)
        while x in unique_set:
            x = round(random.uniform(start, stop),2)
        unique_set.add(x)
        result.append(x)

    return result
print("Cách 3: ")
print("\nDanh sách các số ngẫu nhiên duy nhất giữa 100, 1000")
print(get_float_list(100, 1000, 5))