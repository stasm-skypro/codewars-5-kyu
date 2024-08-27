#!/usr/bin/env python3

from time import perf_counter
cnt = 0


def the_bee(n):
    # Найдём количество ячеек m для заданного числа рёбер n.
    m = 1
    for i in range(1, n + 1):
        m = m + 6 * (i - 1)
    # Построим матрицу смежности, соотвествующую найденному значению m.
    adjacency_matrix = [[0, 0, 0, 1, 1, 1, 0],
                        [1, 0, 1, 0, 0, 0, 1],
                        [1, 0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 1, 0, 0],
                        [1, 0, 0, 0, 0, 1, 0]]
    start_pos = 1
    final_pos = 4
    visited = [0] * m

    # Поиск в глубину.
    def dfs(a, visited, m, start, finish):
        if start == finish:
            return True
        visited[start] = 1
        for i in range(m):
            for j in range(m):
                if a[i][j] == 1 and visited[i] == 0:
                    if dfs(a, visited, m, i, finish):
                        return True
        return False

    res = dfs(adjacency_matrix, visited, m, start_pos, final_pos)
    print(res)
    return


def main():
    start = perf_counter()
    tests = [
        (the_bee(2), 11),
        # (the_bee(3), 291),
        # (the_bee(5), 259123),
        # (the_bee(20), 11419120154603538332020717795),
        # (the_bee(33), 706829476133138423874525925298446150375545319299),
        # (the_bee(50), 61068096560504518254246449553519425203436341865056944755649047832571626123),
    ]
    for t in tests:
        print(['fail', 'OK'][t[0] == t[1]])
    print(f">>>code runs in: {(perf_counter() - start):.06f}")


if __name__ == "__main__":
    main()
