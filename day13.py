#!/usr/bin/env python3

from get_input import get_input, line_parser
from itertools import count

def packets_caught(start_time, firewall):
    for position, depth in firewall.items():
        if (start_time + position) % (2 * (depth - 1)) == 0:
            yield position, depth

def part1(firewall):
    return sum(layer * depth for layer, depth in packets_caught(0, firewall))

def test_part1():
    assert part1({0:3, 1:2, 4:4, 6:4}) == 24

def part2(firewall):
    for start_time in count():
        if not any(True for _ in packets_caught(start_time, firewall)):
            return start_time

def test_part2():
    assert part2({0:3, 1:2, 4:4, 6:4}) == 10

def parse(line):
    return tuple(int(i) for i in line.split(': '))

if __name__ == '__main__':
    firewall = dict(line_parser(get_input(day=13, year=2017), parse=parse))
    # Part 1: 2264
    # Part 2: 3875838
    print('Part 1: {}'.format(part1(firewall)))
    print('Part 2: {}'.format(part2(firewall)))
