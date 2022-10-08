# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# in 54
# out [2, 3, 3, 3]

number = int(input("Введите число: "))

def get_simple_factor(number):
    simple_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                      31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
                      73, 79, 83, 89, 97, 101, 103, 107, 109,
                      113, 127, 131, 137, 139, 149, 151, 157,
                      163, 167, 173, 179, 181, 191, 193, 197, 199]
    simple_factors = []

    for i in range(len(simple_numbers)):
            while number % simple_numbers[i] == 0:
                simple_factors.append(simple_numbers[i])
                number = number / simple_numbers[i]
    return simple_factors

print(f"Список просты множителей: {get_simple_factor(number)}")


