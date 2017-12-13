#!/usr/bin/env python3

from get_input import get_input, line_parser
from copy import deepcopy
from itertools import count

def position(n, depth):
    if depth is None:
        return None
    elif depth <= 1:
        return 0
    return abs((n - (depth - 1)) % (2 * (depth - 1)) - (depth - 1))

def test_position():
    assert [position(n, 3) for n in range(6)] == [0,1,2,1,0,1]
    assert [position(n, 1) for n in range(6)] == [0,0,0,0,0,0]
    assert [position(n, 2) for n in range(6)] == [0,1,0,1,0,1]

class Firewall(object):
    def __init__(self, lines):
        self.depth = dict(lines)
        self.second = None 
        
    def __len__(self):
        return max(self.depth.keys()) + 1

    def __iter__(self):
        copy = deepcopy(self)
        if copy.second is not None:
            copy.second -= 1
        return copy
    
    def __next__(self):
        if self.second is None:
            self.second = 0
        else:
            self.second += 1
        return self

    def __getitem__(self, i):
        if i in self.depth:
            return position(self.second, self.depth[i])
        else:
            return None

def part1(lines):
    score = 0
    for sec, firewall in enumerate(Firewall(lines)):
        if sec >= len(firewall):
            return score
        elif firewall[sec] == 0:
            score += sec * firewall.depth[sec]
    return score

def test_part1():
    assert part1(((0,3),(1,2),(4,4),(6,4))) == 24

def part2(lines):
    for start_time, firewall_start in enumerate(Firewall(lines)):
        for sec, firewall in enumerate(firewall_start):
            if sec >= len(firewall):
                return start_time
            if firewall[sec] == 0:
                break

def test_part2():
    assert part2(((0,3),(1,2),(4,4),(6,4))) == 10

def parse(line):
    return tuple(int(i) for i in line.split(': '))

if __name__ == '__main__':
    lines = line_parser(get_input(day=13, year=2017), parse=parse)
    # Part 1: 2264
    # print('Test 1: {}'.format(part1(((0,3),(1,2),(4,4),(6,4)))))
    print('Part 1: {}'.format(part1(lines)))
    print('Part 2: {}'.format(part2(lines)))
    # print('Test 2: {}'.format(part2(((0,3),(1,2),(4,4),(6,4)))))
