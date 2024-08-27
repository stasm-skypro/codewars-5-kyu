#!/usr/bin/env python3

"""DESCRIPTION:
An Array consisting of "0" and "1"'s also called a binary array is given as an input.

Task
Find the length of the longest contiguous subarray which consists of Equal number of "0"s and "1"s.

Example
s = [1,1,0,1,1,0,1,1]
         |_____|
            |
         [0,1,1,0]

         length = 4
Note
1<=length(array)<120000."""
from time import perf_counter
import itertools


def find_longest(s):
    longest = 0
    for i in range(len(s)):
        c0, c1 = 0, 0
        if s[i] == 0:
            c0 = 1
        else:
            c1 = 1
        for j in range(i + 1, len(s)):
            if s[j] == 0:
                c0 += 1
            else:
                c1 += 1
            if c0 == c1:
                longest = max(longest, c0 + c1)
    return longest


def find_longest2(s: list):
    longest = 0
    i = 0
    for x in s:
        c0, c1 = 0, 0
        if x == 0:
            c0 = 1
        else:
            c1 = 1
        i += 1
        for y in s[i::]:
            if y == 0:
                c0 += 1
            else:
                c1 += 1
            if c0 == c1:
                longest = max(longest, c0 + c1)
    return longest


def find_longest3(s: list):
    counter, longest = 0, 0
    d = {0: -1}
    for i, x in enumerate(s):
        if x == 0:
            counter -= 1
        if x == 1:
            counter += 1
        if counter in d:
            longest = max(longest, i - d[counter])
        else:
            d[counter] = i
    return longest


def main():
    alg = find_longest3
    tests = [
        (alg([1, 0, 0, 1]), 4),
        (alg([1, 0, 0, 1, 1]), 4),
        (alg([1, 0, 0, 1, 1, 0, 0, 0]), 6),
        (alg([0, 0, 1, 1]), 4),
        (alg([1, 1, 0, 1, 1, 0, 1, 1]), 4),
        (alg([0, 1]), 2),
        (alg([0]), 0),
        (alg([0, 1, 1, 0, 1, 1, 1, 0, 0, 0]), 10),
        (alg([0, 0, 1, 1, 1, 0, 0, 0, 0, 0]), 6),
        (alg([1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1]), 18),
    ]

    start = perf_counter()
    for t in tests:
        print(["fail", "OK"][t[0] == t[1]])
    print(f"Time elapsed: {start - perf_counter():.6f}")


if __name__ == "__main__":
    main()
