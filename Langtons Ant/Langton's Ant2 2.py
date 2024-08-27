#!/usr/bin/env python3
"""Задача
Завершите функцию и верните n-ю итерацию муравья Лэнгтона с заданными входными данными.

Параметры:
grid - двумерный массив 1s и 0s (представляющих белые и черные ячейки соответственно)
column - горизонтальное положение муравья
row - вертикальное положение муравья
n - количество итераций
dir - текущее направление муравья (0 - север, 1 - восток, 2 - юг, 3 - запад), должно по умолчанию
равняться 0.
Примечание: параметры column и row всегда будут внутри grid, а количество поколений n никогда
не будет отрицательным.
Вывод
Состояние итераций grid после n выполнения.

Правила
Муравей может перемещаться в любом из четырех основных направлений на каждом своём шаге.
Муравей движется в соответствии с приведенными ниже правилами:
У белого квадрата (обозначенного 1) поверните на 90 ° вправо, измените цвет квадрата и продвиньтесь
на одну единицу вперед. У черного квадрата (0) поверните на 90 ° влево, измените цвет квадрата
и продвиньтесь на одну единицу вперед.
Сетка не имеет ограничений, и поэтому, если муравей выходит
за границы, сетку следует расширить на 0s, соответственно сохраняя форму прямоугольника.

Пример
ant([[1]], 0, 0, 1, 0)   # should return: [[0, 0]]
Изначально обращенный на север (0), на первой итерации муравей поворачивает направо (потому что он
стоит на белом квадрате, 1), переворачивает квадрат и движется вперед."""


def get_ant_pos(board, c, r, n, dir):
    def board_to_maps2(lst):
        """Convert list in to dict."""
        dic = dict()
        for i, row in enumerate(lst):
            for j, el in enumerate(row):
                dic[(i, j)] = el
        return dic

    def get_idx(dic: dict):
        """Creat two lists with item indexes: one for rows, one for columns."""
        ridx = []
        cidx = []
        for k in dic.keys():
            ridx.append(k[0])
            cidx.append(k[1])
        return ridx, cidx

    def recalc_idx(lst_idx, shift):
        """Recalculate indexes if indexes are less to zero."""
        for i, _ in enumerate(lst_idx):
            lst_idx[i] = lst_idx[i] + shift
        return lst_idx

    def renew_keys(src, keys: list):
        """Renews the maps keys."""
        res = dict(zip(keys, list(src.values())))
        return res

    def maps_to_board2(dic: dict):
        """Convert dict to list."""
        ridx, cidx = get_idx(dic)
        rmax, cmax = max(ridx), max(cidx)
        lst = [[0] * (cmax + 1) for _ in range(rmax + 1)]
        for k, v in dic.items():
            i, j = k
            lst[i][j] = v
        return lst

    maps = board_to_maps2(board)

    from collections import deque
    increments = deque([(-1, 0), (0, -1), (1, 0), (0, 1)])
    if dir in [1, 2, 3]:
        increments.rotate(dir)

    for k in range(1, n + 1):
        pos = r, c
        val = maps[pos]
        maps[pos] = int(not val)
        increments.rotate(1) if val == 1 else increments.rotate(-1)
        (dr, dc) = increments[0]
        r, c = r + dr, c + dc
        pos = (r, c)
        if pos not in maps:
            maps[pos] = 0

    ridx, cidx = get_idx(maps)
    rmin, rmax = min(ridx), max(ridx)
    cmin, cmax = min(cidx), max(cidx)

    if rmin < 0:
        rshift = abs(rmin)
        ridx = recalc_idx(ridx, rshift)

    if cmin < 0:
        cshift = abs(cmin)
        cidx = recalc_idx(cidx, cshift)

    maps = renew_keys(maps, zip(ridx, cidx))

    board = maps_to_board2(maps)
    return board


def run():
    """Runs main script."""

    fun = get_ant_pos
    tests = [
        (fun([[1]], 0, 0, 1, 0), [[0, 0]]),
        (fun([[0]], 0, 0, 1, 0), [[0, 1]]),
        (fun([[1]], 0, 0, 3, 0), [[0, 1], [0, 1]]),
        (fun([[1]], 0, 0, 1, -1), [[0, 0]]),
        (fun([[1, 0, 1],
              [0, 1, 0],
              [1, 0, 1], ], 1, 1, 5, 0), [[0, 0, 0, 1],
                                          [1, 0, 0, 1],
                                          [0, 0, 1, 0],
                                          [1, 0, 1, 0], ]),
        (fun([[1, 0, 0, 0, 1, 0, 1, 0, 1],
              [1, 1, 1, 1, 0, 0, 0, 1, 1],
              [0, 1, 0, 1, 1, 1, 1, 0, 1], ], 5, 2, 16, 3), [[0, 0, 0, 0, 0, 0, 1, 1, 0],
                                                             [1, 0, 0, 0, 1, 0, 1, 1, 1],
                                                             [1, 1, 1, 0, 0, 0, 1, 1, 1],
                                                             [0, 1, 0, 0, 1, 1, 1, 0, 1], ]),
    ]
    for t in tests:
        print(['fail', 'OK'][t[0] == t[1]], t[0])


if __name__ == "__main__":
    run()
