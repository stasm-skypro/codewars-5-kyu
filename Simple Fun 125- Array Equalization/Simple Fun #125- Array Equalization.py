#! /usr/bin/env python3

"""Задача
Вам предоставляется массив 'a' из натуральных чисел и intger 'k'. Вы можете выбрать некоторое целое
число 'X' и обновить 'a' несколько раз, где обновить означает выполнить следующие операции:

выберите непрерывный подмассив длиной не более заданного 'k';
замените все элементы в выбранном подмассиве выбранным 'X'.   

Какое минимальное количество обновлений требуется, чтобы сделать все элементы массива одинаковыми?

Пример
Для a = [1, 2, 2, 1, 2, 1, 2, 2, 2, 1, 1, 1] and k = 2 вывода должно быть 4.

Вот как a будет выглядеть после каждого обновления:

[1, 2, 2, 1, 2, 1, 2, 2, 2, 1, 1, 1] ->
[1, 1, 1, 1, 2, 1, 2, 2, 2, 1, 1, 1] ->
[1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1] ->
[1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1] ->
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

Ввод / вывод
[input] целочисленный массив a
Массив целых положительных чисел.

Ограничения: 10 ≤ a.length ≤ 50, 1 ≤ a[i] ≤ 10.

[input] целое число k
Положительное целое число, максимальная длина подмассива.

Ограничения: 2 ≤ k ≤ 9.

[resput] целое число
Минимальное количество обновлений.
"""


def update_list(lst, k):
    ups = []
    for x in set(lst):
        u, i = 0, 0
        clst = lst.copy()
        while i < len(clst):
            if clst[i] == x:
                i = i + 1
            else:
                end = i + k
                if end > len(clst):
                    end = i + (len(clst) - i)
                for j in range(i, end):
                    clst[j] = x
                u = u + 1
                i = i + k
        ups.append(u)
    return min(ups)


def update_list2(lst, k):
    ups = []
    for x in set(lst):
        cnt, i = 0, 0
        while i < len(lst):
            if lst[i] == x:
                i = i + 1
            else:
                cnt = cnt + 1
                i = i + k
        ups.append(cnt)
    return min(ups)


def run():
    fun = update_list2
    tests = [
        (fun([1, 2, 2, 1, 2, 1, 2, 2, 2, 1, 1, 1], 2), 4),
        (fun([1, 2, 2, 3, 1, 1, 2, 3, 1, 1, 2, 1], 2), 4),
        (fun([1, 2, 2, 3, 1, 2, 2, 3, 2, 1, 2, 1], 2), 5),
        (fun([5, 2, 3, 5, 2, 2, 3, 5, 1, 2, 5, 1, 2, 5, 3], 7), 2),
        (fun([1, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1], 9), 1),
    ]
    for t in tests:
        print(["fail", "OK"][t[0] == t[1]], t[0])


if __name__ == "__main__":
    run()
