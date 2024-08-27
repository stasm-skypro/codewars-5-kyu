print(set3)

"""ОПИСАНИЕ:
На этот раз мы хотим записать вычисления с использованием функций и получить результаты. Давайте
посмотрим на некоторые примеры:
seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Требования:
Для каждого числа от 0 ("ноль") до 9 ("девять") должна существовать функция
Должна существовать функция для каждой из следующих математических операций: плюс, минус, умножение, деление_by
Каждое вычисление состоит ровно из одной операции и двух чисел
Самая внешняя функция представляет левый операнд, самая внутренняя функция представляет правый операнд
Деление должно быть целочисленным делением. Например, это должно возвращать 2, а не 2.666666...:
eight(divided_by(three()))."""


def zero(p=None): return 0 if p is None else int(p(0))


def one(p=None): return 1 if p is None else int(p(1))


def two(p=None): return 2 if p is None else int(p(2))


def three(p=None): return 3 if p is None else int(p(3))


def four(p=None): return 4 if p is None else int(p(4))


def five(p=None): return 5 if p is None else int(p(5))


def six(p=None): return 6 if p is None else int(p(6))


def seven(p=None): return 7 if p is None else int(p(7))


def eight(p=None): return 8 if p is None else int(p(8))


def nine(p=None): return 9 if p is None else int(p(9))


def plus(oper): return lambda x: x + oper


def minus(oper): return lambda x: x - oper


def times(oper): return lambda x: x * oper


def divided_by(oper): return lambda x: x // oper


def main():
    tests = [
        (seven(times(five())), 35),
        (four(plus(nine())), 13),
        (eight(minus(three())), 5),
        (six(divided_by(two())), 3),
    ]

    for t in tests:
        print(['failed', 'passed'][t[0] == t[1]], t[0])


if __name__ == "__main__":
    main()
