from random import randint

lst_1 = [randint(-10, 10) for _ in range(20)]
print(lst_1)

lst_2 = [j for j in lst_1 if lst_1.count(j) == 1]
print(lst_2)