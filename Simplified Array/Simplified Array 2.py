#!/usr/bin/env python3

"""Task
You're given an array arr. Apply the following algorithm to it:
1. find intervals of consecutive prime numbers and consecutive non-prime numbers;
2. replace each such interval with the sum of numbers in it;
3. if the resulting array is different from the initial one, return to step 1, otherwise return the
result.

Input
A non-empty integer array such that:
-10000 ≤ arr[i] ≤ 10000
1 ≤ arr length ≤ 1000.

resput
An integer array.

Examples
For arr = [1, 2, 3, 5, 6, 4, 2, 3] the result should be [21, 5]:
[1, 2, 3, 5, 6, 4, 2, 3] --> [(1), (2 + 3 + 5), (6 + 4), (2 + 3)] --> [1, 10, 10, 5]
[1, 10, 10, 5] --> [(1 + 10 + 10), (5)] --> [21, 5].
"""


def isprime(n):
    if n <= 1: return False
    if n % 2 == 0: return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def reduce(a):
    b = list(map(isprime, a))
    res = []
    i = 0
    while i < len(b):
        if b[i] is True:
            j = i
            p = []
            while j < len(b) and b[j] is True:
                p.append(a[j])
                j += 1
                i = j - 1
            res.append(sum(p))
        else:
            k = i
            n = []
            while k < len(b) and b[k] is False:
                n.append(a[k])
                k += 1
                i = k - 1
            res.append(sum(n))
        i += 1
    return res


def checka(a):
    b = list(map(isprime, a))
    for i in range(1, len(b)):
        if b[i - 1] == b[i]:
            return True
    return False


def simplified_array(a):
    flag = 1
    while flag:
        a = reduce(a)
        flag = checka(a)
    return a


def main():
    tests = [
        (simplified_array([1, 2, 3, 5, 6, 4, 2, 3]), [21, 5]),
        (simplified_array([-3, 4, 5, 2, 0, -10]), [1, 7, -10]),
        (simplified_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), [1, 5, 4, 5, 30]),
        (simplified_array([1, 2, 3, 4, 5]), [1, 5, 4, 5]),
        (simplified_array([0, 1]), [1]),
        (simplified_array([-3, 4, 5, 2, 0, 3]), [1, 7, 0, 3]),
        (simplified_array([-3, 4, 5, 2, 0, 0, 0, 3]), [1, 7, 0, 3]),
    ]

    for t in tests:
        print(['fail', 'OK'][t[0] == t[1]])


if __name__ == "__main__":
    main()
