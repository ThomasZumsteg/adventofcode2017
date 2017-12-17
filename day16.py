#!/usr/bin/env python3

from get_input import get_input

def spin(programs, spaces, _):
    return programs[-spaces:] + programs[:-spaces]

def exchage(programs, a, b):
    progs = programs[:]
    progs[a], progs[b] = progs[b], progs[a]
    return progs
    
def parter(programs, n, m):
    a = programs.index(n)
    b = programs.index(m)
    return exchage(programs, a, b)

def dance(programs, moves):
    for func, a, b in moves:
        programs = func(programs, a, b)
    return programs

def part1(moves):
    return ''.join(dance(list('abcdefghijklmnop'), moves))

def part2(moves, iters=1000000000):
    programs = list("abcdefghijklmnop")
    states = {}
    dates = {}
    for i in range(iters):
        state = ''.join(programs)
        if state in states:
            match = states[state]
            return dates[(iters - match) % (i - match)]
        states[ state ] = i
        dates[i] = state
        programs = dance(programs, moves)

def test_dance():
    moves = parser('s1,x3/4,pe/b')
    start = list("abcde") 
    end = dance(start, moves)
    assert end == list('baedc')
    end_2 = dance(list(end), moves)
    assert end_2 == list("ceadb")

def parser(line):
    moves = []
    for move in line.split(','):
        if move[0] == 'x':
            a, b = move[1:].split('/')
            moves.append((exchage, int(a), int(b) ))
        elif move[0] == 'p':
            a, b = move[1:].split('/')
            moves.append((parter, a, b))
        elif move[0] == 's':
            a, b = move[1:], 0
            moves.append((spin, int(a), int(b)))
    return moves

if __name__ == '__main__':
    line = parser(get_input(day=16, year=2017))
    print("Part 1: {}".format(part1(line)))
    print("Part 2: {}".format(part2(line)))
