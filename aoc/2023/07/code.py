import os
import sys
from functools import cmp_to_key
APP_DIR = os.path.abspath(__file__).split("adventofcode")[0]+"adventofcode"
sys.path.append(APP_DIR)
from lib.util import Input
path_to_day = os.path.dirname(__file__)
puzzleinput = Input(f'{path_to_day}/input.txt')

samples = {
"""32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""":6440
}
sample2s = {
"""32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""":5905
}

def process(pz):
    return pz.lines()
pzz = process(puzzleinput)

def get_rank(card):
    return "23456789TJQKA".index(card)

def get_type(hand):
    h = {}
    for card in hand:
        h[card] = h.get(card, 0) + 1

    if len(h) == 1:
        return 7
    if len(h) == 2 and 4 in h.values():
        return 6
    if len(h) == 2 and 3 in h.values() and 2 in h.values():
        return 5
    if len(h) == 3 and 3 in h.values():
        return 4
    if len(h) == 3:
        return 3
    if len(h) == 4:
        return 2
    return 1

def sort_key(hand1, hand2):
    t1 = get_type(hand1)
    t2 = get_type(hand2)
    if t1 != t2:
        return t1 - t2
    for i in range(5):
        r1 = get_rank(hand1[i])
        r2 = get_rank(hand2[i])
        if r1 != r2:
            return r1 - r2

def problem1(pz):
    hands = {}
    for bid in pz:
        hand, bid = bid.split()
        bid = int(bid)
        hands[hand] = bid
    store = {}
    for i, h in enumerate(sorted(hands, key=cmp_to_key(sort_key)), 1):
        store[h] = i * hands[h]
    return sum(store.values())

def get_rank2(card):
    return "J23456789TQKA".index(card)

def get_type2(hand):
    h = {}
    for card in hand:
        h[card] = h.get(card, 0) + 1
    wilds = h.get("J")
    if wilds:
        if len(h) == 1:
            return 7
        if len(h) == 2 and 4 in h.values():
            return 7
        if len(h) == 2 and 3 in h.values() and 2 in h.values():
            return 7
        if len(h) == 3 and 3 in h.values():
            return 6
        if len(h) == 3 and wilds == 2:
            return 6
        if len(h) == 3 and wilds == 1:
            return 5
        if len(h) == 4 and wilds == 2:
            return 4
        if len(h) == 4 and wilds == 1:
            return 4
        if len(h) == 5:
            return 2


    if len(h) == 1:
        return 7
    if len(h) == 2 and 4 in h.values():
        return 6
    if len(h) == 2 and 3 in h.values() and 2 in h.values():
        return 5
    if len(h) == 3 and 3 in h.values():
        return 4
    if len(h) == 3 and 2 in h.values() and 1 in h.values():
        return 3
    if len(h) == 4:
        return 2
    return 1

def sort_key2(hand1, hand2):
    t1 = get_type2(hand1)
    t2 = get_type2(hand2)
    if t1 != t2:
        return t1 - t2
    for i in range(5):
        r1 = get_rank2(hand1[i])
        r2 = get_rank2(hand2[i])
        if r1 != r2:
            return r1 - r2

def problem2(pz):
    hands = {}
    for bid in pz:
        hand, bid = bid.split()
        bid = int(bid)
        hands[hand] = bid
    store = {}
    for i, h in enumerate(sorted(hands, key=cmp_to_key(sort_key2)), 1):
        store[h] = i * hands[h]
    return sum(store.values())

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
