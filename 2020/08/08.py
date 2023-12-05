def main():
    with open("input.txt") as data:
        instructions = data.read().splitlines()

    for i, inst in enumerate(instructions):
        instructions[i] = inst.split(" ")
    
    accumulator  = 0
    i = 0
    linesVisited = [i]
    while True:
        argument = int(instructions[i][1])
        match instructions[i][0]:
            case "acc": 
                accumulator += argument
                i += 1
            case "jmp":
                i += argument
            case "nop":
                i += 1

        if i in linesVisited: 
            print(f"Accumulator at {accumulator} when loop detected")
            return

        linesVisited.append(i)



if __name__ == '__main__':
    main()