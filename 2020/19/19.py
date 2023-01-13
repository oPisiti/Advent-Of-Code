import re

def isComplete(string: str):
    return True if re.fullmatch('^\D+$', string) else False


def cleanRegex(rules: str):
    for i, rule in enumerate(rules):
        # print(f"Input/Output strings: {rule[1]} -> ", end="")
        
        while re.search("\({1}([a-z]+)\){1}", rules[i][1]):
            rules[i][1] = re.sub("\({1}(?P<dig>[a-z]+)\){1}", "\g<dig>", rules[i][1])

        # print(f"{rule[1]}")
    # input()


def main():
    # Getting and cleaning data
    with open("input.txt") as data:
        [rules, messages] = data.read().split("\n\n")

    messages = messages.splitlines()

    rules = [a.split(": ") for a in rules.split("\n")]
    for i in range(len(rules)):
        rules[i][1] = rules[i][1].replace("\"", "")
        rules[i][1] = rules[i][1].replace(" ", "")
        rules[i][1] = re.sub('(\d+)', '(\g<0>)', rules[i][1])
    
    # Creating a regex string of rule[0]
    while not isComplete(rules[0][1]):
        for r, rule in enumerate(rules):
            if isComplete(rule[1]):
                # print(f"Rule {rule[0]} is complete")
                for i in range(len(rules)):
                    rules[i][1] = rules[i][1].replace(rule[0], f"({rule[1]})")
                    # rules[i][1] = re.sub('\((\D)+\)', '\g<0>', rules[i][1])
                    # print(f"rules {i}: {rules[i][1]}")
                
        
        cleanRegex(rules)

    for i, rule in enumerate(rules):
        if rule[0] == "0":
            indexRule0 = i
            break

    print(f"Rule 0 has index {indexRule0}")
    rule0 = "^" + rules[indexRule0][1] + "$"
    print(f"Final regex of rule 0: {rule0}")

    # Applying regex string of rule 0 to all the messages
    sumValidMessages = 0
    for message in messages:
        if re.search(rule0, message):
            sumValidMessages += 1
    
    print(f"There are {sumValidMessages} valid messages")


if __name__ == '__main__':
    main()