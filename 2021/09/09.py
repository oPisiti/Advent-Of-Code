import numpy as np
import re

def main():
    with open("input.txt") as data:
        heights_base = data.read().splitlines()

    heights_base = [re.findall("\d{1}", string) for string in heights_base]
    heights = np.array(heights_base, dtype=np.uint8)

    print(heights)

    # Getting sum of risks based on if a lowpoint
    sum_risk = 0
    for i in range(heights.shape[0]):
        for j in range(heights.shape[1]):
            current = heights[i][j]
            
            # Whenever it is not a lowpoint
            if i > 0: 
                if heights[i-1][j] <= current: continue            
            if i < (heights.shape[0] - 1): 
                if heights[i+1][j] <= current: continue
            if j > 0: 
                if heights[i][j-1] <= current: continue            
            if j < (heights.shape[1] - 1): 
                if heights[i][j+1] <= current: continue

            # Else (is lowpoint)
            sum_risk += current + 1
            print(f"Point ({i}, {j}) = {current} is a low point. Adding {current+1} risk. Total risk: {sum_risk}")
        
    print(f"Sum of risks: {sum_risk}")


if __name__ == '__main__':
    main()



# class Basin:
#     def __init__(self, basinMap):
#         self.map = basinMap

#     def search_points(self) -> int:
#         riskLevel = 0
#         for mapDex, row in enumerate(self.map):
#             for idx, col in enumerate(row):
#                 if (col != 9):
#                     if self.is_low_point([mapDex, idx], col):
#                         riskLevel += (int(col) + 1)
        
#         return riskLevel

#     def is_low_point(self, point, val) -> bool:
#         directions = self.find_directions(point)
        
#         lowest = True
#         for check in directions:
#             if (self.map[check[0]][check[1]] <= val):
#                 lowest = False

#         return lowest

#     def find_directions(self, point) -> list:
#         directions = [[(point[0] - 1), point[1]], [(point[0] + 1), point[1]], [point[0], (point[1] - 1)], [point[0], (point[1] + 1)]]
#         remove = []
#         if (point[0] == 0):
#             remove.append(directions[0])
#         elif (point[0] == (len(self.map) - 1)):
#             remove.append(directions[1])
        
#         if (point[1] == 0):
#             remove.append(directions[2])
#         elif (point[1] == (len(self.map[0]) - 1)):
#             remove.append(directions[3])
        
#         for x in remove:
#             directions.remove(x)

#         return directions

# ### MAIN ###
# if __name__ == "__main__":
#     with open("input.txt") as f:
#         lines = f.read().splitlines()

#     smokeBasin = Basin(lines)
#     answer = smokeBasin.search_points()
#     print("The risk level is " + str(answer))