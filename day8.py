#!/usr/bin/env python3

from get_input import get_input, line_parser
from collections import defaultdict, namedtuple
import operator
import re

Update = namedtuple('Update', ['mod_reg', 'mod_func', 'mod_val', 'test_reg',
                               'test_func', 'test_val', 'line'])

OPERATORS = {
    '>': operator.gt,
    '<': operator.lt,
    '>=': operator.ge,
    '<=': operator.le,
    '==': operator.eq,
    '!=': operator.ne,
}

UPDATE = {
    "inc": operator.add,
    "dec": operator.sub,
}

# b inc 5 if a > 1
REGEX = ("""^(?P<mod_reg>\w+) (?P<mod_func>{}) (?P<mod_val>-?\d+)""" +
        """ if (?P<test_reg>\w+) (?P<test_func>{}) (?P<test_val>-?\d+)$""").format(
            "|".join(UPDATE.keys()), "|".join(OPERATORS.keys()))

def part1(operations):
    registers = defaultdict(int)
    for oper in operations:
        update(registers, oper)
    return max(v for v in registers.values())

def part2(operations):
    biggest = None
    registers = defaultdict(int)
    for oper in operations:
        update(registers, oper)
        max_val = max(v for v in registers.values())
        if biggest is None or max_val > biggest:
            biggest = max_val
    return biggest

def update(env, oper):
    if oper.test_func(env[oper.test_reg], oper.test_val):
        env[oper.mod_reg] = oper.mod_func(env[oper.mod_reg],
                                                    oper.mod_val)

def parser(line):
    try:
        match = re.match(REGEX, line).groupdict()
    except AttributeError:
        raise ValueError("Not a match {}".format(line))
    return Update(
        mod_reg=match['mod_reg'],
        mod_func=UPDATE[match['mod_func']],
        mod_val=int(match['mod_val']),
        test_reg=match['test_reg'],
        test_func=OPERATORS[match['test_func']],
        test_val=int(match['test_val']),
        line=line)

if __name__ == '__main__':
    lines = line_parser(get_input(day=8, year=2017), parse=parser)
    print("Part 1: {}".format(part1(lines)))
    print("Part 2: {}".format(part2(lines)))

