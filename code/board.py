import Visualization as vis
import DataGen as dg


class board():
    def __init__(self, boardSize):
        assert boardSize % 2 == 0
        self.soldiers_info = dg.Soldiers1(boardSize)
        self.soldiers_position, self.soldiers_point = dg.unpack_soldiers_info(self.soldiers_info, boardSize)
        self.boardSize = boardSize

    def visualize(self, queens_position):
        vis.visualize(board_size=self.boardSize, soldiers_position=self.soldiers_position,
                      queens_position=queens_position)

    def max_fitness(self):
        max_fit = 0
        for el in list(self.soldiers_point.values()):
            max_fit += el[0]
        return max_fit
