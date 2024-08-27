#! /usr/bin/env python3

"""ОПИСАНИЕ:
Напишите функцию с именем first_non_repeating_letter, которая принимает строковый ввод и возвращает
первый символ, который нигде не повторяется в строке. Например, если заданы входные данные 'stress',
функция должна вернуть 't', поскольку буква t встречается в строке только один раз и встречается
первой в строке. В качестве дополнительной проблемы заглавные и строчные буквы считаются одним и
тем же символом, но функция должна возвращать правильный регистр для начальной буквы. Например,
ввод 'sTreSS' должен возвращать 'T'. Если строка содержит все повторяющиеся символы, она должна
возвращать пустую строку ("") или None -- см. Примеры тестов."""


def first_non_repeating_letter2(string):
    ans = []
    for ch in string:
        if string.lower().count(ch.lower()) == 1:
            ans.append(ch)

    if ans:
        return ans[0]
    else:
        return ""


def first_non_repeating_letter(string):
    ans = ""
    for ch in string:
        if string.lower().count(ch.lower()) == 1:
            ans = ch
            break

    return ans


def main():
    tests = [
        (first_non_repeating_letter("stress"), "t"),
        (first_non_repeating_letter("sTreSS"), "T"),
        (first_non_repeating_letter("sssssss"), ""),
        (first_non_repeating_letter("a"), "a"),
        (first_non_repeating_letter("moonmen"), "e"),
        (first_non_repeating_letter(""), ""),
        (first_non_repeating_letter("abba"), ""),
        (first_non_repeating_letter("~><#~><"), "#"),
        (first_non_repeating_letter("hello world, eh?"), "w"),
        (first_non_repeating_letter("Go hang a salami, I\'m a lasagna hog!"), ","),
    ]
    for t in tests:
        print(['failed', 'passed'][t[0] == t[1]], t[0])


if __name__ == "__main__":
    main()
