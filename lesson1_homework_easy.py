__author__ = 'Кузнецов Павел Дмитриевич'

#Задача-1

N = input("Введите случайное целое число:")
a = 0
while a < len(N):
    print(N[a])
    a += 1

#Задача-2

a = input("Введите a:")
b = input("Введите b:")
c = a
d = b
print("a =", d)
print("b =", c)

#Задача-3

access = 0
age = int(input("Введите ваш возраст:"))
if age >= 18:
   access = 1
   print("Доступ разрешен")
else:
   print("Извините, пользование данным ресурсом только с 18 лет")