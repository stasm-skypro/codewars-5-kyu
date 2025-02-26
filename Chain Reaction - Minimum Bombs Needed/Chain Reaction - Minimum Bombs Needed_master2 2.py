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

from collections import defaultdict


def get_min_bombs(grid: list) -> int:
    m, n = len(grid), len(grid[0])

    adjacency = {
        '0': [],
        '+': [(-1, 0), (1, 0), (0, -1), (0, 1)],
        'x': [(-1, -1), (-1, 1), (1, 1), (1, -1)],
    }

    graph = defaultdict(list)
    for i, row in enumerate(grid):
        for j, el in enumerate(row):
            if el == '0':
                continue

            graph[i, j].append((i, j))
            for di, dj in adjacency[el]:
                a, b = i + di, j + dj
                if 0 <= a < m and 0 <= b < n and grid[a][b] != '0':
                    graph[i, j].append((a, b))

    spans = {}
    for root in graph:
        span = set()
        queue = [root]
        while queue:
            node = queue.pop()
            for neighbor in graph[node]:
                if neighbor in spans:
                    span = span |  spans[neighbor]
                elif neighbor not in span:
                    span.add(neighbor)
                    queue.append(neighbor)
        spans[root] = span

    n_components = 0
    while spans:
        n_components += 1
        node, span = max(spans.items(), key=lambda x: x[1])
        for x in span:
            spans.pop(x, None)

    return n_components


def main():
    tests = [
        # ([["+", "+", "0", "+", "+"],
        #   ["+", "+", "+", "+", "+"]], 1),

        ([["+", "+", "+", "0", "+", "+", "+"],
          ["+", "+", "+", "0", "0", "+", "+"]], 2),

        # ([["+", "+", "0", "+", "0", "+", "+", "+"],
        #   ["+", "+", "0", "+", "0", "0", "+", "+"]], 3),

        # ([["+", "0", "+", "0", "+", "0", "+"],
        #   ["+", "+", "+", "+", "+", "+", "+"]], 1),

        # ([["+", "0", "+", "+", "+", "+", "+"],
        #   ["+", "+", "+", "0", "0", "+", "+"]], 1),

        # ([['0', '+', '+', '0', '+', '0', '+'],
        #   ['0', '0', '+', '0', '+', '0', '+'],
        #   ['0', '+', '+', '0', '+', '0', '+']], 3),

        # ([["+", "+", "+", "+", "+", "+", "+"],
        #   ['0', '0', '+', '0', '0', '0', '0'],
        #   ['0', '0', '+', '0', '0', '0', '0'],
        #   ["0", "0", "+", "+", "+", "+", "+"]], 1),

        # ([['+', '+', '0', '+', '+'],
        #   ['+', '0', '+', '0', '+'],
        #   ['+', '+', '0', '+', '+']], 3),

        # ([['+', '+', '+', '0', '+', '+', '+'],
        #   ['+', '+', '+', '0', '+', '+', '+'],
        #   ['+', '+', '0', '+', '+', '+', '+'],
        #   ['+', '+', '+', '0', '+', '+', '+'],
        #   ['+', '+', '+', '+', '0', '+', '+'],
        #   ['+', '+', '+', '+', '0', '+', '+']], 2),

        # ([['+', '+', '+', '0', '+', '+', '+'],
        #   ['+', '+', '+', '0', '+', '+', '+'],
        #   ['+', '+', '0', '+', '0', '+', '+'],
        #   ['+', '+', '+', '0', '+', '+', '+'],
        #   ['+', '+', '0', '+', '0', '+', '+'],
        #   ['+', '+', '0', '+', '+', '+', '+']], 3),

        # ([["x", "0", "x"],
        #   ["x", "x", "x"]], 3),

        # ([["x", "x", "x", "0", "x"],
        #   ["x", "x", "x", "x", "x"],
        #   ["x", "x", "x", "0", "x"]], 3),

        # ([["x", "0", "x"],
        #   ["x", "x", "x"]], 3),

        # ([["x", "x", "x", "0", "x"],
        #   ["x", "x", "x", "x", "x"],
        #   ["x", "x", "x", "0", "x"]], 3),

        # ([['x'],
        #   ['+']], 1),

        # ([['+', '0', 'x', '+'],
        #   ['x', '+', 'x', '+'],
        #   ['x', '0', '+', '0'],
        #   ['0', '+', 'x', 'x'],
        #   ['+', '0', '+', 'x']], 4),

        # ([['x', '+', 'x', '+', '+', '+'],
        #   ['x', 'x', '0', '0', 'x', 'x'],
        #   ['x', '+', 'x', 'x', '0', 'x'],
        #   ['0', 'x', 'x', '0', '+', '+'],
        #   ['+', '+', 'x', '+', '0', '+'],
        #   ['0', '+', '+', 'x', '+', '+']], 2)
    ]
    for t in tests:
        res = get_min_bombs(t[0])
        print(["fail", "passed"][res == t[1]], res)


if __name__ == "__main__":
    main()
