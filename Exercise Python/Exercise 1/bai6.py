import random
lst = random.sample(range(10, 1000), 10)
print("lst =",lst)
random.shuffle(lst)
print("Shuffle: ",lst)
lst.reverse()
print("Reverse: ",lst)
lst.sort()
print("Sort: ",lst)