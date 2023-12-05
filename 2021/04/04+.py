import numpy as np
import re
import timeMe as tm

def get_boards(file_path: str):
    """
    Gets all numbers (list[int]) and boards (np.array)
    """

    with open(file_path) as data:
        all_data = data.read().split("\n\n")
    
    drawn_numbers = [int(num) for num in all_data[0].split(",")]
    
    # Cleaning the boards information
    rows_boards   = [board.split("\n") for board in all_data[1:]]
    boards        = [[re.findall("\d+", row) for row in board] for board in rows_boards]
    n_boards      = len(boards)

    # Initializing boards
    i_len, j_len = len(boards[0]), len(boards[0][0])
    np_boards = np.empty((n_boards, i_len, j_len), dtype=np.uint16)
    for i in range(n_boards):
        a_board = np.array(boards[i], dtype=np.uint16)
        np_boards[i] = a_board

    return drawn_numbers, np_boards


def get_partial_score(boards: np.array, bool_boards: np.array, latest_called_number: int, losing_boards: np.array) -> int:
    """
    Returns the score of the column or row that is fully marked
    """

    losing_indexes = [v for v, value in enumerate(losing_boards) if value]
    # print(f"Losing indexes: {losing_indexes}")

    # Checking rows
    for z_losing in losing_indexes:
        for i, row in enumerate(bool_boards[z_losing]):
            row_is_marked = True
            for j, item in enumerate(row):
                # print(f"Item: {item}")
                if not item: 
                    row_is_marked = False
                    break                   
            
            if row_is_marked:
                print(f"R Board {z_losing} is a winner")
                # input()
                losing_boards[z_losing] = False
                # found_good_board(boards, bool_boards, losing_boards, z_losing, latest_called_number)
                break

    # Checking columns
    for z_losing in losing_indexes:
        for j in range(len(bool_boards[z_losing][0])):
            column_is_marked = True
            for i in range(len(bool_boards[z_losing])):
                if not bool_boards[z_losing][i][j]: 
                    column_is_marked = False
                    break
            
            if column_is_marked: 
                print(f"C Board {z_losing} is a winner")
                losing_boards[z_losing] = False
                # found_good_board(boards, bool_boards, losing_boards, z_losing, latest_called_number)
                break
    
    if np.count_nonzero(losing_boards) == 1:
        biggest_loser = [loser for loser in losing_indexes if loser][0]
        print(f"Biggest loser index: {biggest_loser}")
        return sum_not_marked(boards[biggest_loser], bool_boards[biggest_loser])
    return -1


def sum_not_marked(board: np.array, winner_bool_board: np.array) -> int:
    """
    Returns the score of the bingo board based on the board and the winner boolean board
    """
    
    score = 0
    for i, row in enumerate(board):
        for j in range(len(row)):
            if not winner_bool_board[i][j]: score += board[i][j]

    return score



def mark_numbers(num: int, boards: np.array, marked_boards: np.array) -> None:
    """
    Marks as true on marked_boards all occurences of num in boards
    """
    
    for z, board in enumerate(boards):
        found_in_board = False

        for i, row in enumerate(board):
            for j, item in enumerate(row):
                if item == num:
                    marked_boards[z][i][j] = True
                    found_in_board = True
                    break
            
            if found_in_board: break

@tm.timeMe
def lose_bingo():
    """
    Loses a really nice game of bingo :)
    """

    drawn_numbers, boards = get_boards("input.txt")
    marked_boards         = np.full(np.shape(boards),    False, dtype=np.bool_)
    losing_boards         = np.full(np.shape(boards)[0], True,  dtype=np.bool_)

    final_score = -1
    for i, number in enumerate(drawn_numbers):
        # Marking boards
        mark_numbers(number, boards, marked_boards)

        print(f"Number: {number}")
        partial_score = get_partial_score(boards, marked_boards, number, losing_boards)
        
        # print(f"losing_boards: {losing_boards}\n")

        if len([True for board in losing_boards if board]) == 1:
            print(f"Losing_boards: {losing_boards}")
            # TODO: Play the game one last time
            mark_numbers(drawn_numbers[i+1], boards, marked_boards)
            partial_score = sum_not_marked(boards[biggest_loser], bool_boards[biggest_loser])
            final_score = partial_score * drawn_numbers[i+1]

            print(f"Partial score: {partial_score}")
            print(f"Next number:   {drawn_numbers[i+1]}")
            print(f"Final score:   {final_score}")
            return
    

if __name__ == '__main__':
    lose_bingo()