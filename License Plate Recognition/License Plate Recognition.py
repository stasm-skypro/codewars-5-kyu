#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 19:34:30 2023

@author: smayatskiy
"""

"""DESCRIPTION:
You have been hired by a company making speed cameras. Your mission is to
write the controller software turning the picture taken by the camera into a
license plate number.
Specification
The sensor matrix resputs a 3-line string using pipes and underscores. We want
to translate this into a string with regular digits when these are recognized,
and a ? when they are not. See the input and resput examples below.
We plan to sell to various countries, so we make no assumption on length
there are no 0s or 1s on license plates.
The input string sometimes misses one of the bottom two horizontal stripes.
Since there is no ambiguity, we must return the digit instead of a question mark.
Input
A non-empty string with pipes and underscores. It will always have 3 lines of
identical length (which will always be a multiple of 3).
 _  _        _  _  _  _ \n
 _| _||_||_ |_   || ||_|\n
|_  _|  | _|| |  ||_| _|
resput
A string with regular digits and question marks 234?6789."""


def convert(string: str):
    l = string.find("\n")
    p1 = [string[i] for i in range(l)]
    start = l + 1

    l = string.find("\n", start)
    p2 = [string[j] for j in range(start, l)]
    start = l + 1

    l = len(string)
    p3 = [string[k] for k in range(start, l)]

    # n2 = f"{p1[0]}{p1[1]}{p1[2]}\n{p2[0]}{p2[1]}{p2[2]}\n{p3[0]}{p3[1]}{p3[2]}"
    # n3 = f"{p1[3]}{p1[4]}{p1[5]}\n{p2[3]}{p2[4]}{p2[5]}\n{p3[3]}{p3[4]}{p3[5]}"
    # n4 = f"{p1[6]}{p1[7]}{p1[8]}\n{p2[6]}{p2[7]}{p2[8]}\n{p3[6]}{p3[7]}{p3[8]}"

    # d0 = (" _ \n|/|\n|_|",)
    # d1 = ("   \n  |\n  |",)
    # d2 = (" _ \n _|\n|_ ", "   \n _|\n|_ ", " _ \n  |\n|_ ", " _ \n _|\n|  ")
    # d3 = (" _ \n _|\n _|", "   \n _|\n _|", " _ \n  |\n _|", " _ \n _|\n  |")
    # d4 = ("   \n|_|\n  |", "   \n| |\n  |")
    # d5 = (" _ \n|_ \n _|", " _ \n|  \n _|", " _ \n|_ \n  |")
    # d6 = (" _ \n|_ \n|_|", " _ \n|  \n|_|", " _ \n|_ \n| |")
    # d7 = (" _ \n  |\n  |",)
    # d8 = (" _ \n|_|\n|_|", " _ \n| |\n|_|", " _ \n|_|\n| |", "   \n|_|\n|_|")
    # d9 = (" _ \n|_|\n _|", "   \n|_|\n _|", " _ \n| |\n _|", " _ \n|_|\n  |")
    # samp = [d0, d1, d2, d3, d4, d5, d6, d7, d8, d9]
    # samp = {'0': d0, '1': d1, '2': d2, '3': d3, '4': d4, '5': d5, '6': d6, '7': d7, '8': d8, '9': d9}
    samp = {" _ \n|/|\n|_|": 0,
           "   \n  |\n  |": 1,
           " _ \n _|\n|_ ": 2, "   \n _|\n|_ ": 2, " _ \n  |\n|_ ": 2, " _ \n _|\n|  ": 2,
           " _ \n _|\n _|": 3, "   \n _|\n _|": 3, " _ \n  |\n _|": 3, " _ \n _|\n  |": 3,
           "   \n|_|\n  |": 4, "   \n| |\n  |": 4,
           " _ \n|_ \n _|": 5, " _ \n|  \n _|": 5, " _ \n|_ \n  |": 5,
           " _ \n|_ \n|_|": 6, " _ \n|  \n|_|": 6, " _ \n|_ \n| |": 6,
           " _ \n  |\n  |": 7,
           " _ \n|_|\n|_|": 8, " _ \n| |\n|_|": 8, " _ \n|_|\n| |": 8, "   \n|_|\n|_|": 8,
           " _ \n|_|\n _|": 9, "   \n|_|\n _|": 9, " _ \n| |\n _|": 9, " _ \n|_|\n  |": 9,}

    res = ""
    for i in range(0, len(p1), 3):
        n = f"{p1[i]}{p1[i + 1]}{p1[i + 2]}\n{p2[i]}{p2[i + 1]}{p2[i + 2]}\n{p3[i]}{p3[i + 1]}{p3[i + 2]}"
        if n in samp:
            res += str(samp[n])
        else:
            res += "?"

    return res


def main():
    tests = [
        (convert(" _  _        _  _  _  _ \n _| _||_||_ |_   || ||_|\n|_  _|  | _|| |  ||_| _|"),
         "234?6789"),
        (convert(' _  _     _  _  _  _  _ \n'
                 ' _| _||_||_ |_   ||_||_|\n'
                 '|_  _|  | _||_|  ||_| _|'), "23456789"),
        (convert(' _  _     _  _  _  _  _ \n'
                 ' _|  ||_||_ |_   ||_|| |\n'
                 '|_  _|  |  ||_|  || | _|'), "23456789"),
        (convert(' _  _     _     _  _  _ \n'
                 ' _|  ||_||_ |_   ||_|| |\n'
                 '|_  _|  |  ||_|  || | _|'), "2345?789"),
    ]
    for t in tests:
        print(["fail", "OK"][t[0] == t[1]], t[0])


if __name__ == "__main__":
    main()
