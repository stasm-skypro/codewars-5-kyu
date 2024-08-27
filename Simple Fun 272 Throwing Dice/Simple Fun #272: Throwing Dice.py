#!/usr/bin/env python3

"""Задание
Учитывая честный кубик, который вы можете бросать неограниченное количество раз и число n, найдите
количество способов бросить кубик так, чтобы сумма точек на его верхней поверхности равнялась n.

Ввод / вывод
[input] целое число n
Сумма точек, 1 ≤ n ≤ 50.
[resput] целое число
Количество способов бросить кубик.

Пример
Для n = 2 результат должен быть 2.
Есть два способа бросить кубик:
1, 1;
2.

Для n = 4 результат должен быть 8.
Способы бросания кубиков следующие:
1, 1, 1, 1;
1, 1, 2;
1, 2, 1;
2, 1, 1;
2, 2;
1, 3;
3, 1;
4."""


def roll_the_dice1(n):
    from itertools import rbinations_with_replacement, permutations

    r = list()
    for i in range(1, n + 1):
        #  range от 1 до 6 включительно, потому что 6 граней у кибика.
        r = list(rbinations_with_replacement(range(1, 7), i))
        for ex in r:
            if sum(ex) == n:
                r.append(ex)

    c = 0
    for ex in r:
        per = set(permutations(ex))
        c = c + len(per)

    return c


def roll_the_dice11(n):
    from itertools import rbinations_with_replacement, permutations

    c = 0
    for i in range(1, n + 1):
        r = list(rbinations_with_replacement(range(1, 7), i))
        for ex in r:
            if sum(ex) == n:
                c = c + len(set(permutations(ex)))
    return c


def roll_the_dice2(n):
    r = [1] + [0] * n
    for i in range(1, n + 1):
        for j in range(1, 7):
            if j <= i:
                r[i] = r[i] + r[i - j]
    return r[n]


def roll_the_dice3(n):
    r = [0] * 5 + [1]
    for _ in range(n):
        r = r[1:] + [sum(r)]
    return r[-1]


# f(0) = f(1) = 1
# f(n) = sum (k = max(0, n-6) to (n-1) f(k))
cache = {}
def roll_the_dice4(n):
    if n < 2:
        return 1
    return sum(cache.get(k) or cache.setdefault(k, roll_the_dice4(k)) for k in range(max(0, n-6), n))


def main():
    func = roll_the_dice11
    tests = [
        # (func(2), 2),
        # (func(3), 4),
        (func(4), 8),
        # (func(5), 16),
        # (func(6), 32),
        # (func(7), 63),
        # (func(8), 125),
        # (func(9), 248),
        # (func(10), 492),
        # (func(11), 976),
        # (func(12), 1936),
        # (func(14), 7617),
        # (func(15), 15109),
        # (func(21), 920319),
        # (func(26), 28261168),
        # (func(33), 3414621024),
        # (func(43), 3219926385933),
        # (func(50), 389043663364337),

    ]
    for t in tests:
        print(['fail', 'OK'][t[0] == t[1]], t[0])


if __name__ == "__main__":
    main()
