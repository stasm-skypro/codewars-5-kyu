#!/usr/bin/env python3

"""The longest bracket substring in the string.
DESCRIPTION:
When no more interesting kata can be resolved, I just choose to create the new kata, to solve their
own, to enjoy the process --myjinxin2015 said.

Description:
Given a string str consisting of some number of "(" and ")" characters, your task is to find the
longest substring in str such that all "(" in the substring are closed by a matching ")".
The result is the length of that substring.

For example:
"()()(" => 4
Because "()()" is the longest substring, which has a length of 4.

Note:
All inputs are valid.
If no such substring found, return 0.
Please pay attention to the performance of code. ;-)
In the performance test(100000 brackets str x 100 testcases), the time consuming of each test case
should be within 35ms. This means, your code should run as fast as a rocket ;-).

Some Examples
 "" => 0
"()" => 2
"()(" => 2
"()()" => 4
"()()(" => 4
"(()())" => 6
"(()(())" => 6
"())(()))" => 4
"))((" => 0."""


def time_it(func, number=10):
    """Функция принимает на входе в качестве аргумента функцию, для которой необходимо измерить
    время её выполенения."""
    from time import perf_counter

    for _ in range(number):

        def measure(*args, **kwars):
            start = perf_counter()
            result = func(*args, **kwars)
            print(perf_counter() - start)
            return result

    return measure


# @time_it
def count_brackets1(string: str):
    """Алгоритм работает на всех примерах. Но недостаток в использовании вложенного цикла."""
    longest = 0
    d = dict()
    for i in range(len(string)):
        counter = 0
        t = []
        if string[i] == "(":
            counter += 1
            t.append(string[i])
            for j in range(i + 1, len(string)):
                if string[j] == "(":
                    counter += 1
                elif string[j] == ")":
                    counter -= 1
                if counter != -1:
                    t.append(string[j])
                if counter == 0:
                    l = len(t)
                    if l not in d:
                        d[l] = t
                if counter == -1:
                    t = []
                    counter = 0
    if d:
        longest = max(d)
    return longest


# @time_it
def count_brackets2(string: str):
    """Алгоритм работает на всех примерах. Оптимизирован в сравнении с предыдущим.
    Но недостаток в использовании вложенного цикла."""
    longest = 0
    #d = set()
    for i in range(len(string)):
        counter = 0
        t = 0
        if string[i] == "(":
            counter += 1
            t += 1
            for j in range(i + 1, len(string)):
                if string[j] == "(":
                    counter += 1
                elif string[j] == ")":
                    counter -= 1
                if counter != -1:
                    t += 1
                if counter == 0:
                    longest = max(longest, t)
                if counter == -1:
                    t = 0
                    counter = 0
    return longest


# @time_it
def count_brackets3(string: str):
    """Алгоритм работает на всех примерах. Я попытался уменьшить асимптротику, заменив в первом for
    проход по всем элементам на проход по заранее найденным индексам."""
    opens = []
    for i, b in enumerate(string):
        if b == "(":
            opens.append(string.index(b, i))
    longest = 0
    for i in opens:
        counter = 1
        t = 1
        for j in range(i + 1, len(string)):
            b = string[j]
            if b == "(":
                counter += 1
            elif b == ")":
                counter -= 1
            if counter != -1:
                t += 1
            if counter == 0:
                longest = max(longest, t)
            if counter == -1:
                t = 0
                counter = 0
    return longest


# @time_it
def count_brackets4(string: str):
    """Ещё один алгоритм со стеком за O(n).
    https://stackoverflow.com/questions/25952326/find-the-length-of-the-longest-valid-parenthesis-sequence-in-a-string-in-on-t
    Работает на всех примерах."""

    lenstring = len(string)
    longest, last = 0, -1
    if lenstring in (0, 1):
        return 0

    stack = []
    for i in range(lenstring):
        if string[i] == "(":
            stack.append(i)
        else:
            if len(stack) == 0:
                last = i
            else:
                stack.pop()
                if len(stack) == 0:
                    longest = max(longest, i - last)
                else:
                    longest = max(longest, i - stack[-1])
    return longest


def count_brackets5(string):
    stack, longest = [-1], 0
    for i, b in enumerate(string):
        if b == "(":
            stack.append(i)
        else:
            stack.pop()
            if stack:
                longest = max(longest, i - stack[-1])
            else:
                stack.append(i)
    return longest


@time_it
def main():
    for fun in (
        # count_brackets1,
        # count_brackets2,
        # count_brackets3,
        # count_brackets4,
        count_brackets5,
    ):
        tests = [
            (fun("()"), 2),
            (fun("()("), 2),
            (fun("()()"), 4),
            (fun("()()("), 4),
            (fun("(()())"), 6),
            (fun("(()(())"), 6),
            (fun("())(()))"), 4),
            (fun("))(("), 0),
            (fun("))(())"), 4),
            (fun(""), 0),
            (fun("(()(()())"), 8),
            (fun(")(((((((())))(()(()())"), 8),
            (fun("(((()(()((()(((())())()()())))(()"), 24),
        ]
        for t in tests:
            print(["fail", "OK"][t[0] == t[1]], t[0])
        print()


if __name__ == "__main__":
    main()
