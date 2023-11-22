def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def prepare_dic(dic, letter):
    for key in dic:
        nl = []
        for element in sorted(dic[key]):
            nl.append((element, letter))
        dic[key] = nl
    return dic


def combine_two_dic(dic1, dic2):
    dic1_keys_list = dic1.keys()
    dic2_keys_list = dic2.keys()
    combined_keys = []
    for el1 in dic1_keys_list:
        combined_keys.append(el1)
    for el2 in dic2_keys_list:
        if el2 not in combined_keys:
            combined_keys.append(el2)
    combined_dic = {}
    for key in combined_keys:
        if key in dic1_keys_list and key not in dic2_keys_list:
            combined_dic[key] = dic1[key]
        if key in dic2_keys_list and key not in dic1_keys_list:
            combined_dic[key] = dic2[key]
        if key in dic2_keys_list and key in dic1_keys_list:
            combined_dic[key] = sorted(
                dic1[key] + dic2[key],
                key=lambda x: x[0]
            )
        if key not in dic2_keys_list and key not in dic1_keys_list:
            print("shouldnt get here")
    return combined_dic


def crashes(position, board_size, letter):
    vertical_crash = []
    horizontal_crash = []
    diagonal_crash = []
    up_left_corner = (board_size / 2 - 1, -board_size / 2)
    up_right_corner = (board_size / 2 - 1, board_size / 2 - 1)
    vertical_crash_dic = {}
    horizontal_crash_dic = {}
    diagonal_crash_dic_dl = {}
    diagonal_crash_dic_ur = {}
    for i in range(0, len(position)):
        # check queens collision
        for j in range(i + 1, len(position)):

            if position[i][1] == position[j][1]:
                vertical_crash.append([position[i], position[j]])
                if position[i][1] not in vertical_crash_dic:
                    vertical_crash_dic[position[i][1]] = [position[i][0]]
                    vertical_crash_dic[position[i][1]].append(position[j][0])
                else:
                    if position[i][0] not in vertical_crash_dic[position[i][1]]:
                        vertical_crash_dic[position[i][1]].append(position[i][0])
                    if position[j][0] not in vertical_crash_dic[position[i][1]]:
                        vertical_crash_dic[position[i][1]].append(position[j][0])

            if position[i][0] == position[j][0]:
                horizontal_crash.append([position[i], position[j]])
                if position[i][0] not in horizontal_crash_dic:
                    horizontal_crash_dic[position[i][0]] = [position[i][1]]
                    horizontal_crash_dic[position[i][0]].append(position[j][1])
                else:
                    if position[i][1] not in horizontal_crash_dic[position[i][0]]:
                        horizontal_crash_dic[position[i][0]].append(position[i][1])
                    if position[j][1] not in horizontal_crash_dic[position[i][0]]:
                        horizontal_crash_dic[position[i][0]].append(position[j][1])

            if position[i][0] - position[j][0] == position[i][1] - position[j][1]:
                diagonal_crash.append([position[i], position[j]])
                ur_diagonal_line_number = manhattan(up_left_corner[0], up_left_corner[1], position[i][0],
                                                    position[i][1])
                if ur_diagonal_line_number not in diagonal_crash_dic_ur:
                    diagonal_crash_dic_ur[ur_diagonal_line_number] = [position[i][1]]
                    diagonal_crash_dic_ur[ur_diagonal_line_number].append(position[j][1])
                else:
                    if position[i][1] not in diagonal_crash_dic_ur[ur_diagonal_line_number]:
                        diagonal_crash_dic_ur[ur_diagonal_line_number].append(position[i][1])
                    if position[j][1] not in diagonal_crash_dic_ur[ur_diagonal_line_number]:
                        diagonal_crash_dic_ur[ur_diagonal_line_number].append(position[j][1])

            if position[i][0] - position[j][0] == -(position[i][1] - position[j][1]):
                diagonal_crash.append([position[i], position[j]])
                dl_diagonal_line_number = manhattan(up_right_corner[0], up_right_corner[1], position[i][0],
                                                    position[i][1])
                if dl_diagonal_line_number not in diagonal_crash_dic_dl:
                    diagonal_crash_dic_dl[dl_diagonal_line_number] = [position[i][1]]
                    diagonal_crash_dic_dl[dl_diagonal_line_number].append(position[j][1])
                else:
                    if position[i][1] not in diagonal_crash_dic_dl[dl_diagonal_line_number]:
                        diagonal_crash_dic_dl[dl_diagonal_line_number].append(position[i][1])
                    if position[j][1] not in diagonal_crash_dic_dl[dl_diagonal_line_number]:
                        diagonal_crash_dic_dl[dl_diagonal_line_number].append(position[j][1])
    print(vertical_crash_dic)
    return (prepare_dic(horizontal_crash_dic, letter), prepare_dic(vertical_crash_dic, letter),
            prepare_dic(diagonal_crash_dic_ur, letter), prepare_dic(diagonal_crash_dic_dl, letter))
    # print("horizontal_crash: " + str(horizontal_crash))
    # print("vertical_crash: " + str(vertical_crash))
    # print("diagonal_crash: " + str(diagonal_crash))
    # print("=============================================================")
    # print("horizontal_crash_dic: " + str(horizontal_crash_dic))
    # print("vertical_crash_dic: " + str(vertical_crash_dic))
    # print("diagonal_crash_dic_ur: " + str(diagonal_crash_dic_ur))
    # print("diagonal_crash_dic_dl: " + str(diagonal_crash_dic_dl))


def crashes1(position, board_size, letter):
    up_left_corner = (board_size / 2 - 1, -board_size / 2)
    up_right_corner = (board_size / 2 - 1, board_size / 2 - 1)
    vertical_allign_dic = {}
    horizontal_allign_dic = {}
    diagonal_allign_dic_dl = {}
    diagonal_allign_dic_ur = {}
    for i in range(0, len(position)):
        for j in range(int(-board_size / 2), int(board_size / 2)):
            if position[i][1] == j:
                if position[i][1] not in vertical_allign_dic:
                    vertical_allign_dic[j] = [position[i][0]]
                else:
                    vertical_allign_dic[j].append(position[i][0])

    for i in range(0, len(position)):
        for j in range(int(-board_size / 2), int(board_size / 2)):
            if position[i][0] == j:
                if position[i][0] not in horizontal_allign_dic:
                    horizontal_allign_dic[j] = [position[i][1]]
                else:
                    horizontal_allign_dic[j].append(position[i][1])

    for i in range(0, len(position)):
        ur_diagonal_line_number = manhattan(up_left_corner[0], up_left_corner[1], position[i][0],
                                            position[i][1])
        for j in range(board_size*2-1):
            if ur_diagonal_line_number == j:
                if ur_diagonal_line_number not in diagonal_allign_dic_ur:
                    diagonal_allign_dic_ur[j] = [position[i][1]]
                else:
                    diagonal_allign_dic_ur[j].append(position[i][1])

    for i in range(0, len(position)):
        dl_diagonal_line_number = manhattan(up_right_corner[0], up_right_corner[1], position[i][0],
                                            position[i][1])
        for j in range(board_size*2-1):
            if dl_diagonal_line_number == j:
                if dl_diagonal_line_number not in diagonal_allign_dic_dl:
                    diagonal_allign_dic_dl[j] = [position[i][1]]
                else:
                    diagonal_allign_dic_dl[j].append(position[i][1])

    return (prepare_dic(horizontal_allign_dic, letter), prepare_dic(vertical_allign_dic, letter),
            prepare_dic(diagonal_allign_dic_ur, letter), prepare_dic(diagonal_allign_dic_dl, letter))
