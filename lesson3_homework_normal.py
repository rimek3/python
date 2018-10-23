__author__ = 'Кузнецов Павел Дмитриевич'

#Задача-1

def fibonacci(n, m):
    a, b = 1, 1
    f = [1, 1]
    for i in range(m):
        a, b = b, a + b
        f.append(a)
    return f[n:m]

print(fibonacci(1, 15))

#Задача-2

#sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

list1 = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]

def sort_to_max(origin_list):
    last_item = len(origin_list) - 1
    for z in range(0, last_item):
        for x in range(0, last_item):
            if origin_list[x] > origin_list[x+1]:
                origin_list[x], origin_list[x+1] = origin_list[x+1],  origin_list[x]

    return origin_list

new_list = sort_to_max(list1).copy()
print("New list:  ", new_list)

#Задача-3

def my_filter(a, b):

    my_list = list()
    for i in b:
        if a(i) == True:
            my_list.append(i)
        else:
            continue
    return my_list


print(my_filter((lambda x: x > 2), b=[3, 1, 1, 5, 6, 2, 8]))






