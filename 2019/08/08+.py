import re

def get_pixel_color(layers: list[str], pixel_index: int) -> str:
    """
    Loops over all the layer to find a pixel color
    """

    if pixel_index >= len(layers[0]): raise IndexError(f"Index {pixel_index} is not valid")
    
    for i in range(len(layers)):
        pixel_color = layers[i][pixel_index]     
        if pixel_color != "2": return pixel_color

    raise AttributeError(f"Only found transparent pixels")


def main():
    with open("input.txt") as data:
        image = data.read()
    
    i_max, j_max = 6, 25
    size_layer = i_max * j_max
    layers = [image[size_layer*i:size_layer*(i+1)] for i in range(int(len(image)/size_layer))]

    count_0 = [len(re.findall("0{1}", layer)) for layer in layers]
    
    min_0_index = 0
    for i in range(1, len(count_0)):
        if count_0[i] < count_0[min_0_index]: min_0_index = i

    count_1 = len(re.findall("1{1}", layers[min_0_index]))
    count_2 = len(re.findall("2{1}", layers[min_0_index]))

    # Getting the final image
    final_img = ""
    for i in range(len(layers[0])):
        final_img += get_pixel_color(layers, i)

    # Showing the picture
    for i in range(int(len(layers[0])/j_max)):
        for pixel in final_img[i * j_max: (i+1) * j_max]:
            print("O" if pixel=="1" else " ", end="")
        print()

if __name__ == '__main__':
    main()