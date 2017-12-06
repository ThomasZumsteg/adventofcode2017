#!/usr/bin/env python3

from get_input import get_input, line_parser

def spiral_coords():
    # 0
    # 1,2, 1,2, 1,2, 1,2
    # 3,2,3,4, 3,2,3,4, 3,2,3,4, 3,2,3,4
    # 5,4,3,4,5,6
    yield((0,0))
    x, y = 0, 0
    ring = 1
    while True:
        while y < ring:
            y += 1
            yield x, y
        while -ring < x:
            x -= 1
            yield x, y
        while -ring < y:
            y -= 1
            yield x, y
        while x < ring:
            x += 1
            yield x, y
        ring += 1

def part1(num):
    for i, (x, y) in enumerate(spiral_coords(), 1):
        if i == num:
            return abs(x) + abs(y)

def part2(num):
    known_coords = {(0,0): 1}
    for i, (x, y) in enumerate(spiral_coords(), 1):
        this = sum(known_coords.get((i,j),0) for i, j in
                   [(x-1,y+1),(x,y+1),(x+1,y+1),
                    (x-1,  y)        ,(x+1,  y),
                    (x-1,y-1),(x,y-1),(x+1,y-1)])
        if (x,y) not in known_coords:
            known_coords[(x,y)] = this
        if this > num:
            return this

if __name__ == "__main__":
    num = 325489
    print("Part 1: {}".format(part1(num)))
    print("Part 2: {}".format(part2(num)))
