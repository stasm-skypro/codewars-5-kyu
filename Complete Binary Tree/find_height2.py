#!/usr/bin/env python3


# Рекурсивная функция для вычисления глубины i-го узла в `parent[]`
def findDepth(parent, depth, i):
    
    # Корневой узел будет иметь глубину 0
    if parent[i] == -1:
        return 0
    
    # Если глубина i-го узла уже рассчитана, вернуть ее
    if depth[i] != 0:
        return depth[i]
    
    # глубина i-го узла = 1 + глубина его родителя
    return 1 + findDepth(parent, depth, parent[i])


# Функция для вычисления высоты бинарного дерева, представленного
# Родительский массив
def findHeight(parent):
    
    # следит за высотой дерева
    height = -1
    
    # создает вспомогательный массив для хранения глубины каждого узла дерева
    depth = [0] * len(parent)
    
    # вычисляет глубину каждого узла дерева `i` и отслеживает
    # максимальная глубина
    for i in range(len(parent)):
        depth[i] = findDepth(parent, depth, i)
        height = max(height, depth[i])
        
    return height


if __name__ == '__main__':
    
    parent = [-1, 0, 0, 1, 2, 2, 4, 4]
#   parent = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  #  На этом массиве не работает
    print('The height of the binary tree is', findHeight(parent))
    