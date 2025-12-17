import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""

sample_answer1 = 26
sample_answer2 = 61229

def process(input):
    return [i.strip() for i in input.splitlines()]

def p1(input):
    data = process(input)
    countup = 0
    for line in data:
        samples, matters = [a.split() for a in line.split(" | ")]
        for m in matters:
            if len(m) in [2,3,4,7]:
                countup += 1
    return countup

segs2num = {2: 1, 7: 8, 4: 4, 3: 7}
def p2(input):
    data = process(input)
    countup = 0
    for line in data:
        nums = {}
        samples, matters = [a.split() for a in line.split(" | ")]
        sorted_samples = sorted(samples, key=len)
        nums[1] = sorted_samples[0]  # it's a 1
        nums[8] = sorted_samples[-1]  # it's an 8
        for s in sorted_samples[1:-1]:
            if len(s) == 3:
                # it's a 7
                nums[7] = s
            if len(s) == 4:
                # it's a 4
                nums[4] = s
        for s in sorted(set(sorted_samples) - set(nums.values()), key=len, reverse=True):
            if len(s) == 6:
                # it's a 6, 9, or 0
                if set(nums[1]) - set(s):  # a 1 minus a 9 or 0 will have nothing left
                    # it's a 6
                    nums[6] = s
                else:
                    # it's a 9 or 0
                    # (set(nums[7]) - set(nums[1])) is the top segment
                    # the top plus the 4 is the nine minus the bottom segment
                    if len(set(s) - (set(nums[4]) | (set(nums[7]) - set(nums[1])))) == 1:
                        # it's a 9
                        nums[9] = s
                    else:
                        # it's a 0
                        nums[0] = s
            if len(s) == 5:
                # it's a 2, 3, or 5
                if not(set(s) - set(nums[6])):
                    # 5 minus 6 should have nothing left
                    nums[5] = s
                elif len(set(nums[4]) - set(s)) == 1:
                    # 4 minus 3 should have 1 left
                    nums[3] = s
                else:
                    # it's a 2
                    nums[2] = s
        score = ""
        for o in matters:
            for n, s in nums.items():
                if set(s) == set(o):
                    score += str(n)
                    break
        countup += int(score)
    return countup

if sample_answer1:
    sample_result = p1(sample_input)
    print("sample1 test", sample_result == sample_answer1)
    print("sample1", p1(sample_input))
    print("problem1", p1(input), "\n\n")
if sample_answer2:
    sample_result = p2(sample_input)
    print("sample2 test", sample_result == sample_answer2)
    print("sample2", p2(sample_input))
    print("problem2", p2(input))
