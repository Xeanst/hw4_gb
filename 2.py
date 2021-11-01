from random import randint

lst_1 = [randint(-10, 10) for _ in range(20)]
print(lst_1)

lst_2 = [j for i, j in zip(lst_1, lst_1[1:]) if j > i]
print(lst_2)