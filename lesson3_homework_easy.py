__author__ = 'Кузнецов Павел Дмитриевич'

#Задача-1

def my_round(number, ndigits):
    number = number * (10 ** ndigits) + 0.34
    number = number // 1
    return number / (10 ** ndigits)


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

#Задача-2

def lucky_ticket(ticket_number):
    n = str(ticket_number)
    n = [int(i) for i in n]
    if sum(n[3:]) == sum(n[:3]):
        return "Lucky"
    else:
        return "Unlucky"


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
