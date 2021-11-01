from random import randint
from itertools import cycle

lst = [randint(-5, 5) for _ in range(3)]
print(lst)

stop = int(input('Введите количество повторов: '))
count = 1
for i in cycle(lst):
    if count > stop:
        break
    print(i)
    count += 1