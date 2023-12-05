from timeMe import timeMe

@timeMe
def simulate_population():
    with open("input.txt") as data:
        init_state = data.read().split(",")

    new_fish_days_to_rep = 8
    iterations = 256
    population = [init_state.count(str(i)) for i in range(new_fish_days_to_rep+1)]

    # Next day
    for _ in range(iterations):
        zero = population[0]

        auxB = population[new_fish_days_to_rep]
        for i in range(len(population)-2, -1, -1):
            auxA          = population[i]
            population[i] = auxB
            auxB          = auxA

        population[new_fish_days_to_rep] =  zero
        population[6]                    += zero
    
    print(f"At the end of {iterations} days, there are {sum(population)} fish in said school")


if __name__ == '__main__':
    simulate_population()