# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


import os
path = os.path.join('task04.txt')

with open(path, 'w') as num:
    k = int(input('ВВедите степень числа k = '))

    while k > -2:
        if k > 0:
            m = int(k/2*8+4)
            num.write(f'{m}x*{k} + ')
            k -= 1
        if k == 1:
            m = int(k/2*8+5)
            num.write(f'{m}x + ')
            k -= 1
        if k == 0:
            m = int(k/3+14)
            num.write(str(m))
            k -= 1
        if k == -1:
            num.write(' = 0')
            k -= 1


        
        
   




    