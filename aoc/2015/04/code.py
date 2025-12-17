import hashlib
import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """
"""

def md5(s):
    return hashlib.md5(s.encode()).hexdigest()

sample_answer1 = "abcdef"
sample_answer2 = "pqrstuv"

def process(input):
    return [i.strip() for i in input.splitlines()][0]

# print(process(sample_input))

def p1(input):
    data = process(input)
    i = 0
    while True:
        if md5(data + str(i))[:6] == "000000":
            return i
        i += 1

def p2(input):
    data = process(input)
    return None

if p1(input):
    print("\nsample1", p1(sample_answer1), "\n\n")
    print("\nsample2", p1(sample_answer2), "\n\n")
    print("\nproblem1", p1(input), "\n\n")


if p2(input):
    print("\nproblem2", p2(input), "\n\n")

    # debug
    if sample_answer2:
        sample_result = p2(sample_input)
        print("sample2", sample_result)
        if sample_result == sample_answer2:
            print("sample2 test pass")


print("\ndone")
