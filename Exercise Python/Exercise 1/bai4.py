import random
lst = []
lst_ = []
for i in range(10):
	n = int(random.uniform(0,1000))
	lst_.append(n)
print("lst_ = \n",lst_)
print ("\nchoice lst: \n", random.choice(lst_))