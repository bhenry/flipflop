import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
"""

sample_answer1 = 64
sample_answer2 = 58

def process(input):
    return [i.strip() for i in input.splitlines()]

# print(process(sample_input))
# adjacent cubes from cube 0,0,0
ADJ = [(0,0,1), (0,0,-1), (0,1,0), (0,-1,0), (1,0,0), (-1,0,0)]

def p1(input):
    data = process(input)
    space = set()
    for i in data:
        x,y,z = [int(j) for j in i.split(",")]
        space.add((x,y,z))
    surf = 0
    for x,y,z in space:
        adj = 0
        for dx,dy,dz in ADJ:
            if (x+dx,y+dy,z+dz) in space:
                adj += 1
        surf += 6-adj
    # cube is touching if it has any side touching another side
    # cube at 2,2,2 is touching cube at 2,3,2 on one side
    return surf

# def p2(input):
#     data = process(input)
#     space = set()
#     highz,lowz,highy,lowy,highx,lowx = 0,0,0,0,0,0
#     for i in data:
#         x,y,z = [int(j) for j in i.split(",")]
#         highz = max(highz,z)
#         lowz = min(lowz,z)
#         highy = max(highy,y)
#         lowy = min(lowy,y)
#         highx = max(highx,x)
#         lowx = min(lowx,x)
#         space.add((x,y,z))
#     surf = 0
#     for x,y,z in space:
#         adj = 0
#         for x in range(lowx-1,x):
#             if (x,y,z) in space:
#                 adj += 1
#                 break
#         for x in range(x,highx+1):
#             if (x,y,z) in space:
#                 adj += 1
#                 break
#         for y in range(lowy-1,y):
#             if (x,y,z) in space:
#                 adj += 1
#                 break
#         for y in range(y,highy+1):
#             if (x,y,z) in space:
#                 adj += 1
#                 break
#         for z in range(lowz-1,z):
#             if (x,y,z) in space:
#                 adj += 1
#                 break
#         for z in range(z,highz+1):
#             if (x,y,z) in space:
#                 adj += 1
#                 break
#         surf += 6-adj
#     return surf
    # if (x,y,z) in DEADEND:
    #     return False
    # if (x,y,z) in STORE:
    #     return STORE[(x,y,z)]
    # highx,lowx,highy,lowy,highz,lowz = bounds
    # if x < lowx or x > highx or y < lowy or y > highy or z < lowz or z > highz:
    #     STORE[(x,y,z)] = True
    #     return True
    # for dx,dy,dz in ADJ:
    #     if (x+dx,y+dy,z+dz) in space:
    #         DEADEND.add((x+dx,y+dy,z+dz))
    #     else:
    #         if reachable(x+dx,y+dy,z+dz,space,bounds):
    #             STORE.add((x,y,z))
    #             return True
    # STORE[(x,y,z)] = False
    # return False


STORE = {}
def reachable(x,y,z,space,bounds,seen):
    if (x,y,z) in STORE:
        return STORE[(x,y,z)]
    highx,lowx,highy,lowy,highz,lowz = bounds
    if x < lowx or x > highx or y < lowy or y > highy or z < lowz or z > highz:
        STORE[(x,y,z)] = True
        return True
    if (x,y,z) in space:
        STORE[(x,y,z)] = False
        return False
    if all((dx,dy,dz) in space for dx,dy,dz in ADJ):
        STORE[(x,y,z)] = False
        return False
    if any(reachable(x+dx,y+dy,z+dz,space,bounds,seen | {(x,y,z)}) for dx,dy,dz in ADJ if (x+dx,y+dy,z+dz) not in seen):
        STORE[(x,y,z)] = True
        return True
    STORE[(x,y,z)] = False
    return False



def countreachablesides(space, bounds):
    c = 0
    seen = set()
    for x,y,z in space:
        for dx,dy,dz in ADJ:
            if reachable(x+dx,y+dy,z+dz,space,bounds,seen):
                c += 1
    return c

def p2(input):
    STORE.clear()
    data = process(input)
    space = set()
    highz,lowz,highy,lowy,highx,lowx = 0,1000,0,1000,0,1000
    for i in data:
        x,y,z = [int(j) for j in i.split(",")]
        highz = max(highz,z)
        lowz = min(lowz,z)
        highy = max(highy,y)
        lowy = min(lowy,y)
        highx = max(highx,x)
        lowx = min(lowx,x)
        space.add((x,y,z))
    bounds = (highx,lowx,highy,lowy,highz,lowz)
    surf = countreachablesides(space, bounds)
    return surf


# if sample_answer1:
#     sample_result = p1(sample_input)
#     print("sample1", sample_result)
#     if sample_result == sample_answer1:
#         print("sample1 test pass")
#         print("\nproblem1", p1(input), "\n\n")

if sample_answer2:
    sample_result = p2(sample_input)
    print("sample2", sample_result)
    if sample_result == sample_answer2:
        print("sample2 test pass")
        # print("\nproblem2", p2(input), "\n\n")
    else:
        print(f"sample2 test should be {sample_answer2}")


print("\ndone")
