#!/usr/bin/env python3

"""DESCRIPTION:
A "True Rectangle" is a rectangle with two different dimensions and four equal angles.
Task:
In this kata, we want to decompose a given true rectangle into the minimum number of squares, Then
aggregate these generated squares together to form all the possible true rectangles.
Notes:
You should take each square with its all adjacent squares or rectangles to form the resulting true
rectangles list. Do not take care of the resulting rectangles' orientation. just
"(long_side*short_side)".
Edge cases:
rectIntoRects(17, 5) should equal rectIntoRects(5, 17).
If length == width it should return an empty list/array
If length == 0 or width == 0 it should return an empty list/array.
References:
https://www.codewars.com/kata/55466989aeecab5aac00003e"""
import itertools as it


def rect_into_rects(x, y):
    L, W = max(x, y), min(x, y)

    dec = []
    while min(x, y) > 0:
        l, w = max(x, y), min(x, y)
        if l // w >= 1:
            dec.append(w)
            l = l - w
            x, y = l, w

    res = []
    cl = L
    for i in range(len(dec) - 1):
        rx = dec[i]
        ry = dec[i]
        for j in range(i + 1, len(dec)):
            rx += dec[j]
            if rx <= cl:
                res.append(f"({rx}*{ry})")
                if dec[j] != dec[i]:
                    cl = rx
    return res


def rect_into_rects2(l, w):
    from itertools import starmap
    res = []
    if l and w:
        while True:
            q, r = divmod(l, w)
            res.extend((i*w, w) for i in range(2, q+1) for _ in range(q-i+1))
            if not r:
                break
            res.extend((r+i*w, w) for i in range(1, q+1))
            l, w = w, r
    return [*starmap("({}*{})".format, res)]


def main():
    fun = rect_into_rects2
    tests = [
        (fun(5, 5), []),
        (fun(0, 5), []),
        (fun(13, 0), []),
        (fun(13, 5),["(10*5)", "(8*5)", "(2*1)", "(3*2)", "(5*3)", "(13*5)"]),
        (fun(5, 13), ["(10*5)", "(8*5)", "(2*1)", "(3*2)", "(5*3)", "(13*5)"]),
        (fun(22, 6), ["(12*6)","(18*6)","(22*6)","(12*6)","(16*6)","(10*6)","(6*4)","(4*2)"]),
        (fun(8, 5), ["(8*5)", "(5*3)", "(3*2)", "(2*1)"]),
        (fun(20, 8), ["(16*8)", "(20*8)", "(12*8)", "(8*4)"]),
    ]
    for t in tests:
        flag = True
        for k in t[0]:
            if k not in t[1]: flag = False
        print('OK' if flag else 'fail')


if __name__ == "__main__":
    main()
