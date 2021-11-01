from functools import reduce

lst = [x for x in range(100,1001) if (x % 2 == 0)]
print(lst)

composition = reduce(lambda x,y: x * y, lst)
print(composition)