#! /usr/bin/env python3

"""DESCRIPTION:
In this example you have to validate if a user input string is alphanumeric. The given string is
not nil/null/NULL/None, so you don't have to check that.
The string has the following conditions to be alphanumeric:
At least one character ("" is not valid)
Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
No whitespaces / underscore."""


def is_alphanumeric(password: str):
    if password == "": return False
    letters = "AEIOUYBCDFGHJKLMNPQRSTVWXZ"
    numbers = "0123456789"
    res = all(map(lambda x: x in letters or x in letters.lower() or x in numbers, password))
    return res


def main():
    tests = [
        (is_alphanumeric("QAZ2wsxEDC4rfv"), True),
        (is_alphanumeric("QAZWSX3edc4rfv"), True),
        (is_alphanumeric("WQCnfybckfd1"), True),
        (is_alphanumeric("Cshfrusm073910frmuza"), True),
        (is_alphanumeric("frmuza"), True),
        (is_alphanumeric(" rmuza"), False),
        (is_alphanumeric("frm_uza"), False),
        (is_alphanumeric("#rmuza"), False),
        (is_alphanumeric(""), False),
    ]
    for t in tests:
        print(['fail', 'OK'][t[0] == t[1]], t[0])


if __name__ == "__main__":
    main()
