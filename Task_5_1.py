# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

from random import sample

def make_sentence(count):
    sentense = []
    for i in range(count):
        sentense.append("".join(sample('абв', 3)))
    return " ".join(sentense)

def delete_elements(list: str) -> str:
    if 'абв' not in list:
        print("Такого элемента нет")
    else:
        return list.replace(" абв", "")


random_list = make_sentence(int(input("Введите количество слов: ")))
print(f"Случайный список: {random_list}")
new_list = delete_elements(random_list)
print(f"Новый список: {new_list}")


