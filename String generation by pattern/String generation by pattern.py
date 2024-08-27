#! /usr/bin/env python3

"""ОПИСАНИЕ:
Реализуйте генератор, который по заданному шаблону возвращает строки, следующие такому шаблону.
В этом ката шаблоном называется строка, состоящая из символов, цифр, знаков препинания
(за исключением квадратных скобок) и токенов, которые должны быть заменены значением, необходимым
для построения следующей строки в последовательности.
Существует четыре типа токенов:
[INC_INT=START,STEP]: Увеличивающее целое число, каждый раз, когда в генераторе вызывается
следующая функция: фактическое целое число помещается в строку, а затем пошагово увеличивается.
Значениями по умолчанию для START и STEP являются 1 и 1;
[INC_FLOAT=START,STEP]: Увеличение числа с плавающей запятой, каждый раз, когда в генераторе
вызывается следующая функция, фактическое число с плавающей запятой помещается в строку, а затем
увеличивается с шагом. Значениями по умолчанию для START и STEP являются 0.1 и 0.1.
[INC_FLOAT] Токен получает точность с плавающей запятой от параметра, в котором содержится
наибольшее количество десятичных разрядов (также учитываются конечные нули). Числа с плавающей
запятой, передаваемые в качестве параметров, могут быть очень маленькими (наименьшее возможное
число 0.0000000001);
[INTERVAL=FIRST,LAST]: Интервал целых чисел, начинающийся с ПЕРВОГО и заканчивающийся ПОСЛЕДНИМ
(оба включены). При достижении ПОСЛЕДНЕГО токен перезапускает интервал с ПЕРВОГО. Значениями
по умолчанию для FIRST и LAST являются 1 и 1. Если задан только один параметр, LAST равен FIRST;
[PERIODIC=START,N]: Каждый раз, когда создается N строк, значение увеличивается на единицу.
Значениями по умолчанию для START и N являются 1 и 1. Обратите внимание, что в тестах N всегда >= 1.
Как уже упоминалось, токены имеют значения по умолчанию: это означает, что вы можете найти токены
с 0, 1 или 2 параметрами. Если задан только один параметр, он является первым в спецификации токена.
Примеры:
INPUT: "Testing [INC_INT], [INC_INT=2], [INC_INT=3,2]"
OUTPUT: "Testing 1, 2, 3", "Testing 2, 3, 5", "Testing 3, 4, 7", "Testing 4, 5, 9",
"Testing 5, 6, 11", "Testing 6, 7, 13", "Testing 7, 8, 15" ...

INPUT: "x=[INC_FLOAT], y=[INC_FLOAT=0.33], z=[INC_FLOAT=0.2,0.004]"
OUTPUT: "x=0.1, y=0.33, z=0.200", "x=0.2, y=0.43, z=0.204", "x=0.3, y=0.53, z=0.208",
"x=0.4, y=0.63, z=0.212", "x=0.5, y=0.73, z=0.216", "x=0.6, y=0.83, z=0.220" ...

INPUT: "Season [PERIODIC=1,5], Episode [INTERVAL=1,5]"
OUTPUT: "Season 1, Episode 1", "Season 1, Episode 2", "Season 1, Episode 3", "Season 1, Episode 4",
"Season 1, Episode 5", "Season 2, Episode 1", "Season 2, Episode 2", "Season 2, Episode 3" ...

Обратите внимание, что внутри токенов могут быть пробелы, например, вы можете найти такие токены,
как [INC_FLOAT = 0.2 , 0.500]. Все шаблоны, приведенные в качестве входных данных, действительны,
нет необходимости проверять наличие ошибок. Если в шаблоне не найдено токенов, генератор просто
генерирует строку при каждом вызове следующей функции."""

# TODO: дорешать задачу.

def parse_token(token: str):
    token = token[1:-1]
    token = token.replace(' ', '').replace('=', '#').replace(',', '#')
    token_list = token.split('#')
    oper, start, step = None, None, None
    if len(token_list) == 3:
        oper = token_list[0]
        start = token_list[1]
        step = token_list[2]
    elif len(token_list) == 2:
        oper = token_list[0]
        start = token_list[1]
        if oper == "INC_FLOAT":
            step = 0.1
        else:
            step = 1
    elif len(token_list) == 1:
        oper = token_list[0]
        if oper == "INC_FLOAT":
            start = 0.1
            step = 0.1
        else:
            start = 1
            step = 1
    return oper, start, step


def string_generator1(string: str):
    string = string.replace('[', '#[').replace(']', ']#')
    string_lst = [el for el in string.split('#') if el != '']
    print(string_lst)

    tokens = ["INC_INT", "INC_FLOAT", "INTERVAL", "PERIODIC"]

    res = ""
    for el in string_lst:
        for tok in tokens:
            if tok in el:
                oper, start, step = parse_token(el)
                # print(oper, start, step)
                if oper == "[INC_INT]":
                    oper = 1
                elif oper == "[INC_FLOAT]":
                    oper = 0.1
                elif oper == "[INTERVAL]":
                    oper = 1
                elif oper == "[PERIODIC]":
                    oper = 1
                res = res + str(oper)
                break
    print(res)


