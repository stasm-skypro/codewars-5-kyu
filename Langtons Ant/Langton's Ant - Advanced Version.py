#!/usr/bin/pjthon 3

"""ОПИСАНИЕ:
Это ката основано на задаче проекта Эйлера № 349. Возможно, вы захотите начать с решения этого ката
в первую очередь.
Описание.
Муравей Лэнгтона движется по обычной сетке из квадратов, окрашенных либо в черный, либо в белый
цвет. Муравей всегда ориентирован в одном из основных направлений (влево, вправо, вверх или вниз)
и движется в соответствии со следующими правилами:
Если он находится на черном квадрате, он меняет цвет квадрата на белый, поворачивается на
90 градусов против часовой стрелки (влево) и перемещается на один квадрат вперед.
Если он находится на белом квадрате, он меняет цвет квадрата на черный, поворачивается на
90 градусов по часовой стрелке (вправо) и перемещается на один квадрат вперед.
Начиная с полностью белой сетки, сколько квадратов становятся черными после n ходов муравья?
Примечание: n будет увеличено до 1020."""


def run_langton_a01(n):
    """Нормально работает до n=10_000. Алгоритм не работает на больших n>=100000."""
    # изначально муравей в белом квадрате - 0, чёрный квадрат - 1
    N = 2000
    field = [[0] * N for _ in range(N)]
    cdir = "u"
    cnt = 0
    i, j = N // 2, N // 2
    pos = (i, j)  # Текущие координаты (i, j)
    k = 0
    while k < n:
        (i, j) = pos
        if field[i][j] == 0:
            field[i][j] = 1
            cnt = cnt + 1
            if cdir == "u":
                cdir = "f"
                j = j + 1
            elif cdir == "f":
                cdir = "d"
                i = i + 1
            elif cdir == "d":
                cdir = "b"
                j = j - 1
            elif cdir == "b":
                cdir = "u"
                i = i - 1
            pos = i, j

        else:
            field[i][j] = 0
            cnt = cnt - 1
            if cdir == "u":
                cdir = "b"
                j = j - 1
            elif cdir == "b":
                cdir = "d"
                i = i + 1
            elif cdir == "d":
                cdir = "f"
                j = j + 1
            elif cdir == "f":
                cdir = "u"
                i = i - 1
            pos = (i, j)
        k = k + 1
    return cnt


def run_langton_a02(n):
    """В этом варианте матрица field создаётся динамически на ходу. Но выледает по ошибке
    list index res of range при n=249. Не знаю в чём трабл. Скорее всего на этом значении n
    начинается переход в атрактор и нужно расширять поле по-другому.
    """
    field = [[0] * n * 2 for _ in range(n * 2)]
    field = [[0]]
    cdir = "u"
    cnt = 0
    # i, j = n // 2, n // 2
    i, j = 0, 0
    pos = (i, j)  # Текущие координаты (i, j)
    k = 0
    while k < n:
        (i, j) = pos
        if field[i][j] == 0:
            field[i][j] = 1
            cnt = cnt + 1
            if cdir == "u":
                cdir = "f"
                field[i].append(0)
                j = j + 1
            elif cdir == "f":
                cdir = "d"
                field.append([0] * len(field[i]))
                i = i + 1
            elif cdir == "d":
                cdir = "b"
                if (j - 1) < 0:
                    for p in range(len(field)):
                        field[p].insert(0, 0)
                else:
                    j = j - 1
            elif cdir == "b":
                cdir = "u"
                if (i - 1) < 0:
                    field.insert(0, [0] * len(field[i]))
                else:
                    i = i - 1
            pos = i, j
        else:
            field[i][j] = 0
            cnt = cnt - 1
            if cdir == "u":
                cdir = "b"
                if (j - 1) < 0:
                    for p in range(len(field)):
                        field[p].insert(0, 0)
                else:
                    j = j - 1
            elif cdir == "b":
                cdir = "d"
                field.append([0] * len(field[i]))
                i = i + 1
            elif cdir == "d":
                cdir = "f"
                field[i].append(0)
                j = j + 1
            elif cdir == "f":
                cdir = "u"
                if (i - 1) < 0:
                    field.insert(0, [0] * len(field[i]))
                else:
                    i = i - 1
            pos = (i, j)
        k = k + 1
    return cnt


