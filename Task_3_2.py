# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in 4
# out [2, 5, 8, 10] [20, 40]

import random
def get_numbers(count):
    ls = random.sample(range(count), count)
    return ls

def find_product_pairs(list, count):
    product = []
    for i in range(int(count/2)):
        product.append(list[i]*list[-(i+1)])
    return product


amount_of_numbers = int(input("Введите требуемое количество чисел: "))
list_of_numbers = get_numbers(amount_of_numbers)
print(f"Ваш список: {list_of_numbers}")
print(f"Произведение пар чисел списка: {find_product_pairs(list_of_numbers, amount_of_numbers)}")