#!/usr/bin/env python3

"""Land perimeter.
DESCRIPTION:

Given an array arr of strings, complete the function by calculating the total perimeter of all the islands. Each piece
of land will be marked with 'X' while the water fields are represented as 'O'. Consider each tile being a perfect
1 x 1 piece of land. Some examples for better visualization:
['XOOXO',
 'XOOXO',
 'OOOXO',
 'XXOXO',
 'OXOOO']
 """
from time import perf_counter


def land_perimeter(arr):
    s0 = "O" * len(arr[0])
    arr = [s0] + arr + [s0]
    new_arr = []
    for row in arr:
        new_row = "O" + row + "O"
        new_arr += [new_row]

    p, k = 0, 0
    for i in range(1, len(new_arr) - 1):
        for j in range(1, len(new_arr[i]) - 1):
            if new_arr[i][j] == 'X':
                if new_arr[i-1][j] == 'X':
                    k += 1
                if new_arr[i][j+1] == 'X':
                    k += 1
                if new_arr[i+1][j] == 'X':
                    k += 1
                if new_arr[i][j-1] == 'X':
                    k += 1
                p += 4 - k
                f = []
                k = 0
    return f"Total land perimeter: {p}"


def main():
    tests = [
        (land_perimeter(["XOOO", "XOXO", "XOXO", "OOXX", "OOOO"]), "Total land perimeter: 18"),
        (land_perimeter(["XOOXO", "XOOXO", "OOOXO", "XXOXO", "OXOOO"]), "Total land perimeter: 24"),
        (land_perimeter(["OXOOOX", "OXOXOO", "XXOOOX", "OXXXOO", "OOXOOX", "OXOOOO", "OOXOOX", "OOXOOO", "OXOOOO", "OXOOXX"]),
                       "Total land perimeter: 60"),
        (land_perimeter(["OXOOO", "OOXXX", "OXXOO", "XOOOO", "XOOOO", "XXXOO", "XOXOO", "OOOXO", "OXOOX", "XOOOO", "OOOXO"]),
                       "Total land perimeter: 52"),
        (land_perimeter(["XXXXXOOO", "OOXOOOOO", "OOOOOOXO", "XXXOOOXO", "OXOXXOOX"]),
                       "Total land perimeter: 40"),
        (land_perimeter(["XOOOXOO", "OXOOOOO", "XOXOXOO", "OXOXXOO", "OOOOOXX", "OOOXOXX", "XXXXOXO"]),
                       "Total land perimeter: 54"),
        (land_perimeter(["OOOOXO", "XOXOOX", "XXOXOX", "XOXOOO", "OOOOOO", "OOOXOO", "OOXXOO"]),
                       "Total land perimeter: 40"),
    ]

    start = perf_counter()
    for t in tests:
        print(['fail', f'OK - {t[0]}'][f'{t[0]}' == t[1]])
    print(f">>>code runs in: {(perf_counter() - start):0.6f}")


if __name__ == "__main__":
    main()
