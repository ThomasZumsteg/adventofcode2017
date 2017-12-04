#!/usr/bin/env python3

from get_input import get_input

def part1(lines):
    return len([1 for line in lines if len(set(line)) == len(line)])

def part2(lines):
    passwords = [[tuple(sorted(word)) for word in line] for line in lines]
    return part1(passwords)

if __name__ == '__main__':
    lines = [line.split() for line in get_input(4, 2017).splitlines()]
    print("Part 1: {}".format(part1(lines)))
    print("Part 2: {}".format(part2(lines)))

