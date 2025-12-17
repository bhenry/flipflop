import os
import re
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5"""

sample_answer1 = 6032
sample_answer2 = 5031

FACINGS = [">", "v", "<", "^"]

def move(grid):
    if grid["facing"] == ">":
        newloc = (grid["loc"][0]+1, grid["loc"][1])
        if newloc[0] > grid[newloc[1]]["right"]:
            newloc = (grid[newloc[1]]["left"], newloc[1])
    elif grid["facing"] == "<":
        newloc = (grid["loc"][0]-1, grid["loc"][1])
        if newloc[0] < grid[newloc[1]]["left"]:
            newloc = (grid[newloc[1]]["right"], newloc[1])
    elif grid["facing"] == "v":
        newloc = (grid["loc"][0], grid["loc"][1]+1)
        if newloc not in grid:
            while True:
                #move up until you fall off the grid
                newloc = (newloc[0], newloc[1]-1)
                if newloc not in grid:
                    #go back down one
                    newloc = (newloc[0], newloc[1]+1)
                    break
    elif grid["facing"] == "^":
        newloc = (grid["loc"][0], grid["loc"][1]-1)
        if newloc not in grid:
            while True:
                #move down until you fall off the grid
                newloc = (newloc[0], newloc[1]+1)
                if newloc not in grid:
                    #go back up one
                    newloc = (newloc[0], newloc[1]-1)
                    break
    if grid.get(newloc) == ".":
        grid["loc"] = newloc

def process(input):
    input = input.split("\n\n")
    grid = {}
    grid["facing"] = ">"
    grid["height"] = len(input[0].splitlines())
    for y, line in enumerate(input[0].splitlines()):
        grid[y] = {
            "width": len(line.strip()),
            "right": line.rindex(line.strip()[-1]),
            "left": line.index(line.strip()[0]),
        }
        if y == 0:
            grid["loc"] = (grid[y]["left"], y)
            grid[grid["loc"]] = grid["facing"]
        for x, char in enumerate(line):
            if char != " ":
                grid[(x, y)] = char
    code = [i for i in re.split(r'([\D+])',input[1]) if i.strip()]
    return grid, code

def p1(input):
    grid, code = process(input)

    for c in code:
        if c == "L":
            grid["facing"] = FACINGS[(FACINGS.index(grid["facing"])-1)%4]
        elif c == "R":
            grid["facing"] = FACINGS[(FACINGS.index(grid["facing"])+1)%4]
        else:
            for _ in range(int(c)):
                move(grid)
    return (grid["loc"][0]+1) * 4 + (grid["loc"][1]+1) * 1000 + FACINGS.index(grid["facing"])

# print(process(sample_input))

def move2(grid):
    if grid["facing"] == ">":
        newloc = (grid["loc"][0]+1, grid["loc"][1])
        newfacing = grid["facing"]
        if newloc[0] > grid[newloc[1]]["right"]:
            # code the 4 ways to fall off the right (wrapping around the cube)
            if 0 <= newloc[1] < 50:
                newloc = (99, 149 - newloc[1])
                newfacing = "<"
            elif 50 <= newloc[1] < 100:
                newloc = (newloc[1] + 50, 49)
                newfacing = "^"
            elif 100 <= newloc[1] < 150:
                newloc = (149, 149 - newloc[1])
                newfacing = "<"
            elif 150 <= newloc[1] < 200:
                newloc = (newloc[1] - 100, 149)
                newfacing = "^"
    elif grid["facing"] == "<":
        newloc = (grid["loc"][0]-1, grid["loc"][1])
        newfacing = grid["facing"]
        if newloc[0] < grid[newloc[1]]["left"]:
            if 0 <= newloc[1] < 50:
                newloc = (0, 149 - newloc[1])
                newfacing = ">"
            elif 50 <= newloc[1] < 100:
                newloc = (newloc[1] - 50, 100)
                newfacing = "v"
            elif 100 <= newloc[1] < 150:
                newloc = (50, 149 - newloc[1])
                newfacing = ">"
            elif 150 <= newloc[1] < 200:
                newloc = (newloc[1] - 100, 0)
                newfacing = "v"
    elif grid["facing"] == "v":
        newloc = (grid["loc"][0], grid["loc"][1]+1)
        newfacing = grid["facing"]
        if newloc not in grid:
            # code the 3 ways to fall off the bottom (wrapping around the cube)
            if 0 <= newloc[0] < 50:
                newloc = (newloc[0] + 100, 0)
                newfacing = "v"
            elif 50 <= newloc[0] < 100:
                newloc = (49, newloc[1] + 100)
                newfacing = "<"
            elif 100 <= newloc[0] < 150:
                newloc = (99, newloc[0] - 50)
                newfacing = "<"
    elif grid["facing"] == "^":
        newloc = (grid["loc"][0], grid["loc"][1]-1)
        newfacing = grid["facing"]
        if newloc not in grid:
            if 0 <= newloc[0] < 50:
                newloc = (50, newloc[0] + 50)
                newfacing = ">"
            elif 50 <= newloc[0] < 100:
                newloc = (0, newloc[0] + 100)
                newfacing = ">"
            elif 100 <= newloc[0] < 150:
                newloc = (newloc[0] - 100, 199)
                newfacing = "^"
    if grid.get(newloc) == ".":
        grid["loc"] = newloc
        grid["facing"] = newfacing


def p2(input):
    grid, code = process(input)

    for c in code:
        if c == "L":
            grid["facing"] = FACINGS[(FACINGS.index(grid["facing"])-1)%4]
        elif c == "R":
            grid["facing"] = FACINGS[(FACINGS.index(grid["facing"])+1)%4]
        else:
            for _ in range(int(c)):
                move2(grid)
    return (grid["loc"][0]+1) * 4 + (grid["loc"][1]+1) * 1000 + FACINGS.index(grid["facing"])

if sample_answer1:
    sample_result = p1(sample_input)
    print("sample1", sample_result)
    if sample_result == sample_answer1:
        print("sample1 test pass")
        print("\nproblem1", p1(input), "\n\n")

# if sample_answer2:
#     sample_result = p2(sample_input)
#     print("sample2", sample_result)
#     if sample_result == sample_answer2:
#         print("sample2 test pass")
print("\nproblem2", p2(input), "\n\n")


print("\ndone")
