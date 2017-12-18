#!/usr/bin/env python3

import logging

def spin(inp, itr=2018):
    pos = inp
    buff = [0]
    for i in range(1, itr):
        buff = buff[:pos] + [i] + buff[pos:]
        logging.debug(buff)
        pos = (inp + pos + 1) % len(buff)
    return buff

def part1(inp):
    buff = spin(inp, itr=2018)
    return buff[buff.index(2017) + 1]

def test_part1():
    assert [0,9,5,7,2,4,3,8,6,1] == spin(3, itr=10)

def spin2(inp, itr=10):
    pos = inp 
    second = 1
    zero_pos = 0
    for i in range(1, itr):
        if pos == zero_pos + 1:
            second = i
        elif pos <= zero_pos:
            zero_pos += 1
        pos = (inp + pos + 1) % (i + 1)
    return second

def test_spin2():
    logging.basicConfig(level=logging.DEBUG)
    for i in range(2, 20):
        for j in range(2, 20):
            buff = spin(i, itr=j)
            assert spin2(i, itr=j) == buff[buff.index(0) + 1]

def part2(inp):
    return spin2(inp, itr=50000000)

def parse(line):
    return line

if __name__ == '__main__':
    inp = 335
    # Part 1: 1282
    # Part 2: 27650600
    # logging.basicConfig(level=logging.WARNING)
    print("Part 1: {}".format(part1(inp)))
    print("Part 2: {}".format(part2(inp)))
