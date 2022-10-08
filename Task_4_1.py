# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
# out
# 9.000000

from decimal import Decimal
def get_accuracy_number (number, accuracy):
    number = Decimal(number)
    number = number.quantize(Decimal(accuracy))
    return number

number = input("Введите число: ")
accuracy = input("Введите требуемую точность: ")


print(f"Ваше число: {get_accuracy_number(number, accuracy)}")
