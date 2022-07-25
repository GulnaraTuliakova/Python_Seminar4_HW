# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
n = int(input('Введите натуральное число = '))
lst = []
k = 0
for i in range(2, n+1):
    for j in range(2, i):
        if i % j == 0:
            k += 1
    if k == 0:
        lst.append(i)
    else:
        k = 0
print(f'Список простых чисел от 1 до {n}: {lst}')

print(f'Список простых множителей числа {n}: ', end=' ')
while n > 1:
    for i in range(len(lst)):
        if n % lst[i] == 0:
            n = n / lst[i]
            print(lst[i], end='  ')
