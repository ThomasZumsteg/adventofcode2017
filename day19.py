#!/usr/bin/env python3

from get_input import get_input, line_parser

def walker(lines):
    pos = (0, lines[0].index('|'))
    drx = (1, 0)
    next_drx = (((1,0),(-1,0)), ((0,1),(0,-1)))
    while 0 <= pos[0] < len(lines) and 0 <= pos[1] < len(lines[pos[0]]):
        char = lines[pos[0]][pos[1]]
        yield char
        if char == '+':
            for new_drx in next_drx[abs(drx[0])]:
                test_char = lines[pos[0] + new_drx[0]][pos[1] + new_drx[1]]
                if test_char != ' ':
                    drx = new_drx
                    break
            else:
                break
        pos = tuple(p + d for p, d in zip(pos, drx))

def part1(lines):
    path = ''
    for char in walker(lines):
        if char not in "+-|":
            path += char
    return path

def part2(lines):
    for steps, char in enumerate(walker(lines), 1):
        if char == 'O':
            return steps

if __name__ == '__main__':
    lines = get_input(day=19, year=2017).splitlines()
    print('Part 1: {}'.format(part1(lines)))
    print('Part 2: {}'.format(part2(lines)))
