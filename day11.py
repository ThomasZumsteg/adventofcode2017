#!/usr/bin/env python3

from get_input import get_input, line_parser
from collections import Counter

class HexStepCounter(object):
    directions = {
        'n': (1,0,0),
        's': (-1,0,0),
        'ne': (0,1,0),
        'sw': (0,-1,0),
        'se': (0,0,1),
        'nw': (0,0,-1),
    }
    def __init__(self):
        self.location= (0,0,0)

    def __iadd__(self, step):
        if step not in self.directions.keys():
            raise ValueError("Not a legal direction: {}".format(step))
        self.location = tuple(a + b for a, b in
                              zip(self.location, self.directions[step]))
        return self

    @property
    def distance(self):
        distances = sorted(abs(l) for l in self.location)
        # XXX: Fix me
        pass

def replace(a, b, r, values):
    diff = min(values[a], values[b])
    values[a] -= diff
    values[b] -= diff
    if r is not None:
        values[r] += diff

def part1(steps):
    count_steps = Counter(steps)
    replace('n', 's', None, count_steps)
    replace('ne', 'sw', None, count_steps)
    replace('nw', 'se', None, count_steps)
    replace('nw', 'ne', 'n', count_steps)
    replace('sw', 'se', 's', count_steps)
    replace('ne', 's', 'se', count_steps)
    replace('sw', 'n', 'nw', count_steps)
    replace('nw', 's', 'sw', count_steps)
    replace('se', 'n', 'ne', count_steps)
    # step_counter = HexStepCounter()
    # for step in steps:
    #     step_counter += step
    return sum(abs(v) for v in count_steps.values())

def test_part1():
    assert part1('ne,ne,ne'.split(',')) == 3
    assert part1('ne,ne,sw,sw'.split(',')) == 0
    assert part1('ne,ne,s,s'.split(',')) == 2
    assert part1('se,sw,se,sw,sw'.split(',')) == 3

def part2(directions):
    furthest = 0
    for i in range(len(directions)):
        furthest = max(furthest, part1(directions[:i]))
    return furthest

if __name__ == '__main__':
    # Part 1: 707
    # Part 2: 1490

    directions = line_parser(get_input(day=11, year=2017).strip(), parse=str, seperator=',')
    print("Part 1: {}".format(part1(directions)))
    print("Part 2: {}".format(part2(directions)))
