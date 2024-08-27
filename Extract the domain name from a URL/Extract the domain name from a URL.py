#! /usr/bin/env python3

"""ОПИСАНИЕ:
Напишите функцию, которая при задании URL-адреса в виде строки анализирует только доменное имя и
возвращает его в виде строки. Например:
* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"."""


def get_domain_name(url: str):
    t = url.replace("http://", "").replace("https://", "").replace("www.", "")
    return t.split('.')[0]


def get_domain_name2(url: str):
    """Решение дамьян."""
    from re import findall, VERBOSE

    try:
        url = findall("""\A
                            (?: http
                            s?
                            ://)?         # matches http:// or https:// or nothing

                            (?: www.)?    # matches www. or nothing

                            ([- a-z]+)    # matches a sequence of letters and dashes

                            (?: .com|.ru)     # matches either .com or .ru
                            (?: [/ a-z]+)?    # matches a sequence or letters and slashes
                            \Z""", url, VERBOSE)
        return url[0]
    except:
        return "Invalid URL."


def main():
    tests = {
        (get_domain_name("http://github.com/carbonfive/raygun"), "github"),
        (get_domain_name("http://www.zombie-bites.com"), "zombie-bites"),
        (get_domain_name("https://www.cnet.com"), "cnet"),
    }
    for t in tests:
        print(['failed', 'passed'][t[0] == t[1]], t[0])


if __name__ == "__main__":
    main()
