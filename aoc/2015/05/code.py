import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: puzzleinput = f.read()

samples = {

}
sample2s = {

}

def process(input):
    return [i.strip() for i in input.splitlines()]

"""
It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
"""


def p1(pz):
    data = process(pz)
    nice = 0
    for s in data:
        vowels = 0
        double = False
        bad = False
        for i in range(len(s)):
            if s[i] in "aeiou":
                vowels += 1
            if i > 0:
                if s[i-1] == s[i]:
                    double = True
                if s[i-1] + s[i] in ["ab", "cd", "pq", "xy"]:
                    bad = True
        if vowels >= 3 and double and not bad:
            nice += 1
    return nice

"""
It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
"""

def p2(pz):
    data = process(pz)
    nice = 0
    for s in data:
        c1 = False
        c2 = False
        for i in range(len(s)):
            if i > 1:
                if s[i-2] + s[i-1] in s[i:]:
                    c2 = True
            if i > 0 and i < len(s) - 1:
                if s[i-1] == s[i+1]:
                    c1 = True
        if c1 and c2:
            nice += 1
    return nice

if answer1 := p1(puzzleinput):
    print("\nproblem1", answer1, "\n\n")

    # debug
    if samples:
        for sample in samples:
            sample_result = p1(sample)
            print("sample1", sample_result)
            if sample_result == samples[sample]:
                print("sample1 test pass")

if answer2 := p2(puzzleinput):
    print("\nproblem2", answer2, "\n\n")

    # debug
    if sample2s:
        for sample in sample2s:
            sample_result = p2(sample)
            print("sample2", sample_result)
            if sample_result == sample2s[sample]:
                print("sample2 test pass")



print("\ndone")
