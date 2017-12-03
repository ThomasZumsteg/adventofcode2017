#!/usr/bin/env python3

import os
import requests

SESSION_KEY = "AOC_SESSION"
AOE_URL = "http://adventofcode.com"

def get_intput(day, year):
    r = requests.get("{}/{}/day/{}/input".format(AOE_URL, year, day),
                     cookies=dict(session=os.environ.get(SESSION_KEY)))
    if not r.ok:
        raise RuntimeError("Could not get the input: {}: {}".format(
            r.status_code, r.reason))
    return r.text

def line_parser(text, parse=int):
    result = []
    for line in text.splitlines():
        result.append([])
        for num in line.split():
            result[-1].append(parse(num))
    return result
