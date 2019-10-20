import numpy as np
import matplotlib.pyplot as plt


class View:

    def __init__(self):
        plt.ion()
        self.board = np.zeros((4, 4), dtype=np.uint64)
        _, self.view = plt.subplots()

    def add_tile(self, new_tile, new_loc):
        self.board[new_loc] = new_tile

    def reset_view(self):
        self.view.clear()
        self.view.set_xticks([])
        self.view.set_yticks([])

    def update_view(self):
        self.view.imshow(self.board)
        for i in range(4):
            for j in range(4):
                if self.board[i, j] == 0:
                    text = ""
                else:
                    text = self.board[i, j]
                self.view.text(j, i, text,
                               ha="center", va="center", color="w")
        plt.draw()
        plt.pause(0.05)
