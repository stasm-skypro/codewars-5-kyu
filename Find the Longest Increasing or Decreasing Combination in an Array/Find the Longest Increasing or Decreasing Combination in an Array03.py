#!/usr/bin/env python3

"""DESCRIPTION:
Given a certain array of positive and negative numbers, give the longest increasing or decreasing combination of at
least 3 elements of the array. If our array is a = [a[0], a[1], ....a[n-1]]:
i) For the increasing case: there is a combination: a[i] < a[j] < a[k]..< a[p], such that 0 ≤ i < j < k < ...< p ≤ n - 1
For the decreasing case the combination would be: a[i] > a[j] > a[k]..> a[p], such that 0 ≤ i < j < k < ...< p ≤ n - 1
For that task create a function longest_comb() (Javascript: longestComb() ) that will receive an array, and a command,
one of the two kinds of strings: '< <' or '<<' (increasing), '> >' or '>>' (decreasing).
Let's see some examples:
longest_comb([-1, 3, -34, 18, -55, 60, 118, -64], '< <') == [-1, 3, 18, 60, 118]
longest_comb([-1, 3, -34, 18, -55, 60, 118, -64], '> >') == [[-1, -34, -55, -64], [3, -34, -55, -64]] # resputs a
2D array of two combinations # of same length in the order that they appear in the given array from # left to right.
We may have some cases withres any possible combination:
longest_comb([-26, 26, -36, 17, 12, 12, -10, -21], "< <") == []
On the other hand we may have cases with many solutions:
longest_comb([-22, 40, -45, -43, -1, 7, 43, -56], "> >") == [[-22, -45, -56], [-22, -43, -56], [40, -45, -56],
[40, -43, -56], [40, -1, -56], [40, 7, -56]]."""


def longest_comb(arr, command):
    """Задача по упрощению кода выполнена."""

    if command == "< <":
        sign = ">"
    elif command == "> >":
        sign = "<"

    maxl = 3
    tres = []
    while arr:
        fst = arr[0]
        t = [x for x in arr if eval(str(x) + sign + str(fst))]
        print(fst, t)
        while t:
            t2 = [fst]
            fst2 = fst
            for x in t:
                current = x
                if eval(str(current) + sign + str(fst2)):
                    t2.append(current)
                    fst2 = current
                if len(t2) >= 3:
                    if t2 not in tres:
                        tres.append(t2)
            t = t[1:]
        arr = arr[1:]

    print(tres)
    if tres == []:
        return []
    else:
        maxl = max([len(r) for r in tres])
        res = [r for r in tres if len(r) == maxl]
        # print(res)
        return res[0] if len(res) == 1 else res


def main():
    tests = [
        # (
        #     longest_comb([-1, 3, -34, 18, -55, 60, 118, -64], "< <"),
        #     [-1, 3, 18, 60, 118],
        # ),
        # (
        #     longest_comb([-1, 3, -34, 18, -55, 60, 118, -64], "> >"),
        #     [[-1, -34, -55, -64], [3, -34, -55, -64]],
        # ),
        # (longest_comb([-26, 26, -36, 17, 12, 12, -10, -21], "< <"), []),
        # (
        #     longest_comb([-22, 40, -45, -43, -1, 7, 43, -56], "> >"),
        #     [
        #         [-22, -45, -56],
        #         [-22, -43, -56],
        #         [40, -45, -56],
        #         [40, -43, -56],
        #         [40, -1, -56],
        #         [40, 7, -56],
        #     ],
        # ),
        # (
        #     longest_comb([-25, -59, -57, -27, -9, -52, 30, -57], "< <"), [-59, -57, -27, -9, 30]
        # ),
        (
            longest_comb([48, -5, 36, -13, 52, -23, 50, 53], "< <"),
            [[-5, 36, 52, 53], [-5, 36, 50, 53]],
        ),
    ]
    for t in tests:
        print(["fail", "OK"][t[0] == t[1]])


if __name__ == "__main__":
    main()
