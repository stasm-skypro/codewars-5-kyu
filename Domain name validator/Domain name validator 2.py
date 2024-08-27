#! /usr/bin/env python3

"""ОПИСАНИЕ:
В этом kata вам необходимо создать средство проверки доменных имен, в основном совместимое с RFC 1035, RFC 1123 и
RFC 2181.

Для целей данного ката применяются следующие правила:
Доменное имя может содержать поддомены (уровни), иерархически разделенные символом . (точка).
Доменное имя не должно содержать более 127 уровней, включая верхний уровень (TLD).
Имя домена не должно быть длиннее 253 символов (в RFC указано 255, но 2 символа зарезервированы для конечной точки и
нулевого символа для корневого уровня).
Имена уровней должны состоять из строчных и прописных букв ASCII, цифр и символа - (со знаком минус).
Имена уровней не должны начинаться или заканчиваться символом - (со знаком минус).
Имена уровней не должны быть длиннее 63 символов.
Верхний уровень (TLD) не должен быть полностью числовым.
Кроме того, в этом ката.
Доменное имя должно содержать по крайней мере один поддомен (уровень) помимо TLD
Проверка верхнего уровня должна быть наивной, т. е.. TLD, несуществующие в реестре IANA, по-прежнему считаются
действительными, пока они соответствуют приведенным выше правилам.
Функция проверки принимает строку с полным доменным именем и возвращает логическое значение, указывающее, является ли
доменное имя допустимым или нет.

Примеры:
validate('codewars'), False),
validate('g.co'), True),
validate('codewars.com'), True),
validate('CODEWARS.COM'), True),
validate('sub.codewars.com'), True),
validate('codewars.com-'), False),
validate('.codewars.com'), False),
validate('example@codewars.com'), False),
validate('127.0.0.1'), False),."""

import string
import re


VALID_CHARS = string.ascii_lowercase + string.digits + '-.'


def validate(domain_name: str) -> bool:
    """Checks Domain name."""

    levels = domain_name.split('.')
    tld = domain_name.split('.')[-1]

    # Доменное имя может содержать поддомены (уровни), иерархически разделенные символом . (точка).
    if domain_name.count('.') == 0:
        return False

    # Доменное имя не должно содержать более 127 уровней, включая верхний уровень (TLD).
    if domain_name.count('.') > 126:
        return False

    # Имя домена не должно быть длиннее 253 символов
    if len(domain_name) > 253:
        return False

    # Имена уровней должны состоять из строчных и прописных букв ASCII, цифр и символа - (со знаком минус)
    if not all(char in VALID_CHARS for char in domain_name.lower()):
        return False

    # Имена уровней не должны начинаться или заканчиваться символом - (со знаком минус)
    def f(x): return x.startswith('-') or x.endswith('-')
    if any(f(l) for l in levels):
        return False

    # Доменное имя не должно начинаться и/или заканчиваться символом '.'
    if '.' in [domain_name[0], domain_name[-1]]:
        return False
    # а также не должны содержать '..' в имени доменаÍ
    if '..' in domain_name:
        return False

    # Имена уровней не должны быть длиннее 63 символов
    def f(x): return len(x) > 63
    if any(f(l) for l in levels):
        return False

    # Верхний уровень (TLD) не должен быть полностью числовым
    if all(char.isdigit() for char in tld):
        return False

    return True


def validate2(domain_name):
    """Решение со страницы с ответами. Автор anter69, Igareck999, tristandrew1128."""
    return re.match('''
        (?=^.{,253}$)          # max. length 253 chars
        (?!^.+\.\d+$)          # TLD is not fully numerical
        (?=^[^-.].+[^-.]$)     # doesn't start/end with '-' or '.'
        (?!^.+(\.-|-\.).+$)    # levels don't start/end with '-'
        (?:[a-z\d-]            # uses only allowed chars
        {1,63}(\.|$))          # max. level length 63 chars
        {2,127}                # max. 127 levels
        ''', domain_name, re.X | re.I)


def validate3(domain_name):
    """Решение со страницы с ответами. Автор anter69."""
    return (
        # number of levels > 1 and < 127
        0 < domain_name.count('.') < 127 and
        # length of domain name < 254
        len(domain_name) < 254 and
        # only allowed characters
        set(domain_name.lower()) <= set('1234567890-qwertyuiopasdfghjklzxcvbnm.') and
        # levels cannot be empty
        all(map(len, domain_name.split('.'))) > 0 and
        # levels cannot start/end with '-'
        all(s[0] != '-' and s[-1] != '-' for s in domain_name.split('.')) and
        # lenght of level names < 64
        max(map(len, domain_name.split('.'))) < 64 and
        # TLD not fully numerical
        not domain_name.split('.')[-1].isdigit()
    )


def main():
    fun = validate
    tests = [
        (fun('codewars'), False),
        (fun('g.co'), True),
        (fun('codewars.com'), True),
        (fun('CODEWARS.COM'), True),
        (fun('sub.codewars.com'), True),
        (fun('codewars.com-'), False),
        (fun('.codewars.com'), False),
        (fun('example@codewars.com'), False),
        (fun('127.0.0.1'), False),
        (fun('q.fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'), False),
        (fun('foo-.bar.baz'), False),
        (fun('foo.-bar.baz'), False),
        (fun('foo.bar-.baz'), False),
        (fun('foo.bar.-baz'), False),
        (fun('foo.bar.baz-'), False),
        (fun('foo-.-bar-.-baz-'), False),
    ]
    for t in tests:
        print(['failed', 'passed'][t[0] == t[1]], t[0])


if __name__ == "__main__":
    main()
