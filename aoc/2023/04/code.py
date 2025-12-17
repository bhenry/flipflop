import os
import sys
APP_DIR = os.path.abspath(__file__).split("adventofcode")[0]+"adventofcode"
sys.path.append(APP_DIR)
from lib.util import Input
path_to_day = os.path.dirname(__file__)
puzzleinput = Input(f'{path_to_day}/input.txt')

samples = {
"""Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""":13
}
sample2s = {
"""Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""":30
}

def process(pz):
    return pz.lines()
pzz = process(puzzleinput)

def problem1(pz):
    total = 0
    for line in pz:
        card, draw = line.split("|")
        game, card = card.split(":")
        card = card.strip()
        draw = draw.strip()
        subtotal = -1
        for c in card.split(" "):
            if c and c in draw.split(" "):
                subtotal += 1
        if subtotal >= 0:
            total += 2**subtotal
    return total

def tally(cache):
    cards = {k: 1 for k in cache}
    for game in cache:
        for k in range(game+1, game+1+cache[game]):
            cards[k] += cards[game]
    return sum(cards.values())

def problem2(pz):
    cache = {}
    for line in pz:
        card, draw = line.split("|")
        game, card = card.split(":")
        game = int(game.strip().split(" ")[-1])
        card = card.strip()
        draw = draw.strip()
        wins = 0
        for c in card.split(" "):
            if c and c in draw.split(" "):
                wins += 1
        cache[game] = wins
    return tally(cache)

# debug
if sample2s:
    for sample in sample2s:
        sample_result = problem2(process(Input(sample)))
        print("sample2", sample_result)
        if sample_result == sample2s[sample]:
            print("sample2 test pass")

if answer2 := problem2(pzz):
    print("\nproblem2", answer2, "\n\n")

# debug
if samples:
    for sample in samples:
        sample_result = problem1(process(Input(sample)))
        print("sample1", sample_result)
        if sample_result == samples[sample]:
            print("sample1 test pass")

if answer1 := problem1(pzz):
    print("\nproblem1", answer1, "\n\n")


print("\ndone")
