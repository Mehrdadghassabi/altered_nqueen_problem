import crash as cr
import DataGen as dg


def fitness(board, queens_position):
    board_size = board.boardSize
    soldiers_info = board.soldiers_info
    up_left_corner = (board_size / 2 - 1, -board_size / 2)
    up_right_corner = (board_size / 2 - 1, board_size / 2 - 1)
    soldiers_position, soldiers_point = dg.unpack_soldiers_info(soldiers_info, board_size)

    v_horizontal_crash_dic, v_vertical_crash_dic, v_diagonal_crash_dic_ur, v_diagonal_crash_dic_dl = cr.crashes1(
        queens_position,
        board_size, "V")

    s_horizontal_crash_dic, s_vertical_crash_dic, s_diagonal_crash_dic_ur, s_diagonal_crash_dic_dl = cr.crashes1(
        soldiers_position,
        board_size, "S")

    vertical_crash = cr.combine_two_dic(s_vertical_crash_dic, v_vertical_crash_dic)
    horizontal_crash = cr.combine_two_dic(s_horizontal_crash_dic, v_horizontal_crash_dic)
    ur_diagonal_crash = cr.combine_two_dic(s_diagonal_crash_dic_ur, v_diagonal_crash_dic_ur)
    dl_diagonal_crash = cr.combine_two_dic(s_diagonal_crash_dic_dl, v_diagonal_crash_dic_dl)

    fitness = 0
    for i in range(len(list(vertical_crash.keys()))):
        for j in range(len(vertical_crash[list(vertical_crash.keys())[i]]) - 1):
            vc = vertical_crash[list(vertical_crash.keys())[i]][j]
            vc_next = vertical_crash[list(vertical_crash.keys())[i]][j + 1]
            y = list(vertical_crash.keys())[i]
            if vc[1] == "S" and vc_next[1] == "S":
                continue
                # print("nothing gonna happen")
            if vc[1] == "S" and vc_next[1] == "V":
                x = vc[0]
                soldiers_point[(x, y)] = (soldiers_point[(x, y)][0], True)
                # print("(x,y): " + str((x, y)))
                # print("SV threat")
            if vc[1] == "V" and vc_next[1] == "S":
                x = vc_next[0]
                soldiers_point[(x, y)] = (soldiers_point[(x, y)][0], True)
                # print("(x,y): " + str((x, y)))
                # print("SV threat")
            if vc[1] == "V" and vc_next[1] == "V":
                fitness -= 2
                # print("VV threat")

    for i in range(len(list(horizontal_crash.keys()))):
        for j in range(len(horizontal_crash[list(horizontal_crash.keys())[i]]) - 1):
            hc = horizontal_crash[list(horizontal_crash.keys())[i]][j]
            hc_next = horizontal_crash[list(horizontal_crash.keys())[i]][j + 1]
            x = list(horizontal_crash.keys())[i]
            if hc[1] == "S" and hc_next[1] == "S":
                continue
                # print("nothing gonna happen")
            if hc[1] == "S" and hc_next[1] == "V":
                y = hc[0]
                soldiers_point[(x, y)] = (soldiers_point[(x, y)][0], True)
                # print("(x,y): " + str((x, y)))
                # print("SV threat")
            if hc[1] == "V" and hc_next[1] == "S":
                y = hc_next[0]
                soldiers_point[(x, y)] = (soldiers_point[(x, y)][0], True)
                # print("(x,y): " + str((x, y)))
                # print("SV threat")
            if hc[1] == "V" and hc_next[1] == "V":
                fitness -= 2
                # print("VV threat")

    for i in range(len(list(ur_diagonal_crash.keys()))):
        for j in range(len(ur_diagonal_crash[list(ur_diagonal_crash.keys())[i]]) - 1):
            udc = ur_diagonal_crash[list(ur_diagonal_crash.keys())[i]][j]
            udc_next = ur_diagonal_crash[list(ur_diagonal_crash.keys())[i]][j + 1]
            diagonal_num = list(ur_diagonal_crash.keys())[i]
            if udc[1] == "S" and udc_next[1] == "S":
                continue
                # print("nothing gonna happen")
            if udc[1] == "S" and udc_next[1] == "V":
                y = udc[0]
                x = (up_left_corner[0] + y) - (up_left_corner[1] + diagonal_num)
                soldiers_point[(x, y)] = (soldiers_point[(x, y)][0], True)
                # print("(x,y): " + str((x, y)))
                # print("SV threat")
            if udc[1] == "V" and udc_next[1] == "S":
                y = udc_next[0]
                x = (up_left_corner[0] + y) - (up_left_corner[1] + diagonal_num)
                soldiers_point[(x, y)] = (soldiers_point[(x, y)][0], True)
                # print("(x,y): " + str((x, y)))
                # print("SV threat")
            if udc[1] == "V" and udc_next[1] == "V":
                fitness -= 2
                # print("VV threat")

    for i in range(len(list(dl_diagonal_crash.keys()))):
        for j in range(len(dl_diagonal_crash[list(dl_diagonal_crash.keys())[i]]) - 1):
            ddc = dl_diagonal_crash[list(dl_diagonal_crash.keys())[i]][j]
            ddc_next = dl_diagonal_crash[list(dl_diagonal_crash.keys())[i]][j + 1]
            diagonal_num = list(dl_diagonal_crash.keys())[i]

            if ddc[1] == "S" and ddc_next[1] == "S":
                continue
                # print("nothing gonna happen")
            if ddc[1] == "S" and ddc_next[1] == "V":
                y = ddc[0]
                x = (up_right_corner[0] + up_right_corner[1]) - (y + diagonal_num)
                soldiers_point[(x, y)] = (soldiers_point[(x, y)][0], True)
                # print("(x,y): " + str((x, y)))
                # print("SV threat")
            if ddc[1] == "V" and ddc_next[1] == "S":
                y = ddc_next[0]
                x = (up_right_corner[0] + up_right_corner[1]) - (y + diagonal_num)
                soldiers_point[(x, y)] = (soldiers_point[(x, y)][0], True)
                # print("(x,y): " + str((x, y)))
                # print("SV threat")
            if ddc[1] == "V" and ddc_next[1] == "V":
                fitness -= 2
                # print("VV threat")
    for val in soldiers_point.values():
        if val[1]:
            fitness += val[0]
    return fitness
