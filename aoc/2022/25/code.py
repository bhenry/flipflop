import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122
"""

sample_answer1 = "2=-1=0"
sample_answer2 = None

def process(input):
    return [i.strip() for i in input.splitlines()]

# print(process(sample_input))
TRANSLATE = {
    "2": 2,
    "1": 1,
    "0": 0,
    "-": -1,
    "=": -2,
}
def todec(s):
    num = 0
    for i, c in enumerate(s[::-1]):
        if c in TRANSLATE:
            num += 5**i * TRANSLATE[c]
    return num

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return "".join(str(d) for d in digits[::-1])

def toelf(num):
    b5 = numberToBase(num, 5)
    b5s = str(b5)
    b5sr = b5s[::-1]
    elf = ""
    carry = 0
    for c in b5sr:
        val = int(c) + carry
        place_digit = val % 5
        carry = val // 5
        if place_digit == 3:
            elf = "=" + elf
            carry += 1
        elif place_digit == 4:
            elf = "-" + elf
            carry += 1
        else:
            elf = str(place_digit) + elf
    if carry:
        elf = str(carry) + elf
    return elf

def p1(input):
    sum = 0
    for line in process(input):
        sum += todec(line)
        print (line, todec(line), sum)
    return toelf(sum) #, sum

def p2(input):
    data = process(input)
    return data

if sample_answer1:
    sample_result = p1(sample_input)
    print("sample1", sample_result)
    if sample_result == sample_answer1:
        print("sample1 test pass")
        print("\nproblem1", p1(input), "\n\n")

if sample_answer2:
    sample_result = p2(sample_input)
    print("sample2", sample_result)
    if sample_result == sample_answer2:
        print("sample2 test pass")
        print("\nproblem2", p2(input), "\n\n")


print("\ndone")
