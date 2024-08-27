#! /usr/bin/env python3

"""Converting z-sequence to p-sequence."""


def convert_z_to_p(z):
    """Convert z-sequence to p-sequence."""

    n = len(z)
    p = [0] * n
    for i in range(1, n):
        if z[i] != 0:
            for j in range(z[i] - 1, -1, -1):
                if j != p[i + j]:
                    p[i + j] = j + 1
    return p


def main():
    tests = [
        (convert_z_to_p([8, 0, 2, 0, 0, 3, 0, 1]), [0, 0, 1, 2, 0, 1, 2, 3]),
        (convert_z_to_p([13, 1, 0, 0, 3, 1, 0, 0, 2, 2, 2, 1, 0]), [
         0, 1, 0, 0, 1, 2, 3, 0, 1, 2, 2, 2, 0]),
        (convert_z_to_p([11, 0, 0, 1, 0, 1, 0, 4, 0, 0, 1]),
         [0, 0, 0, 1, 0, 1, 0, 1, 2, 3, 4]),
        (convert_z_to_p([]), []),
        (convert_z_to_p([7, 0, 0, 3, 0, 0, 0]), [0, 0, 0, 1, 2, 3, 0]),
        (convert_z_to_p([7, 0, 1, 0, 3, 0, 1]), [0, 0, 1, 0, 1, 2, 3]),
    ]
    for t in tests:
        print(['failed', 'passed'][t[0] == t[1]], t[0])


if __name__ == "__main__":
    main()