def run_langton_a03(n):
    """Поле или карту сделал в словаре. Смысл такой: в словаре два ключа: 'b' и 'w' для чёрных
    координат и белых. Т.о. цвет конкретной ячейки определяется ьем, в каком ключе записаны её
    координаты. Поворот и движение муравья реализовал в отдельной функции. Но скорость на 100000
    пдает и алгоритм зависает."""
    pos = (0, 0)
    cdir = "u"
    maps = {0: [pos], 1: []}
    cnt = 0

    def move(p, d, r):
        (i, j) = p
        if r == "CW":
            if d == "u":
                d = "f"
                j = j + 1
            elif d == "f":
                d = "d"
                i = i + 1
            elif d == "d":
                d = 1
                j = j - 1
            elif d == 1:
                d = "u"
                i = i - 1
        elif r == "CCW":
            if d == "u":
                d = 1
                j = j - 1
            elif d == 1:
                d = "d"
                i = i + 1
            elif d == "d":
                d = "f"
                j = j + 1
            elif d == "f":
                d = "u"
                i = i - 1
        p = (i, j)
        return p, d

    k = 0
    while k < n:
        k = k + 1
        if pos in maps[0]:
            maps[0].remove(pos)
            maps[1].append(pos)
            pos, cdir = move(pos, cdir, "CW")
            if pos not in maps[0] and pos not in maps[1]:
                maps[0].append(pos)
            cnt = cnt + 1
        elif pos in maps[1]:
            maps[1].remove(pos)
            maps[0].append(pos)
            pos, cdir = move(pos, cdir, "CCW")
            if pos not in maps[0] and pos not in maps[1]:
                maps[0].append(pos)
            cnt = cnt - 1

    return cnt


def run_langton_a04(n):
    """Заменил while на for.Алгоритм работает на всех n, но на n>= 100000 - всё равно есть заметная
    задержка времени."""
    from collections import deque

    inc = deque([(1, 0), (0, 1), (-1, 0), (0, -1)])
    pos = (0, 0)
    maps = {0: [pos], 1: []}  # 0 - white color, 1 - black color
    cnt = 0

    for _ in range(n):
        if pos in maps[0]:
            maps[0].remove(pos)
            maps[1].append(pos)
            (x, y) = pos
            inc.rotate(1)
            (dx, dy) = inc[0]
            pos = (x + dx, y + dy)
            if pos not in maps[0] and pos not in maps[1]:
                maps[0].append(pos)
            cnt = cnt + 1
        elif pos in maps[1]:
            maps[1].remove(pos)
            maps[0].append(pos)
            (x, y) = pos
            inc.rotate(-1)
            (dx, dy) = inc[0]
            pos = (x + dx, y + dy)
            if pos not in maps[0] and pos not in maps[1]:
                maps[0].append(pos)
            cnt = cnt - 1

    return cnt


LIMIT = 11000
CACHE = [0]

