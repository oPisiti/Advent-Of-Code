import re

def apply_iteration(pol: str, rules: list[list[str]]) -> str:
    new_pol = pol

    index_rule = int()
    for rule in rules:
        try:
            index_rule = pol.index(rule[0])
            print(f"Found {rule[0]} at index {index_rule}")
            # input()
        except ValueError as e:
            continue
        
        print(f"{pol} becomes ", end="")
        new_pol = pol[:index_rule+1] + rule[1] + pol[index_rule+1:]
        print(new_pol)

    return new_pol


def main():
    with open("input.txt") as data:
        polymer, instructions = data.read().split("\n\n")
    
    instructions = instructions.splitlines()
    instructions = [re.split(" -> ", inst) for inst in instructions]
    print(instructions)

    n_iterations = 4
    for i in range(n_iterations):
        polymer = apply_iteration(polymer, instructions)
        print(f"Iteration {i+1}: {polymer}")


if __name__ == '__main__':
    main()