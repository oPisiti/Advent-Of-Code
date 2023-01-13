def checkConnected(a:list, b:list) -> bool:
    checks = []
    for i in range(3):
        if   a[i] == b[i]:                      checks.append("equal")
        elif a[i] == b[i]+1 or a[i] == b[i]-1:  checks.append("diff")

    if checks.count("equal") == 2 and checks.count("diff") == 1: 
        
        return True
    
    return False

def areaDroplet(cubes:list[list], checked:list, index = 0) -> int:
    for i, cube in enumerate(cubes):
        for index in checked:
            if checkConnected()

def main():
    with open("input.txt") as data:
        cubes = data.read().splitlines()

    for i, cube in enumerate(cubes):
        cubes[i] = cube.split(",")

    indexesChecked = []
    print(areaDroplet(cubes, indexesChecked))


if __name__ == "__main__":
    main()