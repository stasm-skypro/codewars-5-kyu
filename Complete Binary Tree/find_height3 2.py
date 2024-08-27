#!/usr/bin/env python3



# Функция для вычисления высоты бинарного дерева, представленного
# Родительский массив
def findHeight(parent):
    
    # создает вспомогательный массив для хранения глубины каждого узла дерева
    depth = [0] * len(parent)
    
    # следит за высотой дерева
    height = -1
    
    # итеративно вычисляет глубину каждого узла дерева `i`
    for i in range(len(parent)):
        
        # инициализирует глубину i-го узла 0 (глубина одного узла)
        depth_i = 0
        
        # проследить путь от i-го узла до корня
        k = i
        while parent[k] != -1:
            #, если глубина k-го узла уже рассчитана
            if depth[k] != 0:
                depth_i += depth[k]
                break
            
            depth_i += 1
            k = parent[k]
            
        # сохранить решение подзадачи
        depth[i] = depth_i
        
        # следит за максимальной глубиной
        height = max(height, depth[i])
        
    return height


if __name__ == '__main__':
#   parent = [-1, 0, 0, 1, 2, 2, 4, 4]
    parent = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print('The height of the binary tree is', findHeight(parent))