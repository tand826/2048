import numpy as np


class Model:
    # Model of MVC

    def __init__(self):
        self.tiles = [2, 4]
        self.proba = [0.875, 0.125]
        self.up = {"w", "i", "8"}
        self.left = {"a", "j", "4"}
        self.down = {"s", "k", "2"}
        self.right = {"d", "l", "6"}
        self.game_over = False
        self.score = 0

    def new_tile(self):
        # Set the new tile of the next move.
        return np.random.choice(self.tiles, p=self.proba)

    def new_loc(self, board):
        # Get blank cells and determine the next cell to place the number.
        blank_x, blank_y = np.where(board == 0)
        if len(blank_x) > 0:
            i = np.random.randint(len(blank_x))
            new_loc = (blank_x[i], blank_y[i])
        else:
            # False means there is no blank space.
            new_loc = False
            self.can_move(board)
        return new_loc

    def can_move(self, board):
        moves = []
        for move_to in ["up", "left", "down", "right"]:
            new_board, moved = self.update_board(board, move_to)
            moves.append(moved)
        if np.sum(moves) == 0:
            self.game_over = True

    def move_to(self):
        # Get the input and parse it to the direction
        typed = False
        while not typed:
            key = input("Next move? ")
            if key in self.up:
                move_to = "up"
                typed = True
            elif key in self.left:
                move_to = "left"
                typed = True
            elif key in self.down:
                move_to = "down"
                typed = True
            elif key in self.right:
                move_to = "right"
                typed = True
            elif key == "exit":
                print("GAME OVER")
                print("SCORE :", self.score)
                import sys
                sys.exit()
            else:
                print("N/A key")
        return move_to

    def update_board(self, board, move_to):
        # Update the board with the new number.

        original_board = board.copy()
        # Align the matrix to check the value from left to right
        if move_to == "up":
            tmp_board = np.rot90(board, 1)
        elif move_to == "left":
            tmp_board = np.rot90(board, 0)
        elif move_to == "down":
            tmp_board = np.rot90(board, -1)
        elif move_to == "right":
            tmp_board = np.rot90(board, -2)

        # Process each line
        for i in range(4):
            line = tmp_board[i, :]
            line = self._zero_to_right(line)

            # 2 values from the left
            for j in range(3):

                # skip if the left value is 0
                if line[j] == 0:
                    continue

                # Merge if the values are same
                elif line[j] == line[j+1]:
                    self.score += int(line[j])
                    line[j] = line[j] * 2
                    line[j+1] = 0

            line = self._zero_to_right(line)

            # Align the matrix to the original direction : insert to tmp_board
            tmp_board[i, :] = line
        print(original_board)
        print(board)

        moved = np.sum(original_board != board) != 0

        return board, moved

    def _zero_to_right(self, line):
        # Put 0s to right
        # ex: [2,0,2,4] -> [2,2,4,0]
        zero = line[np.where(line == 0)[0]]
        nonzero = line[np.where(line != 0)[0]]
        line = np.concatenate([nonzero, zero], axis=0)
        return line
