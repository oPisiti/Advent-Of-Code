def countValidPasswords():
    with open("input.txt") as data:
        passwords = data.read().splitlines()
    
    for i in range(len(passwords)):
        passwords[i] = passwords[i].split(" ")
        passwords[i][1] = passwords[i][1][0]
        passwords[i][0] = passwords[i][0].split("-")

    counter = 0
    for password in passwords:
        if (password[2][int(password[0][0]) - 1] == password[1]) ^ (password[2][int(password[0][1]) - 1] == password[1]): counter += 1

    print(f"Correct passwords: {counter} out of {len(passwords)}")


if __name__ == '__main__':
    countValidPasswords()