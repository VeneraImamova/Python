# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# in 8
# out -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21

number = int(input("Введите число: "))

def fibonacci(count):
    list_fibonacci = [1, 0, 1]
    for i in range(count-1):
        new_element = list_fibonacci[2*i+2]+list_fibonacci[2*i+1]
        list_fibonacci.append(new_element)
        if list_fibonacci[0] > 0:
            list_fibonacci = [-new_element] + list_fibonacci
        else:
            list_fibonacci = [new_element] + list_fibonacci
    return list_fibonacci

print(fibonacci(number))
