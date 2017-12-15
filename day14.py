#!/usr/bin/env python3

from get_input import get_input, line_parser
from day10 import knot_hash, dense_hash

def get_grid(inp):
    grid = []
    for i in range(128):
        h = knot_hash(inp + '-' + str(i))
        digits = ''.join([format(int(d, 16), '04b') for d in dense_hash(h)])
        grid.append(list(digits))
    return grid

def part1(grid):
    return sum(1 for row in grid for c in row if c == '1')

def test_part1():
    test = get_grid('flqrgnkx')
    actual = get_grid('hfdlxzhv')
    assert part1(test) == 8108
    assert part1(actual) == 8230

def part2(grid):
    seen = set()
    groups = []
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if (r,c) in seen or char != '1':
                continue
            queue = [(r,c)]
            group = set()
            while queue:
                p,q = queue.pop()
                if 0 <= p < len(grid) and 0 <= q < len(grid[p]) and \
                    (p, q) not in seen and grid[p][q] == '1':
                    queue.extend([(p-1,q),(p+1,q),(p,q-1), (p,q+1)])
                    seen.add((p,q))
                    group.add((p,q))
            groups.append(group)
    return groups

def test_part2():
    test = get_grid('flqrgnkx')
    actual = get_grid('hfdlxzhv')
    assert len(part2(test)) == 1242  
    assert len(part2(actual)) == 1103

if __name__ == '__main__':
    # Part 1: 8230
    # Part 2: 1103
    grid = get_grid('hfdlxzhv')
    print('Part 1: {}'.format(part1(grid)))
    print('Part 2: {}'.format(len(part2(grid))))