def string_generator(string: str):
    res, tok = "", ""
    
    i = 0
    while i < len(string):
        if string[i] != '[':
            res = res + string[i]
        else:
            j = i
            while string[j] != ']':
                tok = tok + string[j]
                j = j + 1
            tok = tok + string[j]
            oper, start, step = parse_token(tok)
            tok = ""
            res = res + str(start)
            i = j
        i = i + 1
    yield res


def main():
    func = string_generator
    tests = [
        "[INC_INT]",
        # "[INTERVAL]",
        # "[PERIODIC]",
        # "[INTERVAL=0]",
        # "[INTERVAL=15,20]",
        # "[INC_INT=7,0]",
        # "[PERIODIC=0]",
        # "[PERIODIC=1]",
        # "[PERIODIC=7,1]",
        # "[PERIODIC=1,10000000]",
        # "Hello World[INC_INT]!",
        # "I have [INC_INT=3,2] dogs",
        # "[INC_FLOAT=2.3,0.000100]",
        # "Season [PERIODIC=1,4], Episode [INTERVAL=1,4]",
        # "[ INC_INT = 200  ,  3  ], [  INC_FLOAT]",
        # "[INC_INT]hello [INTERVAL =1 ,4], [PERIODIC= 1, 2]",
        # "[INC_FLOAT]+[INC_FLOAT=1.2]+[INC_FLOAT = 1.3, 1.0001]",
        # "Testing small floats: [INC_FLOAT=0.000001,0.000000003]",
        # "No Tokens",
        # "",
        # "[INC_INT]}",
    ]
    results = [
        ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"],
        # ["1", "1", "1", "1", "1", "1", "1", "1", "1"],
        # ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
        # ["0", "0", "0", "0", "0"],
        # ["15", "16", "17", "18", "19", "20", "15", "16", "17", "18"],
        # ["7", "7", "7", "7", "7"],
        # ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
        # ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
        # ["7", "8", "9", "10", "11", "12", "13", "14"],
        # ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
        # ["Hello World1!", "Hello World2!", "Hello World3!", "Hello World4!", "Hello World5!"],
        # ["I have 3 dogs", "I have 5 dogs", "I have 7 dogs", "I have 9 dogs", "I have 11 dogs",
        #  "I have 13 dogs"],
        # ["2.300000", "2.300100", "2.300200", "2.300300", "2.300400", "2.300500", "2.300600",
        #  "2.300700", "2.300800", "2.300900", "2.301000", "2.301100"],
        # ["Season 1, Episode 1", "Season 1, Episode 2", "Season 1, Episode 3", "Season 1, Episode 4",
        #  "Season 2, Episode 1", "Season 2, Episode 2"],
        # ["200, 0.1", "203, 0.2", "206, 0.3", "209, 0.4", "212, 0.5", "215, 0.6", "218, 0.7",
        #  "221, 0.8", "224, 0.9", "227, 1.0", "230, 1.1", "233, 1.2"],
        # ["1hello 1, 1", "2hello 2, 1", "3hello 3, 2", "4hello 4, 2", "5hello 1, 3", "6hello 2, 3",
        #  "7hello 3, 4", "8hello 4, 4", "9hello 1, 5", "10hello 2, 5", "11hello 3, 6"],
        # ["0.1+1.2+1.3000", "0.2+1.3+2.3001", "0.3+1.4+3.3002", "0.4+1.5+4.3003", "0.5+1.6+5.3004",
        #  "0.6+1.7+6.3005", "0.7+1.8+7.3006", "0.8+1.9+8.3007", "0.9+2.0+9.3008", "1.0+2.1+10.3009",
        #  "1.1+2.2+11.3010", "1.2+2.3+12.3011"],
        # ["Testing small floats: 0.000001000", "Testing small floats: 0.000001003",
        #  "Testing small floats: 0.000001006", "Testing small floats: 0.000001009",
        #  "Testing small floats: 0.000001012", "Testing small floats: 0.000001015",
        #  "Testing small floats: 0.000001018", "Testing small floats: 0.000001021",
        #  "Testing small floats: 0.000001024"],
        # ["No Tokens", "No Tokens", "No Tokens", "No Tokens", "No Tokens", "No Tokens", "No Tokens"],
        # ["", "", "", "", "", ""],
        # ["1}", "2}", "3}", "4}", "5}", "6}"],
    ]
    for i in range(len(tests)):
        gen = string_generator(tests[i])
        actual = []
        for _ in range(len(results[i])):
            actual.append(next(gen))
        print(['failed', 'passed'][actual == results[i]])


if __name__ == "__main__":
    main()
