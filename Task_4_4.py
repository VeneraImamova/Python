# 4.* Задана натуральная степень k. Сформировать случайным образом список коэффициентов (от 0 до 10)
# многочлена, записать в файл полученный многочлен не менее 3-х раз.
# in 9 5 3
#
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0

from random import randint
from random import choice
def get_str(number):
    symbol_list = ["-", "+"]
    with open("temp_1.txt", "a", encoding="utf-8") as output:
        if number <= 0:
            return

        while number > 0:
            arg = randint(0, 10)
            if arg > 0:
                output.write(f"{arg}*x^{number} {choice(symbol_list)} ")
            number = number -1
        else:
            arg = randint(0, 10)
            output.write(f"{arg} = 0 \n")

k = 3
while k > 0:
    get_str(int(input("Введите степень: ")))
    k = k - 1