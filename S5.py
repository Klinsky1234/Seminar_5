# Задача 0. С помощью анонимной функции найдите в списке на 15 элементов числа, кратные 5.
# Заполните список случайным образом числами от 1 до 100.
import random


def task0():
    n = [random.randint(1, 25) for _ in range(6)]
    print(n)
    n = list(
        filter(lambda x: x % 5 == 0, n)
    )  # not (x%5) - тпа можно было и так вместо x%5==0
    print(n)


# task0()


# Задача 1. На вход подаётся четырёхзначное число. Получите список, состоящий из цифр данного числа,
# увеличенных на 10.
# 9650 –> [19, 16, 15, 10]
# 1043 –> [11, 10, 14, 13]
def task1():
    num = input(
        "Enter number: "
    )  # тут у нас стринг и поэтому можно перебирать поэлементно
    numbers = [int(letter) for letter in num]
    print(numbers)
    numbers = list(map(lambda x: x + 10, numbers))
    print(numbers)


# task1()


# Задача 2. В зоопарк отправили отчёт о новом поступлении зверей с ошибкой,
# в результате которой некоторые данные не расшифровались.
# Расшифруйте данные. Определите, в какой клетке находится лев. Номер клетки совпадает с номером строки.
# абвгдеёжзийклмнопрстуфхцчшщъыьэюя
def ToBinary(num):
    result = ""
    while num > 0:
        result = str(num % 2) + result
        num //= 2
    return "0" * (6 - len(result)) + result


def decoder(code):
    animal = [code[i : i + 6] for i in range(0, len(code), 6)]
    # print(animal)


def task2():
    animals = [
        "010100001100001001010011001011000000",
        "000001011100001011",
        "001011001111010011",
        "010010010011001111010001001111000111",
        "001100000101000010",
        "001011010001001111001100001001001011",
        "001101010100001100",
        "000001000000010001010010010100001011",
        "000011000101010000000000010001000100",
        "010010001111001101",
        "010010001111000001000000001011000000",
        "011000001001000111",
    ]
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    alphabet = list(alphabet)
    d = {}
    for i in range(len(alphabet)):
        d[ToBinary(i)] = alphabet[i]
    print(d)
    result = list(
        map(lambda x: [d[x[i : i + 6]] for i in range(0, len(x), 6)], animals)
    )
    result = list(map(lambda x: "".join(x), result))
    print(result)


# task2()

# Задача 1. Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5.
#  Используйте для решения лямбда-функцию. 2, 3, 4, 6, 7, 8 -> 6, 7, 8


def S5_HW1():
    n = [random.randint(1, 10) for _ in range(10)]
    print(n)
    n = list(filter(lambda x: x > 5, n))
    print(n)


# S5_HW1()

# Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа,
# описывающие случайную возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] =>[1, 2, 3] или [2, 7] или [4, 6, 7] и т.д.

Dlina = 10
n = [random.randint(1, 10) for i in range(Dlina)]
# print(n)


def new_list(n):
    m = [n[0]]
    for i in n:
        if i > max(m):
            m.append(i)
    return m


# print(new_list(n))

# Задача 3. Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего совпадающих элементов есть в списке.
# Удалите все повторяющиеся элементы. [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают
# Список уникальных элементов [1, 4, 2, 3, 6, 7]


def S5_HW3():
    n = [random.randint(1, 25) for i in range(16)]
    print(f"Полный список -> {n}")
    m = list(set(n))
    print(f"Уникальный список -> {m}")
    diff = len(n) - len(m)
    print(f"{diff} -> элемента(ов) совпадают")


# S5_HW3()
