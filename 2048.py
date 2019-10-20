from model import Model
from view import View


class Controller:

    def __init__(self, test=False):
        self.view = View()
        if test:
            import numpy as np
            self.view.board = np.array([[1, 3, 0, 0],
                                        [2, 5, 6, 12],
                                        [3, 7, 932, 644],
                                        [4, 8, 9, 1238]])
        self.model = Model()
        self.view.reset_view()

    def add_tile(self):
        new_tile = self.model.new_tile()
        new_loc = self.model.new_loc(self.view.board)
        self.view.add_tile(new_tile, new_loc)

    def loop(self):
        self.add_tile()

        while True:
            move_to = self.model.move_to()
            self.view.board, moved = self.model.update_board(self.view.board,
                                                             move_to)
            print(moved)
            if moved:
                break

        self.view.reset_view()
        self.view.update_view()

    def start(self):
        self.add_tile()
        self.view.view.imshow(self.view.board)
        while not self.model.game_over:
            self.loop()
        print("GAME OVER")
        print("SCORE :", self.model.score)


if __name__ == '__main__':
    import sys
    game = Controller(sys.argv[1])
    game.start()
