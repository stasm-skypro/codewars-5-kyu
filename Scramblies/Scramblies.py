#!/usr/bin/env python3

"""DОПИСАНИЕ:
Завершите функцию, scramble(str1, str2) которая возвращает, true если часть str1 символов может
быть переставлена для соответствия str2, в противном случае возвращает false.
Примечания:
Будут использоваться только буквы нижнего регистра (a-z). Знаки препинания или цифры не будут
включены.Необходимо учитывать производительность.
Примеры
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False"""


def scramble(s1, s2):
    res = ""
    l1 = list(s1)
    for char in s2:
        if char in l1:
            res += char
            l1.remove(char)
    return res == s2


def scramble2(s1, s2):
    l1 = list(s1)

    def f(c):
        r = ""
        if c in l1: r += c; l1.remove(c)
        return r
        
    res = "".join(list(map(f, s2)))
    return res == s2


def scramble3(s1: str, s2: str):
    res = ""
    for char in s2:
        if char in s1:
            res += char
            i = s1.index(char)
            s1 = s1[:i] + s1[i+1:]
    return res == s2


def scramble4(s1: str, s2: str):
    res = list(filter(lambda c: (c in s1 and s1.count(c) >= s2.count(c)), s2))
    return "".join(res) == s2


def scramble5(s1: str, s2: str):
    # flag = True
    # for c in set(s2):
    #     if s1.count(c) < s2.count(c):
    #         flag = False
    # return flag
    r = all(s1.count(x) >= s2.count(x) for x in set(s2))
    return r



def main():
    alg = scramble5
    tests = [
        (alg('rkqodlw', 'world'), True),
        (alg('cedewaraaossoqqyt', 'codewars'), True),
        (alg('katas', 'steak'), False),
        (alg('zgtkbncwqukm', 'tzunmbgbc'), False),
        (alg('ymnfszuydptazjblsvja', 'pvnslbyjpz'), False),
        (alg('abcdefghijklmnopqrstuvwxyz' * 10_000, 'zyxcba' * 9_000), True),
    ]

    for t in tests:
        print(["fail", "OK"][t[0] == t[1]])


if __name__ == "__main__":
    main()