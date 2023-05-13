# Задача 1. Дано натуральное число N. Напишите метод,
# который вернёт список простых множителей числа N и количество этих множителей.
# 60 -> 2, 2, 3, 5
# N = input("Введите число: ")
# print(N)
# N = int(input("Введите число: "))
# print(N)

N = int(input("Enter num: "))


def S4_HW1(N):
    factors = list()
    divisor = 2
    while divisor <= N:
        if (N % divisor) == 0:
            factors.append(divisor)
            N = N / divisor
        else:
            divisor += 1
    return factors


print(S4_HW1(N))
