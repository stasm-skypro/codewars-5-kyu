#!/usr/bin/env python3

""""""
from time import perf_counter



def main():
    start = perf_counter()
    print(f">>>code runs in: {(perf_counter() - start):0.6f}")


if __name__ == "__main__":
    main()
