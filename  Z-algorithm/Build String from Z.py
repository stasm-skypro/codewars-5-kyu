#!/usr/bin/env python3

""""""

def get_str_from_z(z: list) -> str:
    """Build string from z-function."""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s = ""
    prefix_length = 0  # длина префикса, который мы записываем
    j = -1  # позиция символа в строке, который будем записывать
    new_character = 0  # индекс нового символа
    for i in range(0, len(z) - 1):
        # мы не пишем какой-то префикс и не будем писать новый
        if z[i] == 0 and prefix_length == 0:
            if new_character < len(alphabet):
                s = s + alphabet[new_character]
                new_character = new_character + 1
            else:
                s = s + alphabet[new_character - 1]
        # нам нужно запомнить, что мы пишем префикс
        if z[i] > prefix_length:
            prefix_length = z[i]
            j = 0
        # пишем префикс
        if prefix_length > 0:
            s = s + s[j]
            # s = s + alphabet[j]
            j = j + 1
            prefix_length = prefix_length - 1
    return s

def main():
    tests = [
        (get_str_from_z([11, 0, 0, 1, 0, 1, 0, 4, 0, 0, 1]), "abracadabra"),
    ]
    for t in tests:
        print(['fail', 'passed'][t[0] == t[1]], t[0])


if __name__ == "__main__":
    main()
