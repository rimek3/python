#Задача-1
import math

m = [16, 25, 3, -4, 6, 9]
n = []
for i in m:
    if i > 0 and math.sqrt(i) % 1 == 0:
        n.append(int(math.sqrt(i)))
print(n)

#Задача-2
#Не понял как выполнить задание

#Задача-3
import random

a = int(input("Кол-во случайных элементов: "))
m = []
for i in range(a):
    m.append(random.randint(-100, 100))
print(m)

#Задача-4

m = [1 , 2, 4, 5, 6, 2, 5, 2]
n = set(m)
print(n)

m = [1 , 2, 4, 5, 6, 2, 5, 2]
n = []
for i in m:
    if m.count(i) == 1:
        n.append(i)
print(n)



