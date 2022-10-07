# Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in 5
# out [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

from random import uniform

def get_numbers(count):
    list_1 = []
    for i in range(count):
        list_1.append(round(uniform(1, count), 2))
    return list_1

def get_another_data(list, count):
    list_2 = []
    for i in range(count):
        list_2.append(round(list[i] % 1, 2))
    print(f"Min: {min(list_2)}  Max: {max(list_2)} Difference: {round((max(list_2) - min(list_2)), 2)}")
    return list_2



amount_of_numbers = int(input("Введите требуемое количество чисел: "))
list_of_numbers = get_numbers(amount_of_numbers)
print(f"Ваш список: {list_of_numbers}")
get_another_data(list_of_numbers, amount_of_numbers)