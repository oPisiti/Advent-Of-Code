class Planet():
    def __init__(self, name, orbits = None):
        self.name = name
        self.orbits_directly = orbits
        self.orbits_n_planets = None

    def count_orbits(self):
        if self.name == "COM": return

        inner_planet = self.orbits_directly
        
        if inner_planet.name == "COM":
            self.orbits_n_planets = 1
            return
        
        if inner_planet.orbits_n_planets is None:
            inner_planet.count_orbits()

        self.orbits_n_planets = inner_planet.orbits_n_planets + 1
        return


def main():
    with open("input.txt") as data:
        orbits = data.read().splitlines()

    orbits = [orbit.split(")") for orbit in orbits]

    # Initializing the planets with the correct orbit
    planets = {"COM": Planet("COM")}
    for orb in orbits:
        inner, outer = orb[0], orb[1]
        if inner not in planets.keys():
            planets[inner] = Planet(inner)

        if outer in planets.keys():
            planets[outer].orbits_directly = planets[inner]
        else:
            planets[outer] = Planet(outer, planets[inner])

    # Count
    for planet in planets.values():
        planet.count_orbits()

    n_all_orbits = 0
    for planet in planets.values():
        planets_orb = planet.orbits_n_planets
        n_all_orbits += planets_orb if planets_orb is not None else 0

    print(f"Count of all direct and indirect orbits: {n_all_orbits}")


if __name__ == '__main__':
    main()