#!/usr/bin/env python3

"""ОПИСАНИЕ:
Это продолжение Chain Reaction - Explosions с теми же настройками, но с другим
вкусом. Как и в предыдущей части, вам будет предоставлен прямоугольный массив,
представляющий "карту" с тремя типами пробелов:

Бомбы "+": при активации их взрыв активирует любые бомбы непосредственно над,
под, слева или справа от бомбы "+".
Бомбы "x": при активации их взрыв активирует любые бомбы, размещенные в любом
из четырех диагональных направлений рядом с бомбой "x".
Пустые пробелы "0".

Цель проста: получив карту, верните минимальное количество бомб, которые
необходимо взорвать, чтобы все бомбы были уничтожены в результате цепной
реакции.
Давайте рассмотрим несколько примеров:
[
["+", "+", "+", "0", "+", "+", "+"],
["+", "+", "+", "0", "0", "+", "+"]
]
Для карты выше ответ таков 2; чтобы взорвать все бомбы, вам просто нужно
взорвать одну бомбу "+" в правом кластере и одну в левом кластере.
[
["x", "0", "x"],
["x", "x", "x"]
]
Для карты выше ответ таков 3; очевидно, что достаточно установить три нижние
бомбы "x", и не менее трех бомб будет достаточно.
[
["x", "x", "x", "0", "x"],
["x", "x", "x", "x", "x"],
["x", "x", "x", "0", "x"]
]
Для карты выше ответ таков 3; срабатывание трех крайних правых бомб в среднем
ряду сделает свое дело.

Примеры
min_bombs_needed([
["+", "+", "+", "0", "+", "+", "+"],
["+", "+", "+", "0", "0", "+", "+"]
]) ➞ 2

min_bombs_needed([
["x", "0", "x"],
["x", "x", "x"]
]) ➞ 3

min_bombs_needed([
["x", "x", "x", "0", "x"],
["x", "x", "x", "x", "x"],
["x", "x", "x", "0", "x"]
]) ➞ 3
Примечания
Обратите внимание, что как бомбы "+", так и бомбы "x" имеют "дальность взрыва",
равную 1.
"""

"""MY COMMENT: Реализация алгоритма на основе графа для бомб типа '+' и для бомб типа 'x'."""


def pprint(d: dict) -> None:
    for k in d:
        print(f"{k}: {d[k]}")


def get_min_bombs(a: list) -> int:
    c = 0
    n, m = len(a), len(a[0])

    incr = {
        '0': [],
        '+': [(0, 0), (0, 1), (1, 0), (-1, 0), (0, -1)],
        'x': [(0, 0), (-1, 1), (1, 1), (1, -1), (-1, -1)],
    }

    blowned = dict()
    for i,row in enumerate(a):
        for j,el in enumerate(row):
            pos = i, j
            for d in incr[el]:
                di, dj = d
                i, j = i + di, j + dj
                if n > i >= 0 and m > j >= 0:
                    neighbour = a[i][j]
                    if neighbour != '0':
                        if pos not in blowned:
                            blowned[pos] = []
                        blowned[pos].append((i, j))
                i, j = pos

    blown_area = dict()

    for root in blowned:
        chain = set()
        queue = [root]
        while queue:
            node = queue.pop()
            for neighbor in blowned[node]:
                if neighbor in blown_area:
                    chain = chain | blown_area[neighbor]
                elif neighbor not in chain:
                    chain.add(neighbor)
                    queue.append(neighbor)
        blown_area[root] = chain

    while blown_area:
        c = c + 1
        node, chain = max(blown_area.items(), key=lambda x: x[1])
        for el in chain:
            blown_area.pop(el, None)

    return c


def main():
    tests = [
        ([["+", "+", "0", "+", "+"],
          ["+", "+", "+", "+", "+"]], 1),

        ([["+", "+", "+", "0", "+", "+", "+"],
          ["+", "+", "+", "0", "0", "+", "+"]], 2),

        ([["+", "+", "0", "+", "0", "+", "+", "+"],
          ["+", "+", "0", "+", "0", "0", "+", "+"]], 3),

        ([["+", "0", "+", "0", "+", "0", "+"],
          ["+", "+", "+", "+", "+", "+", "+"]], 1),

        ([["+", "0", "+", "+", "+", "+", "+"],
          ["+", "+", "+", "0", "0", "+", "+"]], 1),

        ([['0', '+', '+', '0', '+', '0', '+'],
          ['0', '0', '+', '0', '+', '0', '+'],
          ['0', '+', '+', '0', '+', '0', '+']], 3),

        ([["+", "+", "+", "+", "+", "+", "+"],
          ['0', '0', '+', '0', '0', '0', '0'],
          ['0', '0', '+', '0', '0', '0', '0'],
          ["0", "0", "+", "+", "+", "+", "+"]], 1),

        ([['+', '+', '0', '+', '+'],
          ['+', '0', '+', '0', '+'],
          ['+', '+', '0', '+', '+']], 3),

        ([['+', '+', '+', '0', '+', '+', '+'],
          ['+', '+', '+', '0', '+', '+', '+'],
          ['+', '+', '0', '+', '+', '+', '+'],
          ['+', '+', '+', '0', '+', '+', '+'],
          ['+', '+', '+', '+', '0', '+', '+'],
          ['+', '+', '+', '+', '0', '+', '+']], 2),

        ([['+', '+', '+', '0', '+', '+', '+'],
          ['+', '+', '+', '0', '+', '+', '+'],
          ['+', '+', '0', '+', '0', '+', '+'],
          ['+', '+', '+', '0', '+', '+', '+'],
          ['+', '+', '0', '+', '0', '+', '+'],
          ['+', '+', '0', '+', '+', '+', '+']], 3),

        ([["x", "0", "x"],
          ["x", "x", "x"]], 3),

        ([["x", "x", "x", "0", "x"],
          ["x", "x", "x", "x", "x"],
          ["x", "x", "x", "0", "x"]], 3),

        ([["x", "0", "x"],
          ["x", "x", "x"]], 3),

        ([["x", "x", "x", "0", "x"],
          ["x", "x", "x", "x", "x"],
          ["x", "x", "x", "0", "x"]], 3),

        ([['x'],
          ['+']], 1),

        ([['+', '0', 'x', '+'],
          ['x', '+', 'x', '+'],
          ['x', '0', '+', '0'],
          ['0', '+', 'x', 'x'],
          ['+', '0', '+', 'x']], 4),

        ([['x', '+', 'x', '+', '+', '+'],
          ['x', 'x', '0', '0', 'x', 'x'],
          ['x', '+', 'x', 'x', '0', 'x'],
          ['0', 'x', 'x', '0', '+', '+'],
          ['+', '+', 'x', '+', '0', '+'],
          ['0', '+', '+', 'x', '+', '+']], 2)
    ]
    for t in tests:
        res = get_min_bombs(t[0])
        print(["fail", "passed"][res == t[1]], res)


if __name__ == "__main__":
    main()
