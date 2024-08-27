from collections import defaultdict
from math import gcd

h = defaultdict(list)
for r in range(1, 1000):
    for s in range(r + 1, 2 * r):
        if gcd(r, s) == 1 and r * s + s * s <= 1500000:
            a = r * s
            b = r * r
            c = s * s - b
            p = a + b + c
            h[p].append((a, b, c))

k = list(sorted(h.keys()))


def per_ang_twice(n):
    return [k[n - 1], sorted([tuple(sorted(t)) for t in h[k[n - 1]]])]


def main():
    fun = per_ang_twice
    tests = [
        (fun(1), [15, [(4, 5, 6)]]),
        (fun(2), [28, [(7, 9, 12)]]),
        (fun(3), [40, [(9, 15, 16)]]),
        (fun(4), [45, [(9, 16, 20)]]),
        (fun(215), [2470, [(715, 729, 1026)]]),
        (fun(1016), [11704, [(304, 5625, 5775), (2025, 3960, 5719)]]),
    ]
    for t in tests:
        print(["fail", "OK"][t[0] == t[1]], t[0])


if __name__ == "__main__":
    main()
