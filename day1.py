#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def main():
    input_file = sys.argv[1]
    with open(input_file) as f:
        max_calories = sum(sorted([sum(list(map(int, x.split()))) for x in f.read().split("\n\n")])[-3:])
    print(f"The sum of three maxima is {max_calories}")

if __name__ == '__main__':
    main()