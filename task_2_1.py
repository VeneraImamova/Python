# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

number = float(input("Введите вещественное число: "))
length = len(str(number))
number = number * 10**length
sum = 0
while number != 0:
    sum += number % 10
    number//= 10
print("Сумма цифр равна: ", int(sum))