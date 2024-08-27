#!/usr/bin/env python3

"""ОПИСАНИЕ:
Команда маркетинга тратит слишком много времени на ввод хэштегов.
Давайте поможем им с помощью нашего собственного генератора хэштегов!

Вот в чем дело:
Он должен начинаться с хэштега (#).
Первая буква всех слов должна быть заглавной.
Если конечный результат длиннее 140 символов, он должен вернуться false.
Если входные данные или результат представляют собой пустую строку, она должна возвращать false.
Примеры
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false"""


def generate_hashtag(s: str):
    res = '#' + s.title().replace(' ', '')
    return res if s != "" and len(res) < 140 else False


def main():
    tests = [
        (generate_hashtag(" Hello there thanks for trying my Kata"),
         "#HelloThereThanksForTryingMyKata"),
        (generate_hashtag("    Hello     World   "), "#HelloWorld"),
        (generate_hashtag('Codewars'), '#Codewars', 'Should handle a single word.'),
        (generate_hashtag('Codewars      '), '#Codewars', 'Should handle trailing whitespace.'),
        (generate_hashtag('      Codewars'), '#Codewars', 'Should handle leading whitespace.'),
        (generate_hashtag('Codewars Is Nice'), '#CodewarsIsNice', 'Should remove spaces.'),
        (generate_hashtag('codewars is nice'), '#CodewarsIsNice', 'Should capitalize first '
                                                                  'letters of words.'),
        (generate_hashtag('CoDeWaRs is niCe'), '#CodewarsIsNice', 'Only the first letter of each '
                                                                  'word should be capitalized in the final hashtag, all other letters must be lower case.'),
        (generate_hashtag('c i n'), '#CIN',
         'A single letter is considered to be a word of length 1, so should capitalize first letters of words of length 1.'),
        (generate_hashtag('codewars  is  nice'), '#CodewarsIsNice',
         'Should deal with unnecessary middle spaces.'),
        (generate_hashtag(""), False),
    ]

    for t in tests:
        print(['fail', 'passed'][t[0] == t[1]], t[0])


if __name__ == "__main__":
    main()
