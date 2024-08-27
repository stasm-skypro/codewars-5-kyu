#!/usr/bin/env python3

"""Write a rotate function that rotates a two-dimensional array (a matrix) either clockwise or anti-clockwise by
90 degrees, and returns the rotated array.
The function accepts two parameters: an array, and a string specifying the direction or rotation. The direction will
be either "clockwise" or "counter-clockwise".
Here is an example of how your function will be used:
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
rotate(matrix, "clockwise") #  Would return  [[7, 4, 1], [8, 5, 2],  [9, 6, 3]].
To help you visualize the rotated matrix, here it is formatted as a grid:
 [[7, 4, 1],
  [8, 5, 2],
  [9, 6, 3]]
Rotated counter-clockwise it would looks like this:
 [[3, 6, 9],
  [2, 5, 8],
  [1, 4, 7]]."""


def rotate(matrix, direction):
    m, n = len(matrix[0]), len(matrix)
    if direction == 'counter-clockwise':
        # b = [[matrix[j][m - i - 1] for j in range(n)] for i in range(m)]
        return [[matrix[j][m - i - 1] for j in range(n)] for i in range(m)]
    elif direction == 'clockwise':
        # b = [[matrix[n - j - 1][i] for j in range(n)] for i in range(m)]
        return [[matrix[n - j - 1][i] for j in range(n)] for i in range(m)]


def main():
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    tests = [
        (rotate(matrix, 'counter-clockwise'), [[3, 6, 9], [2, 5, 8], [1, 4, 7]]),
        (rotate(matrix, 'clockwise'), [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
        (rotate(rotate(matrix, 'counter-clockwise'), 'clockwise'), [[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
        (rotate(rotate(rotate(rotate(matrix, 'clockwise'), 'clockwise'), 'clockwise'), 'clockwise'),
         [[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
    ]
    for t in tests:
        print(['fail', 'OK'][t[0] == t[1]])

    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              [10, 11, 12]]
    tests = [
        (rotate(matrix, 'counter-clockwise'), [[3, 6, 9, 12], [2, 5, 8, 11], [1, 4, 7, 10]]),
        (rotate(matrix, 'clockwise'), [[10, 7, 4, 1], [11, 8, 5, 2], [12, 9, 6, 3]]),
    ]
    for t in tests:
        print(['fail', 'OK'][t[0] == t[1]])

    matrix = [[1, 2, 3]]
    tests = [
        (rotate(matrix, 'counter-clockwise'), [[3], [2], [1]]),
        (rotate(matrix, 'clockwise'), [[1], [2], [3]]),
        (rotate(rotate(matrix, 'clockwise'), 'clockwise'), [[3, 2, 1]]),
    ]
    for t in tests:
        print(['fail', 'OK'][t[0] == t[1]])

    matrix = [[1]]
    tests = [
        (rotate(matrix, 'counter-clockwise'), [[1]])
    ]
    for t in tests:
        print(['fail', 'OK'][t[0] == t[1]])


if __name__ == "__main__":
    main()
