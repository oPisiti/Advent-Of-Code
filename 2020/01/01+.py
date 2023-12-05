def findTriplet(inputPath, sumTo):
    with open(inputPath) as data:
        nums = data.read().splitlines()
        nums = [int(num) for num in nums]
        nums.sort()

    for i, num in enumerate(nums):
        probeA, probeB = i+1, len(nums) - 1

        while probeA < probeB:
            add = num + nums[probeA] + nums[probeB]
            
            if add == sumTo:
                print(f"Triplet: [{num}, {nums[probeA]}, {nums[probeB]}]")
                print(f"Product: {num * nums[probeA] * nums[probeB]}")
                return
            
            elif add < sumTo: probeA += 1
            elif add > sumTo: probeB -= 1

    raise ValueError(f"No triplets found that add up to {sumTo}")


if __name__ == '__main__':
    findTriplet("input.txt", 2020)