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
from math import log

result = []


class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def get_tree(a: list):
    if len(a) == 1:
        return Tree(a[0])
    if len(a) == 0:
        return None

    n = len(a)
    deep = int(log(n, 2))
    top = (2**deep - 1) // 2 + min(n - 2**deep + 1, 2 ** (deep - 1))

    tree = Tree(a[top])

    left_subtree = a[:top]
    tree.left = get_tree(left_subtree)

    right_subtree = a[top + 1:]
    tree.right = get_tree(right_subtree)

    return tree


def height(tree):
    if not tree:
        return 0

    left_height = height(tree.left)
    right_height = height(tree.right)

    return max(left_height, right_height) + 1


def print_level(tree, level):
    global result

    if not tree:
        return

    if level == 0:
        result.append(tree.value)
    elif level > 0:
        print_level(tree.left, level - 1)
        print_level(tree.right, level - 1)


def breadh_first(tree):
    h = height(tree)
    for i in range(h):
        print_level(tree, i)
    print(result)


def run(a):
    global result
    result = []
    tree = get_tree(a)
    breadh_first(tree)


def main():
    func = run
    tests = [
        (func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
         [7, 4, 9, 2, 6, 8, 10, 1, 3, 5]),
        (func([1, 2, 2, 6, 7, 5]), [6, 2, 5, 1, 2, 7]),
    ]
    for t in tests:
        print(['failed', 'passed'][t[0] == t[1]], t[0])

    # tree = Tree
    # tree.value = Tree(7)
    # tree.left = Tree(4)
    # tree.right = Tree(9)
    # tree.left.left = Tree(2)
    # tree.left.right = Tree(6)
    # tree.right.left = Tree(8)
    # tree.right.right = Tree(10)
    # tree.left.left.left = Tree(1)
    # tree.left.left.right = Tree(3)
    # tree.left.right.left = Tree(5)
    # breadh_first(tree)


if __name__ == "__main__":
    main()
