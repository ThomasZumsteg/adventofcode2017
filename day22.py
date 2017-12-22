#!/usr/bin/env python3

from get_input import get_input, line_parser
import copy
from collections import defaultdict

turn_left = lambda d: (-d[1], d[0])
turn_right = lambda d: (d[1], -d[0])
reverse = lambda d: (-d[0], -d[1])
move = lambda p, d: (p[0] + d[0], p[1] + d[1])

def part1(inp,iters=10000):
    grid = copy.copy(inp)
    pos, head = (0, 0), (-1,0)
    count = 0
    for _ in range(iters):
        if grid[pos] == '.':
            head = turn_left(head)
            grid[pos] = '#'
            count += 1
        elif grid[pos] == '#':
            head = turn_right(head)
            grid[pos] = '.'
        pos = move(pos, head)
    return count

def test_part1():
    test = "..#\n#..\n...".splitlines()
    assert 41 == part1(parse(test), iters=70)

def part2(inp, iters=10000000):
    grid = copy.copy(inp)
    pos, head = (0, 0), (-1,0)
    count = 0
    for _ in range(iters):
        if grid[pos] == '.':
            head = turn_left(head)
            grid[pos] = 'W'
        elif grid[pos] == 'W':
            count += 1
            grid[pos] = '#'
        elif grid[pos] == 'F':
            grid[pos] = '.'
            head = reverse(head)
        elif grid[pos] == '#':
            head = turn_right(head)
            grid[pos] = 'F'
        pos = move(pos, head)
    return count

def test_part2():
    test = "..#\n#..\n...".splitlines()
    assert 26 == part2(parse(test), iters=100)
    assert 2511944 == part2(parse(test), iters=10000000)

def parse(lines):
    grid = defaultdict(lambda: '.')
    height, width = len(lines), len(lines[0])
    for r, row in enumerate(lines, -(height//2)):
        for c, char in enumerate(row, -(width//2)):
            grid[(r,c)] = char
    return grid

if __name__ == '__main__':
    grid = parse(get_input(day=22, year=2017).splitlines())
    print('Part 1: {}'.format(part1(grid)))
    print('Part 2: {}'.format(part2(grid)))
