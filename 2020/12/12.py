from timeMe import timeMe

class Vec2D():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def manhattan(self):
        return abs(self.x) + abs(self.y)

    def __repr__(self):
        return f"<{self.__class__.__name__}> object with pos=({self.x}, {self.y})"

    def __add__(self, obj2):
        return Vec2D(self.x + obj2.x, self.y + obj2.y)
    
    def __mul__(self, scalar):
        return Vec2D(self.x * scalar, self.y * scalar)

@timeMe
def calcShipFinalPos():
    with open("input.txt") as data:
        commands = data.read().splitlines()

    absMovement = {
        "E": Vec2D(1, 0),
        "W": Vec2D(-1, 0),
        "N": Vec2D(0, 1),
        "S": Vec2D(0, -1),
    }

    shipPos = Vec2D(0, 0)
    counterClockRose = "ENWS"
    shipIsFacing = 0

    for command in commands:
        if command[0] in absMovement:
            shipPos += absMovement[command[0]] * int(command[1:])
            continue
        
        addRose = (int(command[1:])/90)
        match command[0]:
            case "L": shipIsFacing = int((shipIsFacing + addRose)%4)
            case "R": shipIsFacing = int((shipIsFacing - addRose)%4)
            case "F": shipPos += absMovement[counterClockRose[shipIsFacing]] * int(command[1:])

    print(f"Final position: {shipPos}. Manhattan distance: {shipPos.manhattan()}")


if __name__ == '__main__':
    calcShipFinalPos()