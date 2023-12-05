def Wind(path: str) -> str:
    with open(path) as data:
        wind = data.read()

    count = 0
    while True:
        yield wind[count]
        count = (count + 1) % len(wind)


class Chamber:
    def __init__(self):
        self.chamber = []

        self.chamber_width = 7
        self.separation_from_floor = 3
        self.left_padding = 2

    def print_chamber(self) -> None:
        """
        Prints a nice little chamber
        """

        for row in self.chamber:
            print(row)

    def put_to_chamber(self,  rock: list[str]) -> None:
        """
        Puts a rock into the chamber.
        Adds height to chamber list as necessary.
        """

        # Adjusting the chamber height to separate it 3 units from floor
        for _ in range(self.separation_from_floor):
            self.chamber.insert(0, "." * self.chamber_width)

        # Putting rock into chamber
        for rock_row in rock:
            right_padding = self.chamber_width - self.left_padding - len(rock_row)
            new_row = "." * self.left_padding + rock_row + "." * right_padding
            self.chamber.insert(0, new_row)


def main():
    global separation_from_floor, left_padding
    

    wind_dir = Wind("wind.txt")

    # Rocks
    with open("rocks.txt") as data:
        rocks = data.read().split("\n\n")
    rocks = [rock.split("\n") for rock in rocks]
    
    chamber = Chamber()
    
    n_iterations = 4
    for count in range(n_iterations):
        rock_index = count % len(rocks)
        
        # Getting the rock's final j position
        final_j = 2
        for _ in range(chamber.separation_from_floor):
            # TODO: Figure out collision
        chamber.put_to_chamber(rocks[rock_index])
        # apply_gravity

    chamber.print_chamber()

if __name__ == "__main__":
    main()
