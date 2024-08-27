#! /usr/bin/env python3

"""ОПИСАНИЕ:
Ваша задача - написать функцию, которая увеличивает строку, чтобы создать новую строку.
Если строка уже заканчивается числом, это число следует увеличить на 1.
Если строка не заканчивается цифрой. к новой строке следует добавить цифру 1.
Примеры:
foo -> foo1
foobar23 -> foobar24
foo0042 -> foo0043
foo9 -> foo10
foo099 -> foo100
Внимание: Если номер содержит начальные нули, следует учитывать количество цифр.
"""


def increment_string(strng):
    digits = ""
    for ch in strng[::-1]:
        if ch.isdigit():
            digits = digits + ch
        else:
            break

    if digits != "":
        digits = digits[::-1]
        number = int(digits) + 1
        return strng[:len(strng) - len(digits)] + str(number).zfill(len(digits))
    else:
        return strng + "1"


def increment_string2(strng):
    """Решение nicholas1."""
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng + "1"
    return head + str(int(tail) + 1).zfill(len(tail))


def main():
    tests = [
        ("foo", "foo1"),
        ("foobar001", "foobar002"),
        ("foobar1", "foobar2"),
        ("foobar00", "foobar01"),
        ("foobar99", "foobar100"),
        ("foobar099", "foobar100"),
        ("fo99obar99", "fo99obar100"),
        ("", "1"),
    ]
    func = increment_string
    for t in tests:
        print(["failed", "passed"][func(t[0]) == t[1]], func(t[0]))


if __name__ == "__main__":
    main()
