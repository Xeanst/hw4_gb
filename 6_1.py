from itertools import count

start, stop = (int(i) for i in input('Введите начальное и конечное значения через пробел: ').split())

for i in count(start):
    print(i)
    if i == stop:
        break