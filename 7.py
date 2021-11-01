def fact(x):
    a = 1
    for i in range(1, x+1):
        a *= i
        yield a

n = int(input('Введите целое пололжительное число: '))
for elem in fact(n):
    print(elem)