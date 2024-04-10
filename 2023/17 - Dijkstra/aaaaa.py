from collections import defaultdict
import heapq

GridString = []
with open("input.txt", "r") as data:
    for t in data:
        Line = t.strip()
        GridString.append(Line)

GridDict = defaultdict()
for y, g in enumerate(GridString):
    for x, n in enumerate(g):
        GridDict[(x,y)] = int(n)

Height = len(GridString)
Width = len(GridString[0])

Directions = [(1,0),(0,1),(-1,0),(0,-1)]
Answers = []
for Part in [1,2]:
    ImperialCore = set()
    OuterRim = []
    StartPoint = (0,0)
    heapq.heappush(OuterRim, (0,StartPoint,(0,0)))
    ImperialCore.add(StartPoint)
    Goal = (Width-1,Height-1)
    while OuterRim:
        Distance, Location, PrevTuple = heapq.heappop(OuterRim)
        X, Y = Location
        PrevDirection, PrevLineNum = PrevTuple
        if (X,Y,PrevTuple) in ImperialCore:
            continue
        ImperialCore.add((X,Y,PrevTuple))
        if Location == Goal:
            if Part == 2 and PrevLineNum < 4:
                continue
            Answers.append(Distance)
            print("Found")
            break
        for v, d in enumerate(Directions):
            if Part == 1:
                if PrevTuple == (v, 3) or v == (PrevDirection+2)%4:
                    continue
            if Part == 2:
                if PrevTuple == (v, 10) or v == (PrevDirection+2)%4 or (1<=PrevLineNum<=3 and v != PrevDirection):
                    continue
            DX, DY = d
            GX, GY = X+DX, Y+DY
            if 0 <= GX < Width and 0 <= GY < Height and (GX,GY,v):
                NewPath = GridDict[(GX,GY)]
                NewDistance = Distance + NewPath
                if PrevDirection == v:
                    NewDirectionTuple = (v, PrevLineNum+1)
                else:
                    NewDirectionTuple = (v, 1)
                NewTuple = (NewDistance, (GX,GY), NewDirectionTuple)
                heapq.heappush(OuterRim, NewTuple)

Part1Answer, Part2Answer = Answers

print(f"{Part1Answer = }")
print(f"{Part2Answer = }")