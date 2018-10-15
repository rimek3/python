__author__ = 'Кузнецов Павел Дмитриевич'

#Задача-1

i = 0
number = input("Введите число:")
while i < 1:
    print(max(number))
    i += 1

#Задача-2

a = input("Введите a:")
b = input("Введите b:")
a, b = b, a
print("a =", a)
print("b =", b)

#Задача-3

import math
print("ax² + bx + c = 0")
a = int(input("Введите значение a:"))
b = int(input("Введите значение b:"))
c = int(input("Введите значение c:"))
D = b ** 2 - 4 * a * c
if D < 0:
    print("Нет корней!")
elif D == 0:
    x1 = (- b) / (2 * a)
    print("Один корень:", x1)
elif D > 0:
    x1 = ((- b) + math.sqrt(D)) / (2 * a)
    x2 = ((- b) - math.sqrt(D)) / (2 * a)
    print("Первый корень:", x1, "Второй корень:", x2)



