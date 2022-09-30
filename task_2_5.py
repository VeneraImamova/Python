# 5. ** Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

count = int(input("Введите длину числа: "))
list1 = list(range(count))
print("Первоначальный список:", *list1)

import random

list2 = list1.copy()

for i in range(count):
    new = int(random.randint(0, count-1))
    temp = list2[i]
    list2[i] = list2[new]
    list2[new] = temp

print("Новый список:", *list2)
