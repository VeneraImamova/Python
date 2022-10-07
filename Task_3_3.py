# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
# in 88
# out 1011000


def get_binary(number):
    binary = []
    while number/2 != 0:
        binary.append(int(number % 2))
        number = int(number/2)
    binary = binary[::-1]
    return binary



decimal_number = int(input("Введите десятичное число: "))
print(f"Двоичное число: {''.join(map(str, get_binary(decimal_number)))}")
