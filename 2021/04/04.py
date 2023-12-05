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


def get_score(boards: np.array, bool_boards: np.array, latest_called_number: int) -> int:
    """
    Returns the score of the column or row that is fully marked
    """

    # Checking rows
    for z, board in enumerate(bool_boards):
        for i, row in enumerate(board):
            row_is_marked = True
            for j, item in enumerate(row):
                if not item: 
                    row_is_marked = False
                    break
            
            if row_is_marked: return latest_called_number * sum_not_marked(boards[z], bool_boards[z])

    # Checking columns
    for z, board in enumerate(bool_boards):
        for j in range(len(board[0])):
            column_is_marked = True
            for i in range(len(board)):
                if not board[i][j]: 
                    column_is_marked = False
                    break
            
            if column_is_marked: return latest_called_number * sum_not_marked(boards[z], bool_boards[z])
    
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
def play_bingo():
    """
    Plays a really nice game of bingo :)
    """

    drawn_numbers, boards = get_boards("input.txt")
    marked_boards         = np.full(np.shape(boards), False, dtype=np.bool_)

    final_score = -1
    for number in drawn_numbers:
        # Marking boards
        mark_numbers(number, boards, marked_boards)

        final_score = get_score(boards, marked_boards, number)

        if final_score > -1:
            print(f"Final score: {final_score}")
            return
    

if __name__ == '__main__':
    play_bingo()