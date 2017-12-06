#!/usr/bin/env python3

import os
import requests

SESSION_KEY = "AOC_SESSION"
AOE_URL = "http://adventofcode.com"

def get_input(day, year):
    r = requests.get("{}/{}/day/{}/input".format(AOE_URL, year, day),
                     cookies=dict(session=os.environ.get(SESSION_KEY)))
    if not r.ok:
        raise RuntimeError("Could not get the input: {}: {}".format(
            r.status_code, r.reason))
    return r.text

def line_parser(text, parse=int, seperator='\n'):
    return [parse(item) for item in text.split(seperator) if item != '']
