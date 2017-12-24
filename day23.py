#!/usr/bin/env python3

from get_input import get_input, line_parser

class ProgRunner(object):
    def __init__(self, prog, reg=None):
        self._prog = prog
        # Do somethigh with auto lookup in a regestry to replace getters and setters
        self.reg = reg or {}
        self.i = 0

    def __repr__(self):
        if not self.done():
            return "{}: {}".format(self.i, ' '.join(self._prog[self.i]))

    @property
    def func(self):
        if not self.done():
            return self._prog[self.i][0]

    def __iter__(self):
        while not self.done():
            yield next(self) 

    def done(self):
        return not (0 <= self.i < len(self._prog))

    def __next__(self):
        if self.done():
            raise StopIteration

        if self.func == 'set':
            self.arg_1 = self.arg_2
        elif self.func == 'sub':
            self.arg_1 -= self.arg_2
        elif self.func == 'mul':
            self.arg_1 *= self.arg_2
        elif self.func == 'jnz':
            if self.arg_1 != 0:
                self.i += self.arg_2 - 1
        self.i += 1
        return self

    def __getattr__(self, prop):
        if prop[:3] == 'arg' and not self.done():
            num = int(prop.split('_')[1])
            val = self._prog[self.i][num]
            if val in self.reg:
                self.reg[val]
            else:
                (val)

class Register(object):
    pass

def part1(program):
    reg = {v: 0 for v in "abcdefgh"}
    state = ProgRunner(program, reg=reg)
    return sum(1 for s in state if s.func == 'mul')

def part2(program):
    # No general purpose algo for figuring this one out
    reg = {v: 0 if v != 'a' else 1 for v in "abcdefgh"}
    state = ProgRunner(program, reg=reg)
    for s in state:
        if s.i == 10:
            if s.reg['b'] % s.reg['d'] == 0:
                s.i = 25
                # print("{:4} % {:4} == 0, {} skip to {}".format(
                    # s.reg['b'], s.reg['d'], s.reg['h'], s))
            else:
                s.i = 20
    return s.reg['h']

def is_prime(n):
     if n % 2 == 0:
         return False
     for m in range(3, int((n+1)**0.5), 2):
         if n % m == 0:
             return False
     return True

if __name__ == '__main__':
    lines = line_parser(get_input(day=23, year=2017), 
            parse=lambda line: line.split(' '))
    # Part 1: 3025
    # Part 2: 915
    print("Part 1: {}".format(part1(lines)))
    print("Part 2: {}".format(part2(lines)))
