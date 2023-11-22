import numpy as np
import cv2 as cv


class Visualization():
    def __init__(self, boardSize=8):
        assert boardSize % 2 == 0
        self.boardSize = boardSize
        self.grid_dimension_x = [-int(self.boardSize / 2), int(self.boardSize / 2)]
        self.grid_dimension_y = [-int(self.boardSize / 2), int(self.boardSize / 2)]
        self.each_squ = [60, 60]
        pass

    def InitialImage(self):
        self.image = np.zeros(((self.grid_dimension_x[1] - self.grid_dimension_x[0]) * self.each_squ[0],
                               (self.grid_dimension_y[1] - self.grid_dimension_y[0]) * self.each_squ[1], 3),
                              dtype=np.uint8)
        indexrow = 0
        for i in np.arange(0, self.image.shape[0] + self.each_squ[0], self.each_squ[0]):
            indexrow += 1
            indexcol = 0
            for j in np.arange(0, self.image.shape[0] + self.each_squ[0], self.each_squ[0]):
                indexcol += 1
                if (indexcol + indexrow) % 2 == 0:
                    cv.rectangle(self.image, (i, j), (i + self.each_squ[0], j + self.each_squ[0]), (255, 255, 255), -1)
        top, bottom, left, right = 10, 10, 10, 10
        borderType = cv.BORDER_CONSTANT
        value = [41, 114, 245]
        # Add borders with above parameters
        self.image = cv.copyMakeBorder(self.image, top, bottom, left, right,
                                       borderType, None, value)

    def AddChessPiece(self, col=-3, row=4, text="", color=[]):
        assert col < self.boardSize and row >= -self.boardSize
        i, j = col, row
        j = -j - 1
        text_org_x = int(((i - self.grid_dimension_x[0]) + 0.6) * self.each_squ[0])
        text_org_y = int(((j - self.grid_dimension_y[0]) + 0.6) * self.each_squ[1])
        text_size, _ = cv.getTextSize(text, cv.FONT_HERSHEY_SIMPLEX, 0.5, 1)
        text_org = (text_org_x - text_size[0] // 2, text_org_y + text_size[1] // 2)
        cv.putText(self.image, text, text_org, cv.FONT_HERSHEY_SIMPLEX, 0.5, color, 2, cv.LINE_AA)

    def Movehorse(self, startPoint=[], EndPoint=[0, 0], color=(128, 0, 100)):
        startPoint = [int(((startPoint[0] - self.grid_dimension_x[0]) + 0.5) * self.each_squ[0]),
                      int(((-startPoint[1] - 1 - self.grid_dimension_y[0]) + 0.5) * self.each_squ[1])]
        EndPoint = [int(((EndPoint[0] - self.grid_dimension_x[0]) + 0.5) * self.each_squ[0]),
                    int(((-EndPoint[1] - 1 - self.grid_dimension_y[0]) + 0.5) * self.each_squ[1])]
        cv.arrowedLine(self.image, tuple(startPoint), tuple(EndPoint), color, 2, tipLength=0.04)


def position_existence(row, col, position):
    for pos in position:
        if pos[0] == row and pos[1] == col:
            return True
    return False


def visualize(board_size, soldiers_position, queens_position):
    Visualizationobj = Visualization(boardSize=board_size)
    Visualizationobj.InitialImage()
    # print("soldiers_position:" + str(soldiers_position))
    # print("queens_position:" + str(queens_position))
    for row in range(-int(Visualizationobj.boardSize / 2), int(Visualizationobj.boardSize / 2)):
        for col in range(-int(Visualizationobj.boardSize / 2), int(Visualizationobj.boardSize / 2)):
            # print("row: " + str(row))
            # print("col: " + str(col))
            if position_existence(row, col, soldiers_position):
                Visualizationobj.AddChessPiece(col=col, row=row, text="{}, {}".format(row, col),
                                               color=(255, 0, 0))
                # print("soldier")
            elif position_existence(row, col, queens_position):
                Visualizationobj.AddChessPiece(col=col, row=row, text="{}, {}".format(row, col),
                                               color=(0, 255, 0))
                # print("queen")
            else:
                if abs(row + col) % 2 == 0:
                    Visualizationobj.AddChessPiece(col=col, row=row, text="{}, {}".format(row, col),
                                                   color=(255, 255, 255))
                else:
                    Visualizationobj.AddChessPiece(col=col, row=row, text="{}, {}".format(row, col),
                                                   color=(0, 0, 0))
            # print("--------------------------")
    cv.imwrite("Position_Notation.png", Visualizationobj.image)
