#!/usr/bin/env python3


# Рекурсивная функция для вычисления глубины i-го узла в `parent[]`
def find_depth(parent, i):
    
    # Корневой узел будет иметь глубину 0
    if parent[i] == -1:
        return 0
    
    # глубина i-го узла = 1 + глубина его родителя
    return 1 + find_depth(parent, parent[i])


# Функция для вычисления высоты бинарного дерева, представленного
# Родительский массив
def find_height(parent):
    
    # следит за высотой дерева
    height = -1
    
    # вычисляет глубину каждого узла дерева `i` и отслеживает
    # максимальная глубина
    for i in range(len(parent)):
        height = max(height, find_depth(parent, i))
        
    return height


if __name__ == '__main__':
    parent = [-1, 0, 0, 1, 2, 2, 4, 4]
#   parent = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print('The height of the binary tree is', find_height(parent))