#!/usr/bin/env python3

from get_input import get_input, line_parser
from collections import namedtuple

Garbage = namedtuple('Garbage', ['value'])
Group = namedtuple('Group', ['value', 'depth'])

def machine(items):
    state = 'read'
    stored = None
    groups = ['']
    depth = 0
    for i in items:
        if state == 'skip':
            state, stored = stored, None
            continue
        elif i == '!':
            stored, state = state, 'skip'
            continue

        groups = [g + i for g in groups]

        if state == 'garbage' and i == '>':
            state = 'read'
            yield Garbage(groups.pop())
        elif state == 'read':
            if i == '<':
                groups.append('<')
                state = 'garbage'
            elif i == '{':
                groups.append('{')
                depth += 1
            elif i == '}':
                yield Group(groups.pop(), depth)
                depth -= 1

def part1(line):
    total = 0
    for group in machine(line):
        if type(group) == Group:
            total += group.depth
    return total

def part2(line):
    total = 0
    for group in machine(line):
        if type(group) is Garbage:
            total += len(group.value) - 2
    return total

if __name__ == '__main__':
    line = get_input(day=9, year=2017)
    print("Part 1: {}".format(part1(line)))
    print("Part 2: {}".format(part2(line)))
