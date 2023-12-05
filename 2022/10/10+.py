# Checks if cycle is 20th, 60th, 100th, 140th, 180th or 220th
def checkCycle(cycleNum):
    if (cycleNum-20)%40 == 0 and cycleNum <= 220: return True
    return False

def strength(cycle, registerX):
    return cycle * registerX

def debugMessage(sumSignal, cycle, registerX):
    print(f"Total sum: {sumSignal} at cycle {cycle} with register {registerX}. Adding {cycle*registerX}")

# Decides or not to add strength to signal
def checkAndAdd(sumSignal:int, cycle:int, registerX:int, debug:bool):
    if checkCycle(cycle): 
        sumSignal += strength(cycle, registerX)
        if debug: debugMessage(sumSignal, cycle, registerX)
    
    return sumSignal

# Draws pixel to crt monitor
def drawPixel(cycle, registerX, crt, spriteLength):
    column = cycle%40
    line = int((cycle-1)/40)
    
    if column >= registerX and column <= (registerX + spriteLength - 1):    crt[line] += "#"
    else:                                                                   crt[line] += "."

def main():
    debug = False

    # Getting data from input
    with open("input.txt") as data:
        instructions = data.read().splitlines()

    for i in range(len(instructions)):
        if instructions[i][:4] == "addx": instructions[i] = instructions[i].split(" ")
    
    # + exercise
    # crt = ["."*40 for i in range(6)]
    crt = ["" for i in range(6)]
    spriteLength = 3


    cycle = 0
    registerX = 1
    sumSignal = 0
    for i, inst in enumerate(instructions):
        if inst == "noop": 
            cycle += 1
            sumSignal = checkAndAdd(sumSignal, cycle, registerX, debug)
            drawPixel(cycle, registerX, crt, spriteLength)
        else:      
            cycle+=1
            sumSignal = checkAndAdd(sumSignal, cycle, registerX, debug)
            drawPixel(cycle, registerX, crt, spriteLength)

            cycle+=1
            sumSignal = checkAndAdd(sumSignal, cycle, registerX, debug)
            drawPixel(cycle, registerX, crt, spriteLength)
            registerX += int(inst[1])

    for line in crt: print(line)



if __name__ == '__main__':
    main()