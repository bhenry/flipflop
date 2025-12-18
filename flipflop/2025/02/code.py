import os
import sys
from functools import cache
APP_DIR = os.path.abspath(__file__).split("flipflop")[0]
sys.path.append(APP_DIR)
from lib.util import nums, rawfile
path_to_day = os.path.dirname(__file__)
raw = rawfile(f'{path_to_day}/input.txt')

# lines = raw.split("\n")
line = raw.strip()
# line = "^^^v^^^^vvvvvvv"
# lines = sample.strip().split("\n")

position = 0
highest = 0
for c in line:
    if c == "^":
        position += 1
    elif c == "v":
        position -= 1
    if position > highest:
        highest = position
print(highest)

position = 0
highest = 0
curr = 0
lastc = ""
for c in line:
    if c == "^":
        curr = curr + 1 if lastc == "^" else 1
    elif c == "v":
        curr = curr - 1 if lastc == "v" else -1
    position += curr
    if position > highest:
        highest = position
    lastc = c
print(highest)

@cache
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

position = 0
highest = 0
curr = 1
lastc = line[0]
for c in line[1:]:
    if c != lastc:
        if lastc == "^":
            position += fib(curr)
        else:
            position -= fib(curr)
        curr = 1
    else:
        curr += 1
    if position > highest:
        highest = position
    lastc = c
print(highest)
