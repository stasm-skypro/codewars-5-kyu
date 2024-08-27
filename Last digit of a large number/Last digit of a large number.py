#! /usr/bin/env python3

"""DESCRIPTION:
Define a function that takes in two non-negative integers a and b and returns the last decimal
digit of a**b. Note that a and b may be very large!

For example, the last decimal digit of 9**7 is 9, since 9**7=4782969. The last decimal digit of
(2**200)**2**op300, which has over 10**92 decimal digits, is 6. Also, please take 0**0 to be 1.

You may assume that the input will always be valid.

Examples
last_digit(4, 1)                # returns 4
last_digit(4, 2)                # returns 6
last_digit(9, 7)                # returns 9
last_digit(10, 10 ** 10)        # returns 0
last_digit(2 ** 200, 2 ** 300)  # returns 6."""


def p1(x, n):
    res = pow(x, n // 2)
    res = res * res
    if n % 2 != 0:
        res = res * x
    return res
    

def p2(x, n):
    res = 1
    if x == 0:
        return 0
    for i in range(1, (n // 2) + 1):
        res = res * x
    res = res * res
    if n % 2 != 0:
        res = res * x
    return res


def p3(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n % 2 != 0:
        return x * p3(x, n - 1)
    elif n % 2 == 0:
        return p3(x*x, n // 2)
    

def last_digit(a, b):
    x = a % 10
    e = b % 4 + 4 * (bool(b) % 10)
#   return pow(a, b, 10)
    return (x ** e) % 10
    

def main():    
    fun = last_digit
    tests = [
        (fun(4, 1), 4),
        (fun(4, 2), 6),
        (fun(9, 7), 9),
        (fun(99999999, 333), 9),
        (fun(2**200, 2**3), 6),
        (fun(2**200, 2*33), 6),
        (fun(99999999, 333333), 9),
        (fun(10, 10**10), 0),
        (fun(2**200, 2**300), 6),
        (fun(3715290469715693021198967285016729344580685479654510946723, 68819615221552997273737174557165657483427362207517952651), 7),
    ]
    for t in tests:
        print(['fail','OK'][t[0] == t[1]], t[0])


if __name__ == "__main__":
    main()