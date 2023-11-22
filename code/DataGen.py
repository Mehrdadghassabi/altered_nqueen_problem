import numpy as np
import random

# The last 3 digits of the student number like 4013644017 is 017
np.random.seed(29)


def Soldiers1(BoardSize=8):
    possRow = range(1, BoardSize + 1)
    possCol = range(1, BoardSize + 1)
    allPossiblePositions = []
    for i in possRow:
        for j in possCol:
            allPossiblePositions.append([i, j])
    random.shuffle(allPossiblePositions)
    Soldiers = []
    for i in range(BoardSize - 1):
        Soldiers.append([allPossiblePositions[i], np.random.randint(1, 4)])
    return Soldiers


def Queens(BoardSize=8, soldiers_position=[]):
    possRow = range(1, BoardSize + 1)
    possCol = range(1, BoardSize + 1)
    allPossiblePositions = []
    for i in possRow:
        for j in possCol:
            if not [i, j] in soldiers_position:
                allPossiblePositions.append([i, j])
    random.shuffle(allPossiblePositions)
    queens = []
    for i in range(BoardSize - 2):
        queens.append(allPossiblePositions[i])
    return queens


def Soldiers2(BoardSize=8):
    possRow = range(1, BoardSize + 1)
    possCol = range(1, BoardSize + 1)
    allPossiblePositions = []
    for i in possRow:
        for j in possCol:
            allPossiblePositions.append([i, j])
    random.shuffle(allPossiblePositions)
    Soldiers = []
    for i in range(2 * BoardSize):
        Soldiers.append([allPossiblePositions[i], np.random.randint(1, 4)])
    return Soldiers


def WhiteHorseMovement(BoardSize=8):
    Soldiers2Output = Soldiers2(BoardSize)
    Soldiers2Pos = []
    for i in Soldiers2Output:
        Soldiers2Pos.append(i[0])
    possRow = range(1, BoardSize + 1)
    possCol = range(1, BoardSize + 1)
    allPossiblePositions = []
    for i in possRow:
        for j in possCol:
            if [i, j] not in Soldiers2Pos:
                allPossiblePositions.append([i, j])
    random.shuffle(allPossiblePositions)
    WhiteHorse = []
    for i in range(2 * BoardSize):
        WhiteHorse.append(allPossiblePositions[i])
    return WhiteHorse


def unpack_soldiers_info(soldiers_info, board_size):
    soldiers_position = []
    soldiers_point = {}
    for sol in soldiers_info:
        revised_sol_point = (sol[0][0] - board_size / 2 - 1, sol[0][1] - board_size / 2 - 1)
        soldiers_position.append([sol[0][0] - board_size / 2 - 1, sol[0][1] - board_size / 2 - 1])
        soldiers_point[revised_sol_point] = (sol[1], False)
    return soldiers_position, soldiers_point


def raw_soldiers_pos(soldiers_info):
    raw_soldiers_position = []
    for sol in soldiers_info:
        raw_soldiers_position.append([sol[0][0], sol[0][1]])
    return raw_soldiers_position


def unpack_queens_info(queens_info, board_size):
    queens_position = []
    for que in queens_info:
        queens_position.append([que[0] - board_size / 2 - 1, que[1] - board_size / 2 - 1])
    return queens_position


if __name__ == "__main__":
    print(Soldiers1(9))
    print(Soldiers2(9))
    print(WhiteHorseMovement(9))
