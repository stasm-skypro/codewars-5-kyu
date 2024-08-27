#!/usr/bin/env python3
"""Array with distance of N.
Task
Your task is to write a function that accept a single parameter - a whole number N and generates an
array with following properties.
There are exactly 2 * N + 1 elements in this array.
There is only one 0 (zero) in array.
Other elements are pairs of natural numbers from 1 to N.
Number of elements between a pair of numbers is equal to the number itself.
For example, the number of elements between a pair of 2s should be exactly 2, for 3s - three and so on.
Examples of arrays
[1, 0, 1]       # Exactly one element between 1s
[1, 2, 1, 0 2]  # Exactly one element between 1s and exactly two elements between 2s.

Example usage
generate(4)
[1, 3, 1, 4, 2, 3, 0, 2, 4]
Notice that there may be multiple solutions for each number. For example, for number 3 both arrays are valid:
[2, 3, 1, 2, 1, 3, 0]
[1, 3, 1, 2, 0, 3, 2]
Notice that a reverse of a correct solution is a correct solution as well.

Tests
The solution will be tested for N < 1024."""


def generate(num):
    if num == 0: return [0]

    left = list(range(num, -1, -2))
    right = left[::-1][0 if num % 2 else 1:]
    head = left + [None] + right
    tail = [None] * (2 * num + 1 - len(head))
    perm = head + tail

    missing_a = [x for x in range(num) if x not in perm]

    while missing_a:
        nearest_none_idx = perm.index(None)
        maxnum = max(missing_a)
        perm[nearest_none_idx] = maxnum
        missing_a.remove(maxnum)

        if perm.count(None) != 0:
            perm[nearest_none_idx + maxnum + 1] = maxnum

    return perm


def main():
    # check_condition = lambda el, arr: el == 0 or len(arr) - 1 - arr[::-1].index(el) - arr.index(el) == el + 1
    # check_array = lambda num, arr: all([check_condition(el, arr) for el in arr]) and arr.count(0) == 1 \
    #                                and len(arr) == 2 * num + 1

    n = 3
    print(generate(n))


if __name__ == "__main__":
    main()
