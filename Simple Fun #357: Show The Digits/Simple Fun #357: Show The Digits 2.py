#! /usr/bin/env/ python3

"""You are given a string digits and an integer size(1-9). Your task is to
generate a result like this:

show("888",1) ===
 -  -  -
| || || |
 -  -  -
| || || |
 -  -  -

show("888",2) ===
 --  --  --
|  ||  ||  |
|  ||  ||  |
 --  --  --
|  ||  ||  |
|  ||  ||  |
 --  --  --

show("1234567890",3) ===
      ---  ---       ---  ---  ---  ---  ---  ---
    |    |    ||   ||    |        ||   ||   ||   |
    |    |    ||   ||    |        ||   ||   ||   |
    |    |    ||   ||    |        ||   ||   ||   |
      ---  ---  ---  ---  ---       ---  ---
    ||        |    |    ||   |    ||   |    ||   |
    ||        |    |    ||   |    ||   |    ||   |
    ||        |    |    ||   |    ||   |    ||   |
      ---  ---       ---  ---       ---  ---  ---
As you can see:
Use '-' represents the horizontal line; Use '|' represents the vertical line.
size determines the length of the horizontal line and the height of the
vertical line. i.e. If size is 1, the horizontal line is -; If size is 2, the
horizontal line is --. and so on..
Each row is separated by "\n".
To keep shapes, other places are filled with spaces. Except for the end of
each line."""


def gen_numbers(digits, l):
    s = ' '  # space
    d = '-'  # dash
    p = '|'  # pipeline

    t = {
      0: [s+d*l+s, p+s*l+p, s+s*l+s, p+s*l+p, s+d*l+s],
      1: [s+s*l+s, s+s*l+p, s+s*l+s, s+s*l+p, s+s*l+s],
      2: [s+d*l+s, s+s*l+p, s+d*l+s, p+s+s*l, s+d*l+s],
      3: [s+d*l+s, s+s*l+p, s+d*l+s, s+s*l+p, s+d*l+s],
      4: [s+s*l+s, p+s*l+p, s+d*l+s, s+s*l+p, s+s*l+s],
      5: [s+d*l+s, p+s+s*l, s+d*l+s, s+s*l+p, s+d*l+s],
      6: [s+d*l+s, p+s+s*l, s+d*l+s, p+s*l+p, s+d*l+s],
      7: [s+d*l+s, s+s*l+p, s+s*l+s, s+s*l+p, s+s*l+s],
      8: [s+d*l+s, p+s*l+p, s+d*l+s, p+s*l+p, s+d*l+s],
      9: [s+d*l+s, p+s*l+p, s+d*l+s, s+s*l+p, s+d*l+s]
    }

    out = """"""
    for i in range(5):
        row = ""
        for d in digits:
            k = int(d)
            sym = t[k][i]
            row = row + sym
        row = row.rstrip()
        if p in row:
            row = (row + '\n')*l
            row = row.rstrip('\n')
        out = out + row + '\n'
    out = out.rstrip('\n')
    if out[-1] == '|':
        out = out + '\n'

    return out


def main():
    tests = [
      (("888", 1), """\
 -  -  -
| || || |
 -  -  -
| || || |
 -  -  -"""),
      (("888", 2), """\
 --  --  --
|  ||  ||  |
|  ||  ||  |
 --  --  --
|  ||  ||  |
|  ||  ||  |
 --  --  --"""),
      (("000", 2), """\
 --  --  --
|  ||  ||  |
|  ||  ||  |

|  ||  ||  |
|  ||  ||  |
 --  --  --"""),
      (("111", 2), """\

   |   |   |
   |   |   |

   |   |   |
   |   |   |"""),
      (("222", 2), """\
 --  --  --
   |   |   |
   |   |   |
 --  --  --
|   |   |
|   |   |
 --  --  --"""),
      (("333", 2), """\
 --  --  --
   |   |   |
   |   |   |
 --  --  --
   |   |   |
   |   |   |
 --  --  --"""),
      (("444", 2), """\

|  ||  ||  |
|  ||  ||  |
 --  --  --
   |   |   |
   |   |   |"""),
      (("555", 2), """\
 --  --  --
|   |   |
|   |   |
 --  --  --
   |   |   |
   |   |   |
 --  --  --"""),
      (("666", 2), """\
 --  --  --
|   |   |
|   |   |
 --  --  --
|  ||  ||  |
|  ||  ||  |
 --  --  --"""),
      (("777", 2), """\
 --  --  --
   |   |   |
   |   |   |

   |   |   |
   |   |   |"""),
      (("888", 2), """\
 --  --  --
|  ||  ||  |
|  ||  ||  |
 --  --  --
|  ||  ||  |
|  ||  ||  |
 --  --  --"""),
      (("999", 2), """\
 --  --  --
|  ||  ||  |
|  ||  ||  |
 --  --  --
   |   |   |
   |   |   |
 --  --  --"""),
      (("123", 1), """\
    -  -
  |  |  |
    -  -
  ||    |
    -  -"""),

      (("1234567890", 3), """\
      ---  ---       ---  ---  ---  ---  ---  ---
    |    |    ||   ||    |        ||   ||   ||   |
    |    |    ||   ||    |        ||   ||   ||   |
    |    |    ||   ||    |        ||   ||   ||   |
      ---  ---  ---  ---  ---       ---  ---
    ||        |    |    ||   |    ||   |    ||   |
    ||        |    |    ||   |    ||   |    ||   |
    ||        |    |    ||   |    ||   |    ||   |
      ---  ---       ---  ---       ---  ---  ---"""),
      (("1", 2), """\n   |\n   |\n\n   |\n   |\n"""),
      (("477", 2), """     --  --\n|  |   |   |\n|  |   |   |\n --\n   |   |   |\n   |   |   |\n""")
    ]

    func = gen_numbers
    for t in tests:
        res = func(t[0][0], t[0][1])
        print(['fail', 'passed'][res == t[1]])
        print("original:")
        print(t[1])
        print("result:")
        print(res)


if __name__ == "__main__":
    main()
