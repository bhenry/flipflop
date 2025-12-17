import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""

sample_answer1 = 4512
sample_answer2 = 1924

def process(input):
    return [i.strip() for i in input.splitlines()]

class Board:
    def __init__(self, board):
        self.board = board
        self.nums = {}
        for x in range(len(board)):
            for y in range(5):
                self.nums[(x,y)] = [board[x].split()[y], None]

    def calln(self, n):
        for x in range(5):
            for y in range(5):
                if self.nums[(x,y)][0] == n:
                    self.nums[(x,y)][1] = "CALLED"

    def win(self):
        for y in range(5):
            if all([self.nums[(x,y)][1] == "CALLED" for x in range(5)]):
                return True
        for x in range(5):
            if all([self.nums[(x,y)][1] == "CALLED" for y in range(5)]):
                return True
        return False

    def score(self):
        return sum([int(self.nums[(x,y)][0]) for x,y in self.nums if self.nums[(x,y)][1] != "CALLED"])

def p1(input):
    data = process(input)
    called = data[0].split(",")

    boards = [Board(i.strip().split('\n')) for i in input.split("\n\n")[1:]]

    for c in called:
        for b in boards:
            b.calln(c)
            if b.win():
                return b.score()*int(c)


def p2(input):
    data = process(input)
    called = data[0].split(",")

    boards = [Board(i.strip().split('\n')) for i in input.split("\n\n")[1:]]

    winners = set()
    for c in called:
        for b in boards:
            b.calln(c)
            if b.win():
                winners.add(b)
                if len(winners) == len(boards):
                    return b.score()*int(c)


if sample_answer1:
    print("sample test", p1(sample_input) == sample_answer1)
    print("Problem1", p1(input))
if sample_answer2:
    print("sample test2", p2(sample_input) == sample_answer2)
    print("Problem2", p2(input))
