def main():
    with open("input.txt") as data:
        nums = data.read().splitlines()
        nums = [int(num) for num in nums]
        nums.sort()

    needsList = []
    for num in nums:
        needs = 2020 - num
        
        try:
            nIndex = needsList.index(num)
        except ValueError as e:
            needsList.append(needs)
            continue
        
        print(f"Numbers: {num} and {nums[nIndex]}")
        print(num * nums[nIndex])


if __name__ == '__main__':
    main()