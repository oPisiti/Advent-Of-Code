import numpy as np

def get_next_index(index: int, step: int, len_list: int) -> int:
    return (index + step)%len_list


def move_item(index: int, li: np.array) -> None:
    """
    Moves the item with index "index" li[index] positions
    in a circle back fashion.
    """

    value_to_move = int(li[index])
    if value_to_move == 0: return

    move_to_index = get_next_index(index, value_to_move, len(li))
    step          = 1 if value_to_move > 0 else -1
    current_index = index

    # Actual moving
    while current_index != move_to_index:
        next_index = get_next_index(current_index, step, len(li))
        li[current_index] = li[next_index]

        current_index = next_index
    
    li[move_to_index] = value_to_move
    print(f'{li}')


def main():
    with open("input.txt") as data:
        li = data.read().splitlines()
    li = [int(item) for item in li]
    
    list_np   = np.array(li, dtype=np.int32)
    orig_list = list_np.copy()

    for item in orig_list:
        new_index = np.where(list_np == item)[0][0]
        move_item(new_index, list_np)

    print(f'Final list: {list_np}')

if __name__ == '__main__':
    main()