#! /usr/bin/env python3

"""ОПИСАНИЕ:
Определение: Согласно Википедии, полное двоичное дерево - это двоичное дерево, в котором каждый
уровень, возможно, за исключением последнего, полностью заполнен, а все узлы на последнем уровне
расположены как можно левее". На странице Википедии, упомянутой выше, также упоминается, что
"Двоичные деревья также могут храниться в порядке следования по ширине как неявная структура данных
в массивах, и если дерево является полным двоичным деревом, этот метод не тратит места".
Ваша задача - написать метод (или функцию), который принимает массив (или список, в зависимости от
языка) целых чисел и, предполагая, что массив упорядочен в соответствии с обходом полного двоичного
дерева в порядке, возвращает массив, содержащий значения дерева в порядке ширины.
Пример 1: Пусть входной массив будет [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Этот массив содержит значения
следующего полного двоичного дерева.
                    _ 7_
                  /      \
                4        9
              /   \     / \
            2      6   8   10
           / \     /
          1   3   5

В этом примере входной массив должен быть отсортирован, но это не является обязательным требованием.
Результат 1: Результатом функции должен быть массив, содержащий значения узлов двоичного дерева,
считываемые сверху вниз, слева направо. В этом примере возвращаемый массив должен быть:
[7, 4, 9, 2, 6, 8, 10, 1, 3, 5]
Пример 2: Пусть входной массив будет [1, 2, 2, 6, 7, 5]. Этот массив содержит значения следующего
полного двоичного дерева.

                6
              /   \
            2       5
           / \     /
          1   2   7

Обратите внимание, что при обходе этого дерева по порядку создается входной массив.
Вывод 2: Результатом функции должен быть массив, содержащий значения узлов двоичного дерева,
считываемые сверху вниз, слева направо. В этом примере возвращаемый массив должен быть:
[6, 2, 5, 1, 2, 7]."""
from math import log, ceil


def get_tree(a: list, flag=True):
    if len(a) == 1:
        return a[0]
    if len(a) == 0:
        return None

    if flag:
        height = ceil(log(len(a)))
        top = 2**height - (height - 1)
    else:
        top = ceil(len(a) // 2)

    flag = False
    tree = a[top]

    left_subtree = a[:top]
    left = get_tree(left_subtree, flag)

    right_subtree = a[top + 1:]
    right = get_tree(right_subtree, flag)

    return [tree, left, right]


def height(tree):
    if not tree:
        return 0

    left_height = height(tree[1])
    right_height = height(tree[2])

    return max(left_height, right_height) + 1


def print_level(tree, level):
    if not tree:
        return

    if level == 0:
        print(tree[0])
    elif level > 0:
        print_level(tree[1], level - 1)
        print_level(tree[2], level - 1)


def breadth_first(tree):
    h = height(tree)
    for i in range(h):
        print_level(tree, i)


def main():
    res = get_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(res)
    # breadth_first(res)

    # func = get_tree
    # tests = [
    #     (func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [7, 4, 9, 2, 6, 8, 10, 1, 3, 5]),
    #     (func([1, 2, 2, 6, 7, 5]), [6, 2, 5, 1, 2, 7]),
    # ]
    # for t in tests:
    #     print(["failed", "passed"][t[0] == t[1]], t[0])


if __name__ == "__main__":
    main()