def precalc_a01():
    """Видимо есть секрет, который знают только математики. Нужно сделать расчёты для n до 11000
    включительно. Затем появляется периодичность, которую можно использовать. Функция precflc
    делает вычисления для всех n до 11000 включительно и записывает результат в CACHE (список).
    """
    pos = (0, 0)
    cdir = "u"
    maps = {"w": [pos], "b": []}
    cnt = 0

    def move(p, d, r):
        (i, j) = p
        if r == "CW":
            if d == "u":
                d = "f"
                j = j + 1
            elif d == "f":
                d = "d"
                i = i + 1
            elif d == "d":
                d = "b"
                j = j - 1
            elif d == "b":
                d = "u"
                i = i - 1
        elif r == "CCW":
            if d == "u":
                d = "b"
                j = j - 1
            elif d == "b":
                d = "d"
                i = i + 1
            elif d == "d":
                d = "f"
                j = j + 1
            elif d == "f":
                d = "u"
                i = i - 1
        p = (i, j)
        return p, d

    for _ in range(LIMIT + 1):
        if pos in maps["w"]:
            maps["w"].remove(pos)
            maps["b"].append(pos)
            pos, cdir = move(pos, cdir, "CW")
            if pos not in maps["w"] and pos not in maps["b"]:
                maps["w"].append(pos)
            cnt = cnt + 1
        elif pos in maps["b"]:
            maps["b"].remove(pos)
            maps["w"].append(pos)
            pos, cdir = move(pos, cdir, "CCW")
            if pos not in maps["w"] and pos not in maps["b"]:
                maps["w"].append(pos)
            cnt = cnt - 1
        CACHE.append(cnt)


def precalc_a02():
    """Задача - максимально оптимизировать по времени. В словаре maps заменить строковые ключи на
    числовые. И второе, более важное, переписать функцию move() или вообще избавится от неё.
    """
    from collections import deque

    inc = deque([(1, 0), (0, 1), (-1, 0), (0, -1)])
    pos = (0, 0)
    maps = {0: [pos], 1: []}  # 0 - white color, 1 - black color
    cnt = 0
    for _ in range(LIMIT + 1):
        if pos in maps[0]:
            maps[0].remove(pos)
            maps[1].append(pos)
            (x, y) = pos
            inc.rotate(1)
            (dx, dy) = inc[0]
            pos = (x + dx, y + dy)
            if pos not in maps[0] and pos not in maps[1]:
                maps[0].append(pos)
            cnt = cnt + 1
        elif pos in maps[1]:
            maps[1].remove(pos)
            maps[0].append(pos)
            (x, y) = pos
            inc.rotate(-1)
            (dx, dy) = inc[0]
            pos = (x + dx, y + dy)
            if pos not in maps[0] and pos not in maps[1]:
                maps[0].append(pos)
            cnt = cnt - 1
        CACHE.append(cnt)


def precalc():
    from collections import deque

    inc = deque([(1, 0), (0, 1), (-1, 0), (0, -1)])
    pos = (1, 0)
    blacks = set()

    for _ in range(LIMIT + 1):
        if pos not in blacks:
            blacks.add((pos))
            (x, y) = pos
            inc.rotate(1)
            (dx, dy) = inc[0]
            pos = (x + dx, y + dy)
        else:
            blacks.remove(pos)
            x, y = pos
            inc.rotate(-1)
            (dx, dy) = inc[0]
            pos = (x + dx, y + dy)
        CACHE.append(len(blacks))


def run_langton(n):
    """Затем основнрой алгоритм досчитывает значения для других n больших 11000."""
    precalc()
    if n < LIMIT:
        return CACHE[n]
    # a(n+104) = a(n) + 12 for n > 9976
    x = (n - LIMIT) // 104 + 1
    return CACHE[n - x * 104] + x * 12


def main():
    fun = run_langton
    tests = [
        # (fun(0), 0),
        # (fun(1), 1),
        # (fun(2), 2),
        # (fun(3), 3),
        # (fun(4), 4),
        # (fun(5), 3),
        # (fun(6), 4),
        # (fun(10), 6),
        (fun(14), 10),
        # (fun(15), 9),
        # (fun(18), 6),
        # (fun(19), 7),
        # (fun(20), 6),
        # (fun(100), 20),
        # (fun(248), 46),
        # (fun(1000), 118),
        # (fun(10000), 720),
        # (fun(11000), 834),
        (fun(100000), 11108),
        # (fun(1000000), 114952),
        (fun(10000000), 1153412),
    ]
    for t in tests:
        print(["fail", "OK"][t[0] == t[1]], t[0])


if __name__ == "__main__":
    main()
