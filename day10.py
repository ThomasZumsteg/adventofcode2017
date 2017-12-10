#!/usr/bin/env python3

from get_input import get_input, line_parser

def knot_hash(hash_vals, hash_size=256, iterations=64):
    hash_list = list(range(hash_size))
    shift_distance = 0
    for skip_size, val in enumerate(hash_vals * iterations):
        hash_list = list(reversed(hash_list[:val])) + hash_list[val:]
        shift_size = (skip_size + val) % hash_size
        shift_distance += shift_size
        hash_list = hash_list[shift_size:] + hash_list[:shift_size]
    shift_distance = hash_size - (shift_distance % hash_size)
    return hash_list[shift_distance:] + hash_list[:shift_distance]

def dense_hash(values, block_size=16):
    hash_str = ''
    for block_start in range(0, len(values), block_size):
        h = 0
        for char in values[block_start:block_start+block_size]:
            h ^= char
        hash_str += format(h, '02x')
    return hash_str

def part1(lengths, n_items=256):
    items = knot_hash(lengths, hash_size=n_items, iterations=1)
    return items[0] * items[1]

def test_part1():
    assert part1([227,169,3,166,246,201,0,47,1,255,2,254,96,3,97,144]) == 13760

def part2(chars, hash_size=256, iterations=64, block_size=16):
    hash_vals = knot_hash([ord(c) for c in chars] + [17, 31, 73, 47, 23])
    return dense_hash(hash_vals)

def test_part2():
    assert 'a2582a3a0e66e6e86e3812dcb672a272' == part2('')
    assert '33efeb34ea91902bb2f59c9920caa6cd' == part2('AoC 2017')

if __name__ == '__main__':
    line = get_input(day=10, year=2017).strip()
    print("Part 1: {}".format(part1(line_parser(line, seperator=','))))
    print("Part 2: {}".format(part2(line)))
