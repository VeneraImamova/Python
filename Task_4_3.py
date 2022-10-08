# 3. Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной
# последовательности в том же порядке.
# in 7
# out
# [4, 5, 3, 3, 4, 1, 2]
#
import random
def get_rand_numbers(count):
    if count < 0:
        print("Нельзя вводить отрицательные числа!")
        return []

    list_nums = [random.randint(0, count*2) for i in range(count)]
    return list_nums

def get_list_numbers(number_list):
    new_list = []
    dict_copy_numbers = {}.fromkeys(number_list, 0)
    for i in number_list:
        dict_copy_numbers[i] += 1

    for k in dict_copy_numbers:
        if dict_copy_numbers[k] == 1:
            new_list.append(k)

    return new_list


number = int(input("Введите требуемое количество чисел: "))
list_of_numbers = get_rand_numbers(number)
print(f"Ваш список: {list_of_numbers}")
print(f"Список неповторяющихся элементов: {get_list_numbers(list_of_numbers)}")