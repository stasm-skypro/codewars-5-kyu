#! /usr/bin/env python3

"""ОПИСАНИЕ:
Напишите программу, которая вычислит количество конечных нулей в факториале заданного числа.
N! = 1 * 2 * 3 *  ... * N
Будь осторожен 1000! состоит из 2568 цифр...
Для получения дополнительной информации смотрите: http://mathworld.wolfram.com/Factorial.html
Примеры
zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero
zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros
Подсказка: вы не предназначены для вычисления факториала. Найдите другой способ найти количество
нулей."""
import scipy


def last_zero_clculate1(n: int):
    f = scipy.special.factorial(n, exact=True)
    f = str(f)
    h = str(f).rstrip('0')
    return len(f) - len(h)


def last_zero_clculate2(n: int):
    f = scipy.special.factorial(n, exact=True)
    c = 0
    while f % 10 == 0:
        c = c + 1
        f = f // 10
    return c


def last_zero_clculate(n: int):
    """Решение учителя. Базируется на утверждении о том, что количество нулей в конце факториала
    зависит от количества цифр 2 и 5 в разложении факториала. Цифр 2 однозначно больше, чем цифр 5,
    т.к. многие цифры можно представить как произведение на 2. Значит количество нулей в конце
    факториала зависит от количества цифр 5. Сколько 5-к, столько и нулей!"""
    k = 0  # количество 5-к
    while n:
        n = n // 5
        k = k + n
    return k


def main():
    tests = [
        (0, 0),
        (6, 1),
        (12, 2),
        (30, 7),
        (100000, 24999),
    ]
    func = last_zero_clculate
    for t in tests:
        print(["failed", "passed"][func(t[0]) == t[1]])


if __name__ == "__main__":
    main()
