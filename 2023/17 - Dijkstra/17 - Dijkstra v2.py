"""
This is the solution of part of the Advent of Code Challenge 2023
Author: oPisiti
"""

from bisect import insort
from functools import cache
import math
import os


class Global:
    MAX_STRAIGHT_LINE = 3


class Index2D:
    def __init__(self, i, j) -> None:
        self.i = i
        self.j = j

    def __add__(self, other):
        if type(other) == Index2D:
            return Index2D(self.i + other.i, self.j + other.j)

        return Index2D(self.i + other[0], self.j + other[1])

    def __sub__(self, other):
        if type(other) == Index2D:
            return Index2D(self.i - other.i, self.j - other.j)

        return Index2D(self.i - other[0], self.j - other[1])
    
    def __eq__(self, other) -> bool:
        if type(other) != Index2D: return False

        return self.i == other.i and self.j == other.j

    def __repr__(self) -> str:
        return f"({self.i}, {self.j})"

 
class Node:
    def __init__(self, pos: Index2D, score: int, came_from: Index2D, line_count: int) -> None:
        self.pos = pos
        self.score = score
        self.came_from = came_from
        self.line_count = line_count


def heat_loss(print_maze = False):
    with open("input.txt") as f:
        data = f.read().strip().split("\n")


    Global.maze = [[int(i) for i in line] for line in data]
    Global.queue = [Node(Index2D(1, 0), 0, Index2D(0, 0), 1),
                    Node(Index2D(0, 1), 0, Index2D(0, 0), 1)]

    Global.nodes = [[Node(Index2D(i, j), math.inf, None, 1) for i in range(len(data[0]))] for j in range(len(data))]
    del data

    # Main loop
    while Global.queue:

        answer = march_crucible(Global.queue.pop(0))
        if print_maze: print_all()
        if answer is not None:             
            if print_maze:
                trace = get_traceback()
                print_all(trace)
            return answer

    pass


def march_crucible(node: Node) -> None:
    # Out of bounds
    if not (0 <= node.pos.i < len(Global.maze)) or not (0 <= node.pos.j < len(Global.maze[0])):
        return

    next_score = node.score + Global.maze[node.pos.i][node.pos.j]

    # Too long in a straight line
    if node.line_count > Global.MAX_STRAIGHT_LINE: 
        return

    # Found the exit
    if [node.pos.i, node.pos.j] == [len(Global.maze) - 1, len(Global.maze[0]) - 1]:
        node.score = next_score
        Global.nodes[node.pos.i][node.pos.j] = node
        return node.score

    # There is a better path to this point
    if next_score > Global.nodes[node.pos.i][node.pos.j].score: 
        return
    
    # Same score but fewer moves in a straight line
    elif next_score == Global.nodes[node.pos.i][node.pos.j].score:
        if node.line_count < Global.nodes[node.pos.i][node.pos.j].line_count:
            node.score = next_score
            Global.nodes[node.pos.i][node.pos.j] = node
        else: 
            return
    
    # Better (smaller) score
    else:
        # Updating the heat loss matrix
        node.score = next_score
        Global.nodes[node.pos.i][node.pos.j] = node

    # Next nodes
    for direction in [Index2D(1, 0), Index2D(0, 1), Index2D(-1, 0), Index2D(0, -1)]:
        next_pos = node.pos + direction

        # Came from here
        if next_pos == node.came_from: continue

        # Continuing a straight line
        if direction == (node.pos - node.came_from):
            insort(Global.queue, 
                   Node(next_pos, next_score, node.pos, node.line_count + 1),
                   key=lambda x: x.score)

        # Turning
        else:
            insort(Global.queue, 
                   Node(next_pos, next_score, node.pos, 1),
                   key=lambda x: x.score)


def print_all(trace = None) -> None:
    # Printing the heat loss 2d list
    os.system("clear")
    for i, line in enumerate(Global.nodes):
        for j, node in enumerate(line):

            if trace is not None and Index2D(i, j) in trace:
                print(f"\033[92m{node.score:03}\033[0m ", end="")
            
            else:
                print(f"{node.score:03} ", end="")
        
        print()


def get_traceback() -> None:
    curr_pos = Index2D(len(Global.maze)-1, len(Global.maze[0])-1)

    traceback = []
    while curr_pos != Index2D(0, 0):
        traceback.append(curr_pos)
        print(f"({curr_pos.i}, {curr_pos.j})")
        curr_pos = Global.nodes[curr_pos.i][curr_pos.j].came_from

    return traceback


if __name__ == '__main__':
    print(heat_loss(print_maze = True))
    # print(heat_loss())