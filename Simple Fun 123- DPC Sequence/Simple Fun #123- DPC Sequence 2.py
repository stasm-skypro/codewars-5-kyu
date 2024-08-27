#!/usr/bin/env python3

"""Задание
Вам выдается строка, состоящая из "D", "P" and "C". Положительное целое число N называется DPC
этой строки, если оно удовлетворяет следующим свойствам:

For each i = 1, 2, ... , size of the string:

Если i-й символ - "D", то N должно делиться на i
Если i-й символ - "P", то N и i должны быть взаимно простыми
Если i-й символ - "C", то N не должно делиться на i.
                           и не быть взаимно простым с i
Ваша задача - найти наименьший DPC в заданной строке или вернуть -1, если таковой нет. Результат
гарантирован <= 10^9.

Пример
Для s = "DDPDD" результат должен быть 20.

"DDPDD" означает, что N должно divided by 1,2,4,5 и N,3 должно быть относительно простым.
Наименьшее число N должно быть 20.

Ввод / вывод
[input] строка s
Данная строка

[resput] целое число,
наименьшее значение DPC из s или -1, если оно не существует.
"""
# from math import lcm, gcd


def is_dpc_a1(s: str):
    d = set(i + 1 for i, ch in enumerate(s) if ch == "D")
    p = set(i + 1 for i, ch in enumerate(s) if ch == "P")
    c = set(i + 1 for i, ch in enumerate(s) if ch == "C")

    def fd(n, d):
        flag = 1
        for i in d:
            flag = flag * (n % i == 0)
            if flag == 0:
                break
        return flag

    def fp(n, p):
        flag = 1
        for i in p:
            flag = flag * (gcd(n, i) == 1)
            if flag == 0:
                break
        return flag

    def fc(n, c):
        flag = 1
        for i in c:
            flag = flag * (n % i != 0) * (gcd(n, i) != 1)
            if flag == 0:
                break
        return flag

    n = 2
    CACHE = set()
    while n <= 1_000_000_000:
        if fd(n, d) and fp(n, p) and fc(n, c):
            CACHE.add(n)
        if CACHE:
            return min(CACHE)

        n = n + 1
    return -1


def is_dpc_rc1(s):
    d = set(i + 1 for i, ch in enumerate(s) if ch == "D")
    p = set(i + 1 for i, ch in enumerate(s) if ch == "P")
    c = set(i + 1 for i, ch in enumerate(s) if ch == "C")

    N = 1
    for i in d:
        N = lcm(N, i)

    for i in p:
        if gcd(N, i) != 1:
            return -1

    for i in c:
        if gcd(N, i) in (1, i):
            return -1

    return N


def is_dpc(s):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    # def gcd(a, b):
    #     if b == 0:
    #         return a
    #     else:
    #         return gcd(b, a % b)

    def lcm(a, b):
        greater = max(a, b)
        while True:
            if (greater % a == 0) and (greater % b == 0):
                lcm = greater
                break
            greater += 1
        return lcm

    N = 1
    for i, ch in enumerate(s, 1):
        if ch == "D":
            N = lcm(N, i)
        elif ch == "P":
            if gcd(N, i) != 1:
                return -1
        elif ch == "C":
            if gcd(N, i) in (1, i):
                return -1
    return N


def run():
    func = is_dpc
    tests = [
        (func("DDPDD"), 20),
        (func("DDDDPDDCCCDDPDCCPCDCDDPCPCCDDCD"), 15782844),
        (func("DPCPDPPPDCPDPDPC"), -1),
        (func("DDDDDDCD"), -1),
        (func("PDCDDDDDD"), -1),
        (func("CDDDPDDD"), -1),
        (func("DDDDDDPCCDPDPP"), -1),
    ]
    for t in tests:
        print(["fail", "OK"][t[0] == t[1]], t[0])


if __name__ == "__main__":
    run()
