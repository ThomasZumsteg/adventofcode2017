#!/usr/bin/env python3

from get_input import get_input, line_parser

def part1(lines, update=None):
    i, count = 0, 0
    lines = lines[:]
    if update is None:
        update = lambda x: x + 1
    while 0 <= i < len(lines):
        jump = lines[i]
        lines[i] = update(lines[i])
        count += 1
        i += jump
    return count

def part2(lines):
    return part1(lines, update=lambda x: x + 1 if x < 3 else x - 1)

if __name__ == '__main__':
    lines = line_parser(get_input(day=5, year=2017))
    print("Solution Part 1 {}".format(part1(lines)))
    print("Solution Part 2 {}".format(part2(lines)))
