import os, re
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: puzzleinput = f.read()

samples = {

}
sample2s = {

}

def process(input):
    return [i.strip() for i in input.splitlines()]

def p1(pz):
    data = process(pz)
    lights = {}
    for s in data:
        x1, y1, x2, y2 = re.findall(r'\d+', s)
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if "turn on" in s:
                    lights[(x, y)] = 1
                elif "turn off" in s:
                    lights[(x, y)] = 0
                elif "toggle" in s:
                    if (x, y) in lights:
                        lights[(x, y)] = (lights[(x, y)] + 1) % 2
                    else:
                        lights[(x, y)] = 1
    return sum(lights.values())

def p2(pz):
    data = process(pz)
    lights = {}
    for s in data:
        x1, y1, x2, y2 = re.findall(r'\d+', s)
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if "turn on" in s:
                    lights[(x, y)] = lights.get((x, y), 0) + 1
                elif "turn off" in s:
                    lights[(x, y)] = max(0, lights.get((x, y), 0) - 1)
                elif "toggle" in s:
                    lights[(x, y)] = lights.get((x, y), 0) + 2
    return sum(lights.values())

if answer2 := p2(puzzleinput):
    print("\nproblem2", answer2, "\n\n")

    # debug
    if sample2s:
        for sample in sample2s:
            sample_result = p2(sample)
            print("sample2", sample_result)
            if sample_result == sample2s[sample]:
                print("sample2 test pass")

if answer1 := p1(puzzleinput):
    print("\nproblem1", answer1, "\n\n")

    # debug
    if samples:
        for sample in samples:
            sample_result = p1(sample)
            print("sample1", sample_result)
            if sample_result == samples[sample]:
                print("sample1 test pass")

print("\ndone")
