import re
import math

def main():
    with open("input.txt") as data:
        image = data.read()
    
    size_layer = 25 * 6
    layers = [image[size_layer*i:size_layer*(i+1)] for i in range(int(len(image)/size_layer) - 1)]

    count_0 = [len(re.findall("0{1}", layer)) for layer in layers]
    
    min_0_index = 0
    for i in range(1, len(count_0)):
        if count_0[i] < count_0[min_0_index]: min_0_index = i

    count_1 = len(re.findall("1{1}", layers[min_0_index]))
    count_2 = len(re.findall("2{1}", layers[min_0_index]))

    print(f'Answer: {count_1 * count_2}')


if __name__ == '__main__':
    main()