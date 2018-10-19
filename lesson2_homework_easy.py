#Задача-1

m = ["яблоко", "банан", "киви", "арбуз"]
for i in range(len(m)):
    print(str(i + 1) + "." + "{:>9}".format(m[i]))

#Задача-2

a = {1, 2, 3, 3, 4, 5}
b = {1, 2, 2, 5}
c = a - b
print(list(c))

#Задача-3

m = [1, 2, 5, 8, 7]
n = []
for i in range(len(m)):
    if m[i] % 2 == 0:
        n.append(m[i] / 4)
    else:
        n.append(m[i] * 2)
print(n)
