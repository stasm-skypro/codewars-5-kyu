#! /usr/bin/env python3

"""ОПИСАНИЕ:
Числа Фибоначчи - это числа в следующей целочисленной последовательности (Fn):
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...
таких как
F (n) = F (n-1) + F (n-2) с F (0) = 0 и F (1) = 1.
Учитывая число, скажем, prod (для продукта), мы ищем два числа Фибоначчи F (n) и F (n + 1), проверяя
F (n) * F (n + 1) = результат.
Ваша функция productFib принимает целое число (prod) и возвращает массив:
[F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)
в зависимости от языка, если F (n) * F(n+1) = prod.
Если вы не найдете двух последовательных подтверждающих F (n)F(n) * F(n+1) = prod, вы вернетесь
[F(n), F(n+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)
F (n) - наименьшее из них, такое как F(n) * F(n+1) > prod.
Некоторые примеры возврата:
(зависит от языка)
productFib(714) # should return (21, 34, true),
                # since F(8) = 21, F(9) = 34 and 714 = 21 * 34

productFib(800) # should return (34, 55, false),
                # since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55
-----
productFib(714) # should return [21, 34, true],
productFib(800) # should return [34, 55, false],
-----
productFib(714) # should return {21, 34, 1},
productFib(800) # should return {34, 55, 0},
-----
productFib(714) # should return {21, 34, true},
productFib(800) # should return {34, 55, false},
Примечание:
Вы можете увидеть примеры для вашего языка в разделе "Примеры тестов"."""


def product_fib(prod):
    a, b = 0, 1
    while a * b < prod:
        a, b = b, a + b
    return [a, b, a * b == prod]


def main():
    tests = [
        (product_fib(714), [21, 34, True]),
        (product_fib(4895), [55, 89, True]),
        (product_fib(5895), [89, 144, False]),
        (product_fib(800), [34, 55, False]),
    ]

    for t in tests:
        print(['failed', 'passed'][t[0][2] == t[1][2]], t[0])


if __name__ == "__main__":
    main()
