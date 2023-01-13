def main():
    with open("input.txt") as data:
        crates, procedure = data.read().split("\n\n")

    # Getting crates data into an array
    crates = crates.split("\n")[0:-1]
    cratesArr = [[] for i in range(int((len(crates[0])+1)/4))]
    for line in crates:
        for i in range(0, len(line), 4):
            if line[i:i+3] != "   ":
                cratesArr[int(i/4)].append(line[i:i+3])

    for i in range(len(cratesArr)):
        cratesArr[i] = cratesArr[i][::-1]

    # Getting procedures into an array
    baseProcedure = procedure.split("\n")
    procedureArr = []
    for i in range(len(baseProcedure)):
        temp = baseProcedure[i].split(" ")
        procedureArr.append([int(temp[1]), int(temp[3]), int(temp[5])])

    # Applying the procedures
    for proc in procedureArr:
        for i in range(proc[0]):
            cratesArr[proc[2]-1].append(cratesArr[proc[1]-1][-1])
            cratesArr[proc[1]-1] = cratesArr[proc[1]-1][:-1]

    print(f"Top crates: ", end="")
    for stack in cratesArr:
        print(stack[-1][1], end="")


if __name__ == "__main__":
    main()