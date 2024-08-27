#! /usr/bin/env python3

"""ОПИСАНИЕ:
Пит любит печь торты. У него есть несколько рецептов и ингредиентов. К сожалению, он не силен в математике.
Можете ли вы помочь ему выяснить, сколько тортов он мог бы испечь, учитывая его рецепты?
Напишите функцию cakes(), которая принимает рецепт (объект) и доступные ингредиенты, (тоже объект) и возвращает
максимальное количество пирожных, которые может испечь Пит (целое число). Для простоты здесь нет единиц измерения
количества (например, 1 фунт муки или 200 г сахара равны просто 1 или 200). Ингредиенты, которых нет в объектах,
могут рассматриваться как 0.

Примеры:
# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})"""


def cakes(recipe, available):
    cakes = 1_000_000
    for k, v in recipe.items():
        if k not in available:
            cakes = 0
        else:
            cakes = min([cakes, available[k] // recipe[k]])
    return cakes


def cakes2(recipe, available):
    """Решение учителя."""
    return min([available[k] // recipe[k] if k in available else 0 for k in recipe])


def main():
    recipe = {"flour": 500, "sugar": 200, "eggs": 1}
    available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
    print(['failed', 'passed'][cakes(recipe, available) == 2])

    recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
    available = {"sugar": 500, "flour": 2000, "milk": 2000}
    print(['failed', 'passed'][cakes(recipe, available) == 0])


if __name__ == "__main__":
    main()
