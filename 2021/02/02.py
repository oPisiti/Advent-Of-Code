class position_2d():
    def __init__(self):
        self.h     = 0
        self.depth = 0

    def __repr__(self):
        return f"(Height: {self.h}, Depth: {self.depth})"

    def product_position(self):
        return self.h * self.depth


def final_position():
    with open("input.txt") as data:
        commands = data.read().splitlines()
    
    commands = [command.split(" ") for command in commands]
    
    pos = position_2d()

    for command in commands:
        amount = int(command[1])
        match command[0]:
            case "forward": pos.h +=     amount
            case "down":    pos.depth += amount
            case "up":      pos.depth -= amount 

    print(f"Final position: {pos}")
    print(f"Product of final position's coordinates: {pos.product_position()}")


if __name__ == '__main__':
    final_position()