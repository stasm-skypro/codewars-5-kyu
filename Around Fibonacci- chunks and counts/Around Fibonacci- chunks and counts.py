#! /usr/bin/env python3

"""ОПИСАНИЕ:
Еще один Фибоначчи... да, но с другими видами результатов. Функция называется aroundFib или
around_fib, в зависимости от языка. Его параметром является n (положительное целое число).
Сначала вам нужно вычислить f значение fibonacci(n) с помощью fibonacci(0) --> 0 и 
fibonacci(1) --> 1 (см.: https://en.wikipedia.org/wiki/Fibonacci_number).
Найдите количество каждой цифры ch в f (ch: цифра от 0 до 9), назовите это значение cnt и найдите
максимальное значение cnt; назовите это максимальное значение maxcnt. Если есть связи, то цифра,
которую ch следует учитывать, является первой - в натуральном порядке следования цифр maxcnt.
Разделите значение f на фрагменты не более длины 25. Последний фрагмент может быть длиной 25 или
меньше.
Example: for `n=100` you have only one chunk `354224848179261915075`.
Example: for `n=180` f is `18547707689471986212190138521399707760` and you have two chunks 
`1854770768947198621219013` and `8521399707760`. First length here is 25 and second one is 13.
Наконец, верните строку в следующем формате:
"Последний фрагмент ...; Максимум равен ... для цифр ... ",
где Max - это maxcnt первая цифра ch (через 0..9), ведущая к maxcnt.
Example: for `n=100` -> "Last chunk 354224848179261915075; Max is 3 for digit 1" 
Example: for `n=180` -> "Last chunk 8521399707760; Max is 7 for digit 7"
Example: for `n=18000` -> "Last chunk 140258776000; Max is 409 for digit 1"
Будьте осторожны:
fib(18000) содержит 3762 цифры. Значения n находятся между 500 и 25000."""
    

def around_fib_a1(n):
    fib = lambda n: pow(2 << n, n + 1, (4 << 2 * n) - (2 << n) - 1) % (2 << n)
    f = fib(n)
    sf = str(f)
    maxcnt = 0
    maxd = dict()
    for ch in sf:
        cnt = sf.count(ch)
        if cnt >= maxcnt:
            maxcnt = cnt
            if cnt not in maxd:
                maxd[cnt] = []
            if ch not in maxd[cnt]:
                maxd[cnt].append(ch)
    lk = sorted(maxd.keys())[-1]
    m = maxd[lk][-1]

    ln = len(sf)
    last = ln % 25
    lastchunk = sf[-last::]
    return f"Last chunk {lastchunk}; Max is {maxcnt} for digit {m}"


def around_fib_a2(n):
    """Это решение  прошло проверку и было принято. Но в проследтвии я нашёл где оптимизировать."""
    fib = lambda n: pow(2 << n, n + 1, (4 << 2 * n) - (2 << n) - 1) % (2 << n)

    sf = str(fib(n))
    maxcnt, maxd = 0, dict()
    for ch in sf:
        cnt = sf.count(ch)
        if cnt >= maxcnt:
            maxcnt = cnt
            if cnt not in maxd:
                maxd[cnt] = []
            if ch not in maxd[cnt]:
                maxd[cnt].append(ch)
    lk = sorted(maxd.keys())[-1]
    m  = sorted(maxd[lk])[0]

    ln = len(sf)
    rem = ln % 25
    if rem == 0:
        rem = 25
    chunk = sf[-rem::]

    return f"Last chunk {chunk}; Max is {maxcnt} for digit {m}"


def around_fib(n):
    # fib = lambda n: pow(2 << n, n + 1, (4 << 2 * n) - (2 << n) - 1) % (2 << n)
    a, b = 0, 1
    for i in range(n - 1):
        a, b = b, a + b
    f = str(b)
    
    maxcnt, m = 0, -1
    for i in "0123456789":
        cnt = f.count(i)
        if cnt > maxcnt:
            maxcnt = cnt
            m = i
    
    rem = len(f) % 25
    if rem == 0: rem = 25
    chunk = f[-rem::]

    return f"Last chunk {chunk}; Max is {maxcnt} for digit {m}"


def main():
    fun = around_fib_a2
    tests = [
        (fun(100), "Last chunk 354224848179261915075; Max is 3 for digit 1"),
        (fun(180), "Last chunk 8521399707760; Max is 7 for digit 7"),
        (fun(18000), "Last chunk 140258776000; Max is 409 for digit 1"),
        (fun(666), "Last chunk 56699078708088; Max is 18 for digit 8"),
        (fun(934), "Last chunk 78863403327510987087; Max is 30 for digit 7"),
    ]
    for t in tests:
        print(['fail', 'OK'][t[0] == t[1]], t[0])


if __name__ == "__main__":
    main()
