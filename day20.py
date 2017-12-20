#!/usr/bin/env python3

from get_input import get_input, line_parser
import re
from collections import defaultdict

class Partical(object):
    digit_group = r'-?\d+,-?\d+,-?\d+'
    line_parse = re.compile(r'p=<({0})>,v=<({0})>,a=<({0})>'.format(digit_group))
    
    def __init__(self, line):
        r_match = type(self).line_parse.match(line.replace(' ', ''))
        if not r_match:
            raise ValueError('Not a valid line {}'.format(line))
        self._position = tuple(int(n) for n in r_match.group(1).split(','))
        self._velocity = tuple(int(n) for n in r_match.group(2).split(','))
        self._acceleration = tuple(int(n) for n in r_match.group(3).split(','))

    @property
    def scalar(self):
        return tuple(sum(abs(v) for v in values) for values in 
                (self._acceleration, self._velocity, self._position))

    def position(self, t):
        # v1 = a0 + v0
        # p1 = p0 + (a0 + v0)

        # v2 = a0 + v1 = a0 + (a0 + v0)
        # p2 = p1 + v2 = (p0 + a0 + v0) + (a0 + a0 + v0) = 3 * a0 + 2 * v0 + p0

        # v3 = a0 + v2 = a0 + (a0 + a0 + v0)
        # p3 = p2 + v3 = (3 * a0 + 2 * v0 + p0) + (3 * a0 + v0) = 6 * a0 + 3 * v0 + p0

        # vn = n * a0 + v0
        # pn = (n * (n + 1) / 2) a0 + n * v0 + p0
        return tuple(int(a*t*(t+1)/2 + t * v + p) for a, v, p in zip(
            self._acceleration, self._velocity, self._position))

    def collides(self, other):
        # a_x0 * t^2 / 2 + v_x0 * t + p_x0 == a_x1 * t^2 / 2 + v_x1 * t + p_x1
        # a_y0 * t^2 / 2 + v_y0 * t + p_y0 == a_y1 * t^2 / 2 + v_x1 * t + p_x1
        # a_z0 * t^2 / 2 + v_z0 * t + p_z0 == a_z1 * t^2 / 2 + v_z1 * t + p_z1
        #
        # (a_x0 - a_x1) * t^2 / 2 + (v_x0 - vx1) * t + (p_x0 - p_x1) == 0
        # (a_y0 - a_y1) * t^2 / 2 + (v_y0 - vy1) * t + (p_y0 - p_y1) == 0
        # (a_z0 - a_z1) * t^2 / 2 + (v_z0 - vz1) * t + (p_z0 - p_z1) == 0
        #
        # (-Δv_x ± √(Δv_x^2 - 2*Δa_x*Δp_x) / Δa_x 
        # (-Δv_y ± √(Δv_y^2 - 2*Δa_y*Δp_y) / Δa_y
        # (-Δv_z ± √(Δv_z^2 - 2*Δa_z*Δp_z) / Δa_z
        #
        # or if Δa is zero
        # -Δp/Δv
        diff = [[None for _ in range(3)] for _ in range(3)]
        for p, prop in enumerate(('_acceleration', '_velocity', '_position')):
            for d in range(3):
                diff[d][p] = getattr(self, prop)[d] - getattr(other, prop)[d]
        if all(vec[2] == 0 for vec in diff):
            return 0

    def __repr__(self):
        return 'p=<{}>, v=<{}>, a=<{}>'.format(
                self._position, self._velocity, self._acceleration)

def test_particles():
    particles = [Partical(line) for line in (
        'p=<-6,0,0>,v=<3,0,0>,a=<0,0,0>',
        'p=<-4,0,0>,v=<2,0,0>,a=<0,0,0>',
        'p=<-2,0,0>,v=<1,0,0>,a=<0,0,0>',
        'p=< 3,0,0>,v=<-1,0,0>,a=<0,0,0>')]
    assert particles[0].collides(particles[0]) == 0
    assert particles[0].collides(particles[1]) == 2
    assert particles[0].collides(particles[3]) == None

def part1(particles):
    smallest, n = particles[0], 0
    for i, p in enumerate(particles[1:], 1):
        if p.scalar < smallest.scalar:
            smallest, n = p, i
    return n

def part2(particles, iters=100):
    for t in range(100):
        collitions = defaultdict(list)
        for p in particles:
            collitions[p.position(t)].append(p)
        particles = [vals[0] for vals in collitions.values() if len(vals) == 1]
    return len(particles)

if __name__ == '__main__':
    lines = line_parser(get_input(day=20, year=2017), parse=Partical)
    print('Part 1: {}'.format(part1(lines)))
    print('Part 2: {}'.format(part2(lines)))
