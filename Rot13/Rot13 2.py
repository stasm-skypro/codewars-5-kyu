#!/usr/bin/env python3

"""ОПИСАНИЕ:
ROT13 - это простой шифр замены букв, который заменяет букву буквой 13, следующей за ней в алфавите.
ROT13 является примером шифра Цезаря.
Создайте функцию, которая принимает строку и возвращает строку, зашифрованную с помощью Rot13. Если
в строку включены цифры или специальные символы, они должны быть возвращены такими, какие они есть.
Сдвигать следует только буквы латинского / английского алфавита, как в оригинальной "реализации"
Rot13.
Пожалуйста, обратите внимание, что использование encode считается мошенничеством."""
from collections import deque


def encode_rot13(text: str):
    queue = deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                   'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])

    res = ""
    for i, ch in enumerate(text):
        curr = ch.lower()
        if curr in queue:
            idx = queue.index(curr)
            queue.rotate(13)
            ench = queue[idx]
            if ch.istitle():
                ench = ench.upper()
            res = res + ench
        else:
            res = res + ch

    return res


def main():
    rot13 = encode_rot13
    tests = [
        (rot13('test'), 'grfg', 'Returned solution incorrect for fixed string = test'),
        (rot13('Test'), 'Grfg', 'Returned solution incorrect for fixed string = Test'),
        (rot13('aA bB zZ 1234 *!?%'), 'nN oO mM 1234 *!?%',
         'Returned solution incorrect for fixed string = aA bB zZ 1234 *!?%'),
    ]

    for t in tests:
        print(['failed', 'passed'][t[0] == t[1]], t[0])


if __name__ == "__main__":
    main()
