def main():
    with open("input.txt") as data:
        answers = data.read().split("\n\n")
    
    for i in range(len(answers)): answers[i] = answers[i].split("\n")

    count = 0
    for group in answers:
        appearences = {}
        for person in group:
            for question in person:
                if question not in appearences: appearences[question] = 1
                else:                           appearences[question] += 1

        for question in appearences:
            if appearences[question] == len(group): count += 1
    
    print(f"Sum of counts: {count}")


if __name__ == '__main__':
    main()