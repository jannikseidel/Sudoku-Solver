# script for solving sudokus, entered in a 9x9 Matrix
################################################################################
#
################################################################################
import numpy as np


def sudoku_opener():
    # inserting the sudoku in commaseperated txt, empty fields as 0s, each row in a
    # seperate line of the txt file
    in_file = open("sudoku.txt", "r")
    line_name = ["line_1","line_2","line_3","line_4","line_5","line_6","line_7","line_8","line_9",]
    count = 0
    line_dict = {}
    for line in in_file:
        line = line.strip().split(",")
        count_line = 0
        for n in line:
            line[count_line] = int(n)
            count_line += 1
        line_dict[line_name[count]] = line
        count += 1

    sudoku = np.array([line_dict['line_1'],line_dict['line_2'],line_dict['line_3'],line_dict['line_4'],line_dict['line_5'],line_dict['line_6'],line_dict['line_7'],line_dict['line_8'],line_dict['line_9']])
    return sudoku

def get_lines(sudoku):
    count_line = 0
    dict_line = {}
    for line in sudoku:
        line = str(line)
        line = line.strip("[]").split(" ")
        line = list(filter(lambda a: a != '0', line))
        dict_line[str(count_line)] = line
        count_line +=1
    return dict_line

def get_coloumns(sudoku):
    dict_coloumns = {}
    for col in range(0,9):
        coloumn = []
        for row in range(0,9):
            coloumn.append(str(sudoku[row, col]))
        coloumn = list(filter(lambda a: a != '0', coloumn))
        dict_coloumns[str(col)] = coloumn
    return dict_coloumns

def get_matrices(sudoku):
    # getting 3x3 submatrices from the sudoku and returning them as a dictionary
    # the positions of the matrices are encoded in the keys
    # 'matrix_rowpos1.rowpos2.rowpos3,colpos1.colpos2.colpos3'
    dict_matrix = {}
    for line in range(0,9,3):
        line_coord_1 = line
        line_coord_2 = line + 1
        line_coord_3 = line + 2
        for coloumn in range(0,9,3):
            coloumn_coord_1 = coloumn
            coloumn_coord_2 = coloumn + 1
            coloumn_coord_3 = coloumn + 2
            matrix = np.array([[str(sudoku[line_coord_1,coloumn_coord_1]),str(sudoku[line_coord_1,coloumn_coord_2]),str(sudoku[line_coord_1,coloumn_coord_3])],[str(sudoku[line_coord_2,coloumn_coord_1]),str(sudoku[line_coord_2,coloumn_coord_2]),str(sudoku[line_coord_2,coloumn_coord_3])],[str(sudoku[line_coord_3,coloumn_coord_1]),str(sudoku[line_coord_3,coloumn_coord_2]),str(sudoku[line_coord_3,coloumn_coord_3])]])
            name = "matrix_"+str(line_coord_1)+"."+str(line_coord_2)+"."+str(line_coord_3)+","+ str(coloumn_coord_1) + '.' + str(coloumn_coord_2) + '.' + str(coloumn_coord_3)
            dict_matrix[name] = matrix
    return dict_matrix

def missing_lines(lines):
    # input as a dictionary with numbers in the lines and outpout as a dictionary
    # with the missing numbers per line
    dict_mis_lines = {}
    for line in lines:
        line_set = set(lines[line])
        numbers = set(['1','2','3','4','5','6','7','8','9'])
        dict_mis_lines[line] = numbers - line_set
    return dict_mis_lines

def missing_coloumns(coloumns):
    # takes a dictionary with the numbers in each coloumn and returns a
    # dictionary with the missing numbers per coloumn

    dict_mis_coloumns = {}
    for coloumn in coloumns:
        coloumn_set = set(coloumns[coloumn])
        numbers = set(['1','2','3','4','5','6','7','8','9'])
        dict_mis_coloumns[coloumn] = numbers - coloumn_set
    return dict_mis_coloumns

def missing_matrix(matrices):
    # taking all submatrices as input and returning a list of missing numbers
    # per matrix as output
    dict_mis_matrices = {}
    numbers = set(['1','2','3','4','5','6','7','8','9'])
    for matrix in matrices:
            matrix_list1 = list(matrices[matrix][0])
            matrix_list2 = list(matrices[matrix][1])
            matrix_list3 = list(matrices[matrix][2])
            matrix_set = set(matrix_list1+matrix_list2+matrix_list3)
            matrix_set = numbers - matrix_set
            dict_mis_matrices[matrix] = matrix_set
    return dict_mis_matrices

def position_zeros(sudoku):
    # returning the position of all empty entries in the sudoku as {name:[line_number, col_number]}
    dict_zeros = {}
    count_line = 0
    for line in sudoku:
        #counting zero entries
        num_zeros = str(line).count("0")
        # converting line to string with only numbers
        string = str(line).strip("[]").replace(" ",'')
        # finding first 0 in line
        pos_zero = string.find("0")

        while pos_zero != -1:
            # defining the key for the dict_zero
            name = str(count_line)+ "_" + str(pos_zero)
            dict_zeros[name] = [count_line,pos_zero]
            pos_zero = string.find("0",pos_zero+1)
        count_line += 1
    return dict_zeros

def eval_zeros_intersection(sudoku,mis_line,mis_col,mis_matrices,lines, coloumns, dict_pos):
    # evaluating the zero entries and entering a missing number if its bijective
    pos_keys = dict_pos.keys()
    mis_pos = {}
    for key in pos_keys:
        # getting the position of the zeros in the sudoku
        position = dict_pos[key]
        matrix = mis_matrices.keys()
        for mat_key in matrix:
            matrix_name = mat_key[mat_key.find("_")+1:]
            matrix_pos = {}
            matrix_name_new = matrix_name.split(',')
            # checking if position of line is in matrix_name
            if str(position[0]) in matrix_name_new[0] and str(position[1]) in matrix_name_new[1]:
                line_pos = matrix_name_new[0].split(".")
                col_pos = matrix_name_new[1].split(".")
                matrix_pos["line"] = line_pos
                matrix_pos["coloumn"] = col_pos
                break
        # evaluating if a number is the only one acceptable at a position
        # 1. getting the intersection of missing in line and coloumn and matrix
        #
        if matrix_pos:
            # determining missing numbers at position
            missing_line = mis_line[str(position[0])]
            missing_col = mis_col[str(position[1])]
            missing_mat = mis_matrices[mat_key]
            intersect_line_col_mat = missing_line & missing_col & missing_mat
            inter_len = len(list(intersect_line_col_mat))
            # preparing the mis_pos dictionary for returning the position and
            # the missing values at this position
            mis_pos[key]= list(intersect_line_col_mat)
            if inter_len == 1:
                sudoku[position[0], position[1]] = int(intersect_line_col_mat.pop())

        lines = get_lines(sudoku)
        coloumns = get_coloumns(sudoku)
        matrices = get_matrices(sudoku)
        mis_line = missing_lines(lines)
        mis_col = missing_coloumns(coloumns)
        mis_matrices = missing_matrix(matrices)
        dict_pos = position_zeros(sudoku)

    return sudoku, mis_pos

def eval_zeros_all_others(sudoku,dict_pos,mis_pos,lines,coloumns,matrices):
    # function for evaluating if the numbers missing at a position are already
    # taken in all other coloumns and lines sourrounding the position
    pos_keys = dict_pos.keys()
    print("ALL OTHERS IS EVALUATED!")
    for key in pos_keys:
        # getting the position of the zeros in the sudoku
        position = dict_pos[key]
        matrix = matrices.keys()

        matrix

        for mat_key in matrix:
            matrix_name = mat_key[mat_key.find("_")+1:]
            later_matrix_name = mat_key
            matrix_pos = {}
            matrix_name_new = matrix_name.split(',')
            # checking if position of line is in matrix_name
            if str(position[0]) in matrix_name_new[0] and str(position[1]) in matrix_name_new[1]:
                line_pos = matrix_name_new[0].split(".")
                col_pos = matrix_name_new[1].split(".")
                matrix_pos["line"] = line_pos
                matrix_pos["coloumn"] = col_pos
                later_matrix_name = mat_key
                break
        missing_numbers = mis_pos[key]
        eval_position = []
        for number in missing_numbers:
            matrix = matrices[later_matrix_name]
            # determining the position in the submatrix

            line_pos = matrix_name_new[0].replace(".","")
            col_pos = matrix_name_new[1].replace(".","")
            sub_mat_pos = [line_pos.find(str(position[0])),col_pos.find(str(position[1]))]

            if sub_mat_pos[0] == 0:
                    sub_line1 = str(matrix[line_pos.find(line_pos[1])]).strip("[]").replace('\'','')
                    sub_line2 = str(matrix[line_pos.find(line_pos[2])]).strip("[]").replace('\'','')
                    sub_line3 = str(matrix[line_pos.find(line_pos[0])]).strip("[]").replace('\'','')
                    sub_line1 = sub_line1.replace(' ','')
                    sub_line2 = sub_line2.replace(' ','')
                    sub_line3 = sub_line3.replace(' ','')
            elif sub_mat_pos[0] == 1:
                    sub_line1 = str(matrix[line_pos.find(line_pos[0])]).strip("[]").replace('\'','')
                    sub_line2 = str(matrix[line_pos.find(line_pos[2])]).strip("[]").replace('\'','')
                    sub_line3 = str(matrix[line_pos.find(line_pos[1])]).strip("[]").replace('\'','')
                    sub_line1 = sub_line1.replace(' ','')
                    sub_line2 = sub_line2.replace(' ','')
                    sub_line3 = sub_line3.replace(' ','')
            elif sub_mat_pos[0] == 2:
                    sub_line1 = str(matrix[line_pos.find(line_pos[0])]).strip("[]").replace('\'','')
                    sub_line2 = str(matrix[line_pos.find(line_pos[1])]).strip("[]").replace('\'','')
                    sub_line3 = str(matrix[line_pos.find(line_pos[2])]).strip("[]").replace('\'','')
                    sub_line1 = sub_line1.replace(' ','')
                    sub_line2 = sub_line2.replace(' ','')
                    sub_line3 = sub_line3.replace(' ','')

            if sub_mat_pos[1] == 0:
                subcol1 = ""
                subcol2 = ""
                subcol3 = ""
                for i in range(0,3):
                    subcol1 += matrix[i,1]
                    subcol2 += matrix[i,2]
                    subcol3 += matrix[i,0]
            elif sub_mat_pos[1] == 1:
                subcol1 = ""
                subcol2 = ""
                subcol3 = ""
                for i in range(0,3):
                    subcol1 += matrix[i,0]
                    subcol2 += matrix[i,2]
                    subcol3 += matrix[i,1]
            elif sub_mat_pos[1] == 2:
                subcol1 = ""
                subcol2 = ""
                subcol3 = ""
                for i in range(0,3):
                    subcol1 += matrix[i,0]
                    subcol2 += matrix[i,1]
                    subcol3 += matrix[i,2]

            # positions of the sourrounding lines and coloumns
            line_pos = matrix_pos["line"]

            if str(position[0]) in line_pos:
                line_pos.remove(str(position[0]))
            col_pos = matrix_pos["coloumn"]
            if str(position[1]) in col_pos:
                col_pos.remove(str(position[1]))

            # getting the whole lines and coloumns
            line1 = lines[line_pos[0]]
            line2 = lines[line_pos[1]]
            line3 = lines[str(position[0])]
            coloumn1 = coloumns[col_pos[0]]
            coloumn2 = coloumns[col_pos[1]]
            coloumn3 = coloumns[str(position[1])]

            # each position in the submatrix is checked for possible solutions

            if sub_mat_pos[0] == 0 and sub_mat_pos[1] == 0:
                if number in line1 and number in line2 and number in coloumn1 and number in coloumn2 and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 1")
                    print(position)
                elif subcol3.count("0") == 1 and number in coloumn1 and number in coloumn2 and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 2")
                    print(position)
                elif sub_line3[1] != '0' and sub_line3[2] != '0' and number in line1 and number in line2 and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 3")
                    print(position)
                elif sub_line2.count('0') == 0 and number in line1 and number in coloumn1 and number in coloumn2 and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 4")
                    print(position)
                elif sub_line1.count("0") == 0 and number in line2 and number in coloumn1 and number in coloummn2 and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 5")
                    print(position)
                elif subcol1.count('0') == 0 and number in coloumn2 and number in line1 and number in line2 and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 6")
                    print(position)
                elif subcol2.count('0') == 0 and number in coloumn1 and number in line1 and number in line2 and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 7")
                    print(position)
                elif subcol3[1] != '0' and number in coloumn1 and number in coloumn2 and number in line2 and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 8")
                elif sub_line3[1] != '0' and number in coloumn2 and number in line1 and number in line2 and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 9")
                    print(position)
                elif subcol3[2] != '0' and number in coloumn1 and number in line1 and number in line2 and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 10")
                    print(position)
                elif subcol3[2] != '0' and number in line1 and number in coloumn1 and number in coloumn2 and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 11")
                    print(position)
                elif sub_line2.count("0") == 0 and sub_line3[1] != '0' and sub_line3[2] != '0' and number in line1 and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 12")
                    print(position)

            elif sub_mat_pos[0] == 0 and sub_mat_pos[1] == 1:
                if number in line1 and number in line2 and number in coloumn1 and number in coloumn2 and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 13")
                    print(position)
                elif number in line1 and number in line2 and number in coloumn2 and sub_line3[1] != "0" and number not in line3 and number not in coloumn3:
                     sudoku[position[0], position[1]] = int(number)
                     print("WORKED! 14")
                     print(position)
                elif number in coloumn1 and number in coloumn2 and sub_line2[0] != '0' and sub_line2[2] != '0' and number in line1 and number not in line3 and number not in coloumn3:
                     sudoku[position[0], position[1]] = int(number)
                     print("WORKED! 15")
                     print(position)
                elif sub_line3[2] != '0' and number in coloumn1 and number in line1 and number in line2 and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 16")
                    print(position)
                elif number in line1 and number in line2 and sub_line3[0] is not "0" and sub_line3[2] is not '0' and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 17")
                    print(position)
                elif number in coloumn1 and number in coloumn2 and number in line2 and sub_line1[1] != "0" and number not in line3 and number not in coloumn3:
                     sudoku[position[0], position[1]] = int(number)
                     print("WORKED! 18")
                     print(position)
                elif sub_mat_pos[0] == 0 and sub_mat_pos[1] == 1 and sub_line3[0] != '0' and number in coloumn2 and number in line1 and number in line2 and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 19")
                    print(position)

                pass
            elif sub_mat_pos[0] == 0 and sub_mat_pos[1] == 2:
                if number in line1 and number in line2 and number in coloumn1 and number in coloumn2 and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 20")
                    print(position)
                elif number in line1 and number in line2 and sub_line3.count('0') == 1 and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 21")
                    print(position)
                elif subcol3[1] != "0" and number in line2 and number in coloumn1 and number in coloumn2 and number not in coloumn3 and number not in line3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 22")
                    print(position)
                elif subcol2.count('0') == 0 and subcol3.count('0') == 1 and number in coloumn1 and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 22a")
                    print(position)
                elif subcol1.count('0') == 0 and subcol3.count("0") == 1 and number in coloumn2 and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 22b")
                    print(position)
                pass
            elif sub_mat_pos[0] == 1 and sub_mat_pos[1] == 0:
                if number in line1 and number in line2 and number in coloumn1 and number in coloumn2 and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 23")
                    print(position)
                elif sub_line2.count("0") == 0 and sub_line3.count('0') == 1 and number in line1 and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 24")
                    print(position)


                pass
            elif sub_mat_pos[0] == 1 and sub_mat_pos[1] == 1:
                if number in line1 and number in line2 and number in coloumn1 and number in coloumn2 and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 25")
                    print(position)
                elif number in coloumn1 and number in coloumn2 and sub_line1[1] != '0' and sub_line2[1] != '0' and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 26")
                    print(position)
                elif number in line1 and number in line2 and sub_line3[0] is not "0" and sub_line3[2] is not '0' and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 27")
                    print(position)
                elif number in line1 and number in coloumn1 and number in coloumn2 and sub_line2[1] != '0' and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 27a")
                    print(position)
                elif number in line2 and number in coloumn1 and number in coloumn2 and sub_line1[1] != '0' and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 27b")
                    print(position)
                elif number in line1 and number in line2 and number in coloumn1 and subcol2[1] !="0" and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 27c")
                    print(position)
                elif number in line1 and number in line2 and number in coloumn2 and subcol1[1] != '0' and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 27d")
                    print(position)

                pass
            elif sub_mat_pos[0] == 1 and sub_mat_pos[1] == 2:
                if number in line1 and number in line2 and number in coloumn1 and number in coloumn2 and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 28")
                    print(position)
                elif sub_line3[0] != '0'  and number in line1 and number in line2 and number in coloumn2 and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 29")
                    print(position)
                elif number in line1 and number in line2 and number in coloumn1 and sub_line3[1] != "0" and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 30")
                    print(position)
                elif sub_line2.count("0") == 0 and sub_line3.count('0') == 1 and number in line1 and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 31")
                    print(position)
                elif number in line1 and number in line2 and number in coloumn1 and number in coloumn2 and number not in coloumn3 and number not in line3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 32")
                    print(position)
                pass
            elif sub_mat_pos[0] == 2 and sub_mat_pos[1] == 0:
                if number in line1 and number in line2 and number in coloumn1 and number in coloumn2 and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 33")
                    print(position)
                elif subcol2.count("0") == 0 and number in coloumn1 and subcol3.count('0') == 1 and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 34")
                    print(position)
                elif number in line1 and number in line2 and number in coloumn2 and sub_line3[1] != '0' and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 34a")
                    print(position)
                elif number in line1 and number in line2 and number in coloumn1 and sub_line3[2] != '0' and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 34b")
                    print(position)
                elif number in coloumn1 and number in coloumn2 and number in line1 and subcol3[1] != '0' and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 34c")
                    print(position)
                elif number in coloumn1 and number in coloumn2 and number in line2 and subcol3[0]!= '0' and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 34d")
                    print(position)
                elif number in line1 and number in line2 and sub_line3.count('0') == 1 and number not in line3 :
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 35a")
                    print(position)
                elif number in coloumn1 and number in coloumn2 and subcol3.count('0') == 1 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 35b")
                    print(position)
                pass
            elif sub_mat_pos[0] == 2 and sub_mat_pos[1] == 1:
                if number in line1 and number in line2 and number in coloumn1 and number in coloumn2 and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 35")
                    print(position)
                elif number in coloumn1 and number in coloumn2 and subcol3[0] != '0' and number in line2 and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 36")
                    print(position)
                elif number in coloumn1 and number in coloumn2 and subcol3[1] != '0' and number in line1 and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 36a")
                    print(position)
                elif number in line1 and number in line2 and sub_line3[0] != "0" and number in coloumn2 and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 37")
                    print(position)
                elif number in line1 and number in line2 and number in coloumn1 and number in coloumn2 and number not in coloumn3 and number not in line3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 36")
                    print(position)
                elif sub_line3[2] != "0" and number in coloumn1 and number in line1 and number in line2 and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 37")
                    print(position)
                elif number in line1 and number in line2 and int(sub_line3[0]) is not 0 and int(sub_line3[2]) is not 0 and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 38")
                    print(position)
                elif number in coloumn1 and number in coloumn2 and number in line2 and sub_line2[1] != "0" and number not in line3 and number not in coloumn3:
                     sudoku[position[0], position[1]] = int(number)
                     print("WORKED! 39")
                     print(position)
                pass
            elif sub_mat_pos[0] == 2 and sub_mat_pos[1] == 2:
                if number in line1 and number in line2 and number in coloumn1 and number in coloumn2 and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 40")
                    print(position)
                elif sub_line3[1] != "0" and number in coloumn1 and number in line1 and number in line2 and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 41")
                    print(position)
                elif number in coloumn1 and number in coloumn2 and subcol3[0] != "0" and subcol3[1] != "0" and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 42")
                    print(position)
                elif number in line2 and number in coloumn2 and sub_line3.count("0") == 1 and sub_line1[0] != "0" and sub_line1[2] != "0" and number not in line3 and number not in coloumn3:
                    sudoku[position[0], position[1]] = int(number)
                    print("WORKED! 43")
                    print(position)
                pass




            if sub_line1.count('0') == 0 and number in line2 and number in coloumn1 and number in coloumn2 and ((number not in coloumn3) and (number not in line3)):
                sudoku[position[0], position[1]] = int(number)
                print("WORKED! 44")
                print(position)
            elif sub_line2.count('0') == 0 and number in line1 and number in coloumn1 and number in coloumn2 and ((number not in coloumn3) and (number not in line3)):
                sudoku[position[0], position[1]] = int(number)
                print("WORKED! 45")
                print(position)
            elif subcol1.count('0') == 0 and number in line1 and number in line2 and number in coloumn2 and ((number not in coloumn3) and (number not in line3)):
                sudoku[position[0], position[1]] = int(number)
                print("WORKED! 46")
                print(position)
            elif subcol2.count('0') == 0 and number in line1 and number in line2 and number in coloumn1 and ((number not in coloumn3) and (number not in line3)):
                sudoku[position[0], position[1]] = int(number)
                print("WORKED! 47")
                print(position)
            elif subcol1.count('0') == 0 and number in line1 and number in line2 and number in coloumn2 and ((number not in coloumn3) and (number not in line3)):
                sudoku[position[0], position[1]] = int(number)
                print("WORKED! 48")
                print(position)

            elif subcol1.count("0") == 0 and subcol2.count("0") == 0 and sub_line1.count('0') == 0 and sub_line2.count("0") == 0 and ((number not in coloumn3) and (number not in line3)):
                sudoku[position[0], position[1]] = int(number)
                print("WORKED! 49")
                print(position)
                # evaluate if only one is missing in line or coloumn and
                # all others are blocked for this number

                #######################################################
                # MACHT FEHLER! LOGIK NICHT EINEINDEUTIG???? HIER LIEGT DAS PROBLEM ... Faelle eindeutig beschreiben!
                #######################################################
            elif (subcol3.count("0") == 1 and number in line1 and number in line2 and number not in line3 and number not in coloumn3) and (number in coloumn1 and number in coloumn2):
                sudoku[position[0], position[1]] = int(number)
                print("WORKED! 50")
                print(position)

            elif sub_line3.count("0") == 1 and number in coloumn1 and number in coloumn2 and number not in line3 and number not in coloumn3 and (number in line1 and number in line2):
                sudoku[position[0], position[1]] = int(number)
                print("WORKED! 51")
                print(position)

            elif sub_mat_pos[0] == 0 and sub_mat_pos[1] == 0 and subcol3[2] != "0" and number in coloumn1 and number in coloumn2 and number in line1:
                sudoku[position[0], position[1]] = int(number)
                print("WORKED! 52")
                print(position)

            lines = get_lines(sudoku)
            coloumns = get_coloumns(sudoku)
            matrices = get_matrices(sudoku)
            mis_line = missing_lines(lines)
            mis_col = missing_coloumns(coloumns)
            mis_matrices = missing_matrix(matrices)
            dict_pos = position_zeros(sudoku)



    return sudoku


sudoku = sudoku_opener()


mis_pos
sudoku

count_zeros = 0
for line in sudoku:
    line = str(line).strip("[]")
    count_zeros += line.count("0")
    print(count_zeros)

zeros = 0
while count_zeros != 0:
    count_zeros = 0
    for line in sudoku:
        line = str(line).strip("[]")
        count_zeros += line.count("0")

    print("new round")
    print(count_zeros)
    lines = get_lines(sudoku)
    coloumns = get_coloumns(sudoku)
    matrices = get_matrices(sudoku)
    mis_line = missing_lines(lines)
    mis_col = missing_coloumns(coloumns)
    mis_matrices = missing_matrix(matrices)
    dict_pos = position_zeros(sudoku)
    sudoku, mis_pos = eval_zeros_intersection(sudoku,mis_line,mis_col,mis_matrices, lines, coloumns, dict_pos)
    if zeros == count_zeros:
        lines = get_lines(sudoku)
        coloumns = get_coloumns(sudoku)
        matrices = get_matrices(sudoku)
        mis_line = missing_lines(lines)
        mis_col = missing_coloumns(coloumns)
        mis_matrices = missing_matrix(matrices)
        dict_pos = position_zeros(sudoku)
        sudoku = eval_zeros_all_others(sudoku,dict_pos,mis_pos,lines,coloumns, matrices)
    zeros = count_zeros
    print(sudoku)

sudoku
save = open("sudoku_solved.txt","w")
for line in sudoku:
    save.write(str(line).strip("[]"))
    save.write("\n")
save.close()
