import genetic_solution_q1 as ga
import board as bo

if __name__ == '__main__':
    board_size = 20
    board = bo.board(board_size)
    ga.EA1(board, laambda=100, mio=20, Pc=0.8, Pm=0.05)
