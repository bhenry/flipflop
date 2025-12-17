import re

def nums(s):
    return [int(x) for x in re.findall(r'-?\d+', s)]

class Grid():
    def __init__(self, w=None, h=None, default=None):
        self.w = w
        self.h = h
        self.default = default
        self.grid = {}
        if w and h:
            for x in range(w):
                for y in range(h):
                    self.grid[(x,y)] = default

    def point(self, x, y):
        return self.grid.get((x,y), self.default)

    def get(self, x=None, y=None):
        if x == None and y == None:
            return self.grid
        if x == None:
            return [self.point(x,y) for x in range(self.w)]
        if y == None:
            return [self.point(x,y) for y in range(self.h)]
        return self.point(x,y)

    def set(self, x, y, val):
        self.grid[(x,y)] = val

    def neighbors(self, x, y):
        neighbors = []
        for y2 in range(y-1, y+2):
            for x2 in range(x-1, x+2):
                if x2 == x and y2 == y: continue
                neighbors.append(self.get(x2, y2))
        return neighbors

    def neighborsmap(self, x, y, diag=True):
        neighbors = {}
        for y2 in range(y-1, y+2):
            for x2 in range(x-1, x+2):
                if x2 == x and y2 == y: continue
                if not diag and x2 != x and y2 != y: continue
                neighbors[(x2, y2)] = self.get(x2, y2)
        return neighbors

    def neighborslocs(self, x, y, diag=True):
        neighbors = []
        for y2 in range(y-1, y+2):
            for x2 in range(x-1, x+2):
                if x2 == x and y2 == y: continue
                if not diag and x2 != x and y2 != y: continue
                neighbors.append((x2, y2))
        return neighbors


class Input():
    def __init__(self, filename):
        if not filename.endswith('input.txt'):
            self.filename = None
            self.input = filename
        else:
            self.filename = filename
            with open(filename) as f: self.input = f.read().strip()

    def grid(self, default=None):
        lines = self.input.splitlines()
        grid = Grid(len(lines[0]), len(lines), default)
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                grid.set(x, y, char)
        return grid

    def lines(self):
        return self.input.splitlines()

    def ints(self):
        return [int(i) for i in self.input.splitlines()]

    def ints_by_line(self):
        return [[int(i) for i in re.findall(r'-?\d+', line)] for line in self.input.splitlines()]

def rawfile(path):
    with open(path) as f:
        return f.read().strip()
