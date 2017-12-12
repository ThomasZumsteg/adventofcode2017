#!/usr/bin/env python3

from get_input import get_input, line_parser

def make_set(table, seed):
    seen = set()
    queue = [seed]
    while queue:
        p = queue.pop()
        if p not in seen:
            seen.add(p)
            queue.extend(table[p])
    return seen

def part1(table):
    return len(make_set(table, 0))

def part2(table):
    return len(set(frozenset(make_set(table, v)) for v in table.keys()))

def parse(line):
    ppid, pids = line.split(' <-> ')
    return (int(ppid), tuple(int(p) for p in pids.split(', ')))

if __name__ == '__main__':
    table = dict(line_parser(get_input(day=12, year=2017), parse=parse))
    print("Part 1: {}".format(part1(table)))
    print("Part 2: {}".format(part2(table)))
