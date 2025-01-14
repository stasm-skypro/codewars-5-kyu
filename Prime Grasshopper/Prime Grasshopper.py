#! /usr/bin/env python3

"""ОПИСАНИЕ:
Сколько квадратов может покрыть Чак Норрис за один прыжок? Все!
Кузнечик прыгает вперед в пространстве с одной осью, представленном в виде массива (списка).
Он может охватывать p пробелы за один прыжок, где p - любое простое число.
Grasshopper начинается на любом расстоянии перед начальным элементом массива и заканчивается
на любом расстоянии после последнего элемента массива. Кузнечик никогда не прыгает назад.
Вычислите максимальную сумму значений элементов массива, на которые grasshopper может приземлиться
во время путешествия. Поскольку не существует такого понятия, как максимальное простое число, 
полне возможно, что кузнечик вообще не приземлится ни на один предмет и преодолеет все расстояние
от старта до финиша за один прыжок.
Массив состоит до 5000 элементов в диапазоне от -100 до + 100, поэтому убедитесь, что ваш алгоритм
достаточно быстр.
Для вашего удобства простые числа до 5003 предварительно загружены как PRIMES.
"""


def pryg_pryg(lst: list):
    pass


def run():
    func = pryg_pryg
    tests = [
        (func([-10, 3, 4, 5, 6]), 10),
    ]
    for t in tests:
        print(['fail', 'OK'][t[0] == t[1]])
        

if __name__ == "__main__":
    run()
