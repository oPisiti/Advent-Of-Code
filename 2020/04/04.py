import re

def countValid():
    with open("input.txt") as data:
        passports = data.read().split("\n\n")
    
    for i, passport in enumerate(passports):
        passports[i] = re.split("\n| ", passport)

    fields = [{field[:3] for field in person} for person in passports]

    mustHaveFields = {
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid"}

    numValid = 0
    for passport in fields:
        if mustHaveFields.issubset(passport): numValid += 1

    print(f"{numValid} passports are valid")

if __name__ == '__main__':
    countValid()