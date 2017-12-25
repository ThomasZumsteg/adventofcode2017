#!/usr/bin/env python3

from get_input import get_input, line_parser
from collections import defaultdict
import re

def part1(state, steps, machine):
    tape = defaultdict(int)
    p = 0
    for _ in range(steps):
        write, move, state = machine[state][tape[p]]
        tape[p] = int(write)
        p += 1 if move == 'right' else -1
    return sum(tape.values())

def test_part1():
    text = """Begin in state A.
Perform a diagnostic checksum after 6 steps.

In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state B.

In state B:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A.\n"""
    start, steps, machine = parse(text)
    assert 3 == part1(start, steps, machine)

def parse(text):
    initial = re.compile('Begin in state (.).\n' + 
        'Perform a diagnostic checksum after (\d+) steps.\n\n')

    step = re.compile("""In state (?P<state>.):
  If the current value is 0:
    - Write the value ([01]).
    - Move one slot to the (right|left).
    - Continue with state (.).
  If the current value is 1:
    - Write the value (0|1).
    - Move one slot to the (left|right).
    - Continue with state (.).\n\n?""")

    state, steps = None, None
    machine = {}
    while text:
        m = step.match(text)
        if m is None:
            m = initial.match(text)
            state = m.group(1)
            steps = int(m.group(2))
        else:
            machine[m.group(1)] = (tuple(m.groups()[1:4]), tuple(m.groups()[4:]))
        text = text[m.end():]
    return state, steps, machine

if __name__ == '__main__':
    state, steps, machine = parse(get_input(day=25, year=2017))
    print("Part 1: {}".format(part1(state, steps, machine)))
