import numpy
import random
import time

def initialize_board(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if (random.randint(0, 1) == 1):
                board[i][j] = 1

# Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

def count_neighbors(board, i, j):
    # if row_offset in range(-1, 2):
        # if col_offset in range(-1, 2):
            # n_x = i + row_offset
            # if (board[x][y] == 1):
                # count += 1
    return numpy.sum(
        board[max(i-1, 0):i+2, max(j-1, 0):j+2]
    ) - board[i][j]

if __name__ == "__main__":
    board_size = (10, 10)
    board = numpy.zeros(board_size)
    initialize_board(board)

    num_epochs = 10
    for _ in range(num_epochs):
        print("")
        print(board)
        print("")
        time.sleep(1)
        new_board = numpy.zeros(board_size)

        for i in range(len(board)):
            for j in range(len(board)):
                num_neighbors = count_neighbors(board, i, j)
                # print(f'({i}, {j}): {num_neighbors}')
                if (board[i][j] == 1 and (num_neighbors == 2 or num_neighbors == 3)):
                    new_board[i][j] = 1
                elif (num_neighbors == 3):
                    new_board[i][j] = 1

        board = new_board

