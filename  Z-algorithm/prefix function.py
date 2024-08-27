#!/usr/bin/env python3

"""Prefix function algorithm."""


def pfunc(s):
    """Calculate p-sequence for string."""
    n = len(s)
    p = [0] * n

    for i in range(1, n):
        k = p[i - 1]
        while k > 0 and s[k] != s[i]:
            k = p[k - 1]
        if s[k] == s[i]:
            k = k + 1
        p[i] = k
    return p


def main():
    fun = pfunc
    tests = [
        (fun("ababcaba"), [0, 0, 1, 2, 0, 1, 2, 3]),
        (fun("aabcaabxaaaaz"), [0, 1, 0, 0, 1, 2, 3, 0, 1, 2, 2, 2, 0]),
        (fun("abracadabra"), [0, 0, 0, 1, 0, 1, 0, 1, 2, 3, 4]),
        (fun(""), []),
        (fun("abcabcd"), [0, 0, 0, 1, 2, 3, 0]),
        (fun("abacaba"), [0, 0, 1, 0, 1, 2, 3]),
        (fun("abcdabcabcdabcdab"), [0, 0, 0, 0,
                                    1, 2, 3, 1, 2, 3, 4, 5, 6, 7, 4, 5, 6]),
    ]
    for t in tests:
        print(['failed', 'passed'][t[0] == t[1]], t[0])


if __name__ == "__main__":
    main()
