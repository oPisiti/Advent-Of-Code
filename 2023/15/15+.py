"""
This is the solution of part of the Advent of Code Challenge 2023
Author: oPisiti
"""


import re


class Lens():
    def __init__(self, focus: int, pos: int):
        self.focus = focus
        self.pos = pos


def focusing_power() -> int:
    boxes_count = 256

    with open("input.txt") as f:
        data = f.read().strip().split(",")


    boxes = [dict() for _ in range(boxes_count)]

    # Processing each step
    for step in data:
        label, op, focus = parse_step(step)

        box_number = hash(label)

        # Add operation
        if op == "=":
            # Lens label already present
            if label in boxes[box_number].keys():
                boxes[box_number][label].focus = focus

            # Adding new lens
            else:
                boxes[box_number][label] = Lens(focus, len(boxes[box_number]) + 1)

        # Remove operation
        elif op == "-":
            # Lens label already present
            if label in boxes[box_number].keys():
                label_pos = boxes[box_number][label].pos

                # Subtracting 1 from boxes behind
                for l in boxes[box_number].keys():
                    if boxes[box_number][l].pos > label_pos:
                        boxes[box_number][l].pos -= 1

                # Removing the label
                boxes[box_number].pop(label, None)    

    # Calculating the power
    return sum([sum([(box_num + 1) * lens.pos * lens.focus for lens in box.values()]) for box_num, box in enumerate(boxes)])


def hash(step: str) -> int:
    curr_value = 0

    for char in step:
        curr_value += ord(char)
        curr_value *= 17
        curr_value %= 256
        
    return curr_value    


def parse_step(step: str) -> (str, str, int):
    label, focus = re.split("=|-", step)

    if focus: return label, "=", int(focus)

    return label, "-", 0


if __name__ == '__main__':
    print(focusing_power())