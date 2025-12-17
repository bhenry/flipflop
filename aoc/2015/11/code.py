import os
import sys
APP_DIR = os.path.abspath(__file__).split("adventofcode")[0]+"adventofcode"
sys.path.append(APP_DIR)
from lib.util import Input
path_to_day = os.path.dirname(__file__)
puzzleinput = "vzbxkghb"

samples = {
"abcdefgh":"abcdffaa",
"ghijklmn":"ghjaabcc",
}
sample2s = {

}

def two_pairs(password):
    pairs = []
    i = 0
    while i < len(password)-1:
        if password[i] == password[i+1]:
            pairs.append(password[i])
            i += 2
        else:
            i += 1
    return len(set(pairs)) >= 2

def valid(password):
    return (
        len(password) == 8 and
        not any([c in password for c in "iol"]) and
        any([password[i]+password[i+1]+password[i+2] in "abcdefghijklmnopqrstuvwxyz" for i in range(len(password)-2)]) and
        two_pairs(password)
    )

def increment(password):
    if password and password[-1] == "z":
        return increment(password[:-1]) + "a"
    else:
        return password[:-1] + chr(ord(password[-1])+1)

def problem1(pz):
    password = pz
    i = 0
    while not valid(password):
        i += 1
        password = increment(password)
    return password

def problem2(pz):
    password = problem1(pz)
    password = increment(password)
    return problem1(password)

# debug
if sample2s:
    for sample in sample2s:
        sample_result = problem2(Input(sample).input)
        print("sample2", sample_result)
        if sample_result == sample2s[sample]:
            print("sample2 test pass")

if answer2 := problem2(puzzleinput):
    print("\nproblem2", answer2, "\n\n")

# debug
if samples:
    for sample in samples:
        sample_result = problem1(Input(sample).input)
        print("sample1", sample_result)
        if sample_result == samples[sample]:
            print("sample1 test pass")

if answer1 := problem1(puzzleinput):
    print("\nproblem1", answer1, "\n\n")


print("\ndone")
