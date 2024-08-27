"""ОПИСАНИЕ:
Если бы мы создали игру в крестики-нолики, мы бы хотели знать, решено ли
текущее состояние доски, не так ли? Наша цель - создать функцию, которая
проверит это для нас!

Предположим, что плата имеет форму массива 3x3, где значение, если пятно
пустое, если это «X» или «O», например:012.

[[0, 0, 1],
 [0, 1, 2],
 [2, 1, 0]]
Мы хотим, чтобы наша функция вернула:
-1 если доска еще не закончена И еще никто не выиграл (есть пустые места),
1 если "Х" выиграет,
2 если «О» выиграет,
0 если это кошачья игра (т.е. ничья).
Вы можете предположить, что переданная доска действительна в контексте игры в
крестики-нолики."""


def allel(line: list, x):
    flag = 1
    for el in line:
        if el == x:
            flag = flag * 1
        else:
            flag = 0
    return flag


def tictactoe(board: list):
    zerofound = False

    collection = [
            board[0], board[1], board[2],
            [board[0][1], board[1][1], board[2][1]],
            [board[0][2], board[1][2], board[2][2]],
            [board[0][0], board[1][1], board[2][2]],
            [board[0][0], board[1][1], board[2][2]],
            [board[0][2], board[1][1], board[2][0]],
        ]

    for el in collection:
        if allel(el, 1):
            return 1
        if allel(el, 2):
            return 2
        if 0 in el:
            zerofound = True

    return -1 if zerofound else 0


def tictactoe2(board):
    """Решение avidwlewis, SeanGoku11, HackerVik."""
    for sign in [1, 2]:
        win = [sign] * 3
        if (win in board or
            win in zip(*board[::-1]) or
            win in [[board[x][0], board[1][1], board[2-x][2]] for x in [0, 2]]):
                return sign
    return -1 if 0 in sum(board, []) else 0


def tictactoe3(board):
    for i in range(0,3):
        if board[i][0] == board[i][1] == board[i][2] != 0:
            return board[i][0]
        elif board[0][i] == board[1][i] == board[2][i] != 0:
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][0]

    elif 0 not in board[0] and 0 not in board[1] and 0 not in board[2]:
        return 0
    else:
        return -1


def main():
    tests = [
        ([[0, 0, 1],
          [0, 1, 2],
          [2, 1, 0]], -1),  # 0

        ([[1, 1, 1],
          [2, 1, 2],
          [1, 2, 2]], 1),  # 1

        ([[2, 2, 2],
          [2, 1, 1],
          [1, 2, 2]], 2),  # 2

        ([[1, 2, 2],
          [1, 1, 1],
          [2, 1, 2]], 1),  # 3

        ([[1, 2, 1],
          [2, 2, 2],
          [2, 1, 2]], 2),  # 4

        ([[2, 1, 2],
          [1, 2, 2],
          [1, 1, 1]], 1),  # 5

        ([[1, 2, 1],
          [2, 1, 2],
          [2, 2, 2]], 2),  # 6

        ([[1, 2, 1],
          [1, 1, 2],
          [1, 2, 2]], 1),  # 7

        ([[2, 1, 2],
          [2, 2, 1],
          [2, 1, 1]], 2),  # 8

        ([[2, 1, 2],
          [1, 1, 2],
          [2, 1, 1]], 1),  # 9

        ([[2, 2, 1],
          [1, 2, 2],
          [2, 2, 1]], 2),  # 10

        ([[2, 2, 1],
          [1, 2, 1],
          [2, 1, 1]], 1),  # 11

        ([[2, 1, 2],
          [1, 1, 2],
          [1, 2, 2]], 2),  # 12

        ([[1, 2, 2],
          [2, 1, 1],
          [2, 2, 1]], 1),  # 13

        ([[2, 2, 1],
          [1, 2, 1],
          [1, 1, 2]], 2),  # 14

        ([[1, 2, 1],
          [2, 1, 1],
          [1, 2, 2]], 1),  # 15

        ([[1, 2, 2],
          [2, 2, 1],
          [2, 1, 1]], 2),  # 16

        ([[1, 2, 2],
          [2, 1, 1],
          [1, 1, 2]], 0)  # 17
    ]
    f = tictactoe3
    for n, t in enumerate(tests):
        print([f'{n} fail', f'{n} OK'][f(t[0]) == t[1]], f(t[0]))


if __name__ == "__main__":
    main()