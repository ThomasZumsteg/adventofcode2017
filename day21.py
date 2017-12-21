#!/usr/bin/env python3

from itertools import product
from get_input import get_input, line_parser

BASE = tuple(tuple(line) for line in ".#.\n..#\n###".splitlines())

def part1(patters, iters=5):
    result = BASE
    for _ in range(iters):
        size = len(result)
        if len(result) % 2 == 0:
            sub_map = sub_divide(result, 2)
        elif len(result) % 3 == 0:
            sub_map = sub_divide(result, 3)
        join_result = tuple(tuple(patters[m] for m in maps) for maps in sub_map)
        result = join(join_result)
    return sum(1 for row in result for c in row if c == '#')


def test_part1():
    test = """../.# => ##./#../...\n.#./..#/### => #..#/..../..../#..#\n"""
    patters = parse(test)
    assert part1(patters, iters=2) == 12

def join(sub_grids):
    sub_size = len(sub_grids[0][0])
    result = []
    for row in sub_grids:
        for sub_row in range(sub_size):
            result.append([])
            for col in row:
                result[-1].extend(col[sub_row])
    return tuple(tuple(row) for row in result)
                
def sub_divide(grid, s):
    size = len(grid) - 1
    sub_maps = [[None for _ in range(0, size, s)] for _ in range(0, size, s)]
    for n, m in product(range(0, size, s), range(0, size, s)):
        sub_maps[n//s][m//s] = tuple(tuple(grid[j][m:m+s]) for j in range(n,n+s))
    return tuple(tuple(m) for m in sub_maps)

def part2(patters, iters=18):
    return part1(patters, iters=18)

def rotate(grid):
    rows, cols = len(grid), len(grid[0])
    result = [[None for _ in range(rows)] for _ in range(cols)]
    for r,c in product(range((rows+1)//2), range((cols+1)//2)):
        result[c][r] = grid[rows-r-1][c]
        result[cols-c-1][r] = grid[rows-r-1][cols-c-1]
        result[cols-c-1][rows-r-1] = grid[r][cols-c-1]
        result[c][rows-r-1] = grid[r][c]
    return tuple(tuple(l) for l in result)

def test_rotate():
    assert rotate((('00', '01'),('10','11'))) == (('10', '00'),('11','01'))
    assert rotate((('00','01','02'), ('10','11','12'), ('20','21','22'))) == \
        (('20','10','00'), ('21','11','01'), ('22','12','02'))

def parse(text):
    patters = {}
    for line in text.splitlines():
        find, replace = (tuple(tuple(row) for row in grid.split('/')) 
                for grid in line.split(" => "))

        for find_me in (find, tuple(reversed(find))):
            for _ in range(4):
                patters[find_me] = replace
                find_me = rotate(find_me)

    return patters

if __name__ == '__main__':
    # Part 1: 190
    # Part 2: 2335049
    lines = parse(get_input(day=21, year=2017))
    print("Part 1: {}".format(part1(lines)))
    print("Part 2: {}".format(part2(lines)))
