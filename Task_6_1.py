# 1. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента. Use comprehension.
# in 9
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]
# in
# 10
# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

import random
def get_numbers(count):
    return random.sample(range(count*3), count)

def get_next_max_list(list):
    return [list[i] for i in range(1, len(list)) if list[i] > list[i-1]]




number = int(input("Введите требуемое количество элементов: "))
first_list = get_numbers(number)
print(f"Исходный список: {first_list}")
print(f"Обработанный список: {get_next_max_list(first_list)}")