# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in 5
# out [10, 2, 3, 8, 9]
# 22


import random
def get_numbers(count):
    ls = random.sample(range(count), count)
    return ls

def get_list_sum(list, count):
    sum = 0
    for i in range(0, count, 2):
        sum += list[i]
    return sum

amount_of_numbers = int(input("Введите требуемое количество чисел: "))
list_of_numbers = get_numbers(amount_of_numbers)
print(f"Ваш список: {list_of_numbers}")
print(f"Сумма чисел, стоящих на нечетных позициях, равна: {get_list_sum(list_of_numbers, amount_of_numbers)}")
