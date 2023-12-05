def main():
    with open("input.txt") as data:
        answers = data.read().split("\n\n")
    
    for i in range(len(answers)): answers[i] = answers[i].split("\n")

    count = 0
    for group in answers:
        ansSet = set()
        for person in group:
            for question in person:
                ansSet.add(question)

        count += len(ansSet)
    
    print(f"Sum of counts: {count}")


if __name__ == '__main__':
    main()