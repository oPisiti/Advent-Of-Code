def checkCycle(cycleNum):
    if (cycleNum-20)%40 == 0 and cycleNum <= 220: return True
    return False

def strength(cycle, registerX):
    return cycle * registerX

def debugMessage(sumSignal, cycle, registerX):
    print(f"Total sum: {sumSignal} at cycle {cycle} with register {registerX}. Adding {cycle*registerX}")

def checkAndAdd(sumSignal:int, cycle:int, registerX:int, debug:bool):
    if checkCycle(cycle): 
        sumSignal += strength(cycle, registerX)
        if debug: debugMessage(sumSignal, cycle, registerX)
    
    return sumSignal

def main():
    debug = True

    with open("input.txt") as data:
        instructions = data.read().splitlines()

    for i in range(len(instructions)):
        if instructions[i][:4] == "addx": instructions[i] = instructions[i].split(" ")
    
    cycle = 0
    registerX = 1
    sumSignal = 0
    for i, inst in enumerate(instructions):
        if inst == "noop": 
            cycle += 1
            sumSignal = checkAndAdd(sumSignal, cycle, registerX, debug)
        else:      
            cycle+=1
            sumSignal = checkAndAdd(sumSignal, cycle, registerX, debug)
            
            cycle+=1
            sumSignal = checkAndAdd(sumSignal, cycle, registerX, debug)

            registerX += int(inst[1])

    print(f"Sum of the signal strengths: {sumSignal}")



if __name__ == '__main__':
    main()