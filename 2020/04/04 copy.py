import re

def check_passport(passport: list[str]):
    sorted_passport = sorted(passport)

    if sorted_passport[1][:3] == "cid": 
        sorted_passport = sorted_passport[0:1] + sorted_passport[2:]

    for i, field in enumerate(sorted_passport):
        field_name = field[:3]
        data =       field[4:]
        if field_name in {"byr", "eyr", "iyr"}: int_data = int(data)
        
        match field_name:
            case "byr":         
                if (len(data) != 4) or (int_data < 1920) or (int_data > 2002):
                    return 0 
                continue

            case "ecl":         
                if data not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
                    return 0
                continue

            case "eyr":         
                if len(data) != 4 or int_data < 2020 or int_data > 2030:
                    return 0
                continue

            case "hcl":         
                if data[0] != "#" or not re.match("^[a-f|0-9]{6}$", data[1:]):
                    return 0
                continue

            case "hgt":         
                unit = data[-2:]
                if unit not in {"cm", "in"}:                                   return 0

                int_height = int(data[:-2])

                if   unit == "cm" and (int_height < 150 or int_height > 193):  return 0
                elif unit == "in" and (int_height < 59 or int_height > 76):    return 0
                continue

            case "iyr":         
                if len(data) != 4 or int_data < 2010 or int_data > 2020:
                    return 0
                continue

            case "pid":         
                if len(data) != 9: return 0
                continue

    return 1


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
        "pid"
    }

    numValid = 0
    for i, person in enumerate(passports):
        if mustHaveFields.issubset(fields[i]):     
            numValid += check_passport(person)

    print(f"{numValid} passports are valid")

if __name__ == '__main__':
    countValid()