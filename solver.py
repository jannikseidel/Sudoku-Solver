# script for solving sudokus, entered in a 9x9 Matrix
################################################################################
#
################################################################################
import numpy as np
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
    print(line)
    line_dict[line_name[count]] = line
    count += 1

line_dict
sudoku = np.matrix([line_dict['line_1'],line_dict['line_2'],line_dict['line_3'],line_dict['line_4'],line_dict['line_5'],line_dict['line_6'],line_dict['line_7'],line_dict['line_8'],line_dict['line_9']])
sudoku
def find_empty(sudoku):
    # finding the position of each empty field in the sudoku
    # {name:[x_position, y_position]}
    count_line = 0
    dict_pos = {}
    dict_pos_name = []
    for line in sudoku:
        line = str(line).strip("[]").replace(" ","")
        count_zeros = line.count("0")
        pos_0 = 0
        for zero in range(count_zeros):
            pos_0 = line.find("0",pos_0)
            dict_pos[str(count_line) + "_" + str(zero+1)] = [count_line,pos_0]
            dict_pos_name.append(str(count_line) + "_" + str(zero+1))
            pos_0 += 1
        count_line += 1
    return dict_pos, dict_pos_name

def find_how_many_empty_in_line(sudoku):
    # returns a dictionary stating how many empty cells are there per line
    count_line = 0
    dict_line_num = {}
    for line in sudoku:
        line = str(line).strip("[]").replace(" ","")
        count_zeros = line.count("0")
        dict_line_num[str(count_line)]= count_zeros
        count_line += 1
    return dict_line_num

def row_missing(sudoku):
    row_names = ['0', '1', '2','3', '4', '5','6', '7', '8']
    rows = {}
    row_missing = {}

    # for loop over the rows extracting the numbers as strings and getting the
    # set of missing numbers per row

    for row_num in range(0,9):
        row = ''
        for row_pos in range(0,9):
             row = row + str(sudoku[row_num, row_pos]) + " "
        row = row[: -1]
        set_nums = set(['1','2','3','4','5','6','7','8','9'])
        row = row.split()
        row_set = set(row)
        rows[row_names[row_num]] = row
        row_missing[row_names[row_num]] =  set_nums - row_set

    return rows,row_missing,row_names

def coloumn_missing(sudoku):
    coloumns = {}
    col_missing = {}
    coloumn_names = ['0', '1', '2','3', '4', '5','6', '7', '8']

    # for loop over the coloumns extracting the numbers as strings and
    # extracting the missing numbers as sets
    for col_num in range(0,9):
        coloumn = ''
        for col_pos in range(0,9):
             coloumn = coloumn + str(sudoku[col_pos, col_num]) +' '
        coloumn = coloumn[:-1]
        coloumn = coloumn.split(" ")
        col_set = set(coloumn)
        set_nums = set(['1','2','3','4','5','6','7','8','9'])
        col_missing[coloumn_names[col_num]] = set_nums - col_set
        coloumns[coloumn_names[col_num]] = coloumn
    return coloumns, col_missing, coloumn_names

# dictionary mit missing intersection row coloumn erstellen
def intersection_row_col(dict_pos,row_mis,col_mis, dict_pos_name):
    inter_mis_pos = {}
    for name in dict_pos_name:
        x,y = dict_pos[name]
        missing_in_row = row_mis[str(x)]
        missing_in_coloumn = col_mis[str(y)]
        inter_mis = missing_in_row.intersection(missing_in_coloumn)
        inter_mis_pos[name] = inter_mis
    return inter_mis_pos

def submatrices(sudoku):
    matrix_names = ['matrix_1_1', 'matrix_1_2', 'matrix_1_3', 'matrix_2_1', 'matrix_2_2', 'matrix_2_3', 'matrix_3_1', 'matrix_3_2', 'matrix_3_3']
    matrices = {}

    # giving the corresponding row and coloumn numbers to the submatrices in
    # following order "row1row2row3,coloumn1coloumn2coloumn3"
    matrices_pos = {}


    # sorting the sudoku in 3x3 submatrices


    for matrix in matrix_names:
            if matrix[-3] == '1' and matrix[-1] == '1':
                matrix_slice = np.matrix([[sudoku[0,0],sudoku[0,1],sudoku[0,2]],[sudoku[1,0],sudoku[1,1],sudoku[1,2]],[sudoku[2,0],sudoku[2,1],sudoku[2,2]]])
                matrices[matrix] = matrix_slice
                matrices_pos[matrix] = "012,012"
            elif matrix[-3] == '1' and matrix[-1] == '2':
                matrix_slice = np.matrix([[sudoku[0,3],sudoku[0,4],sudoku[0,5]],[sudoku[1,3],sudoku[1,4],sudoku[1,5]],[sudoku[2,3],sudoku[2,4],sudoku[2,5]]])
                matrices[matrix] = matrix_slice
                matrices_pos[matrix] = "012,345"
            elif matrix[-3] == '1' and matrix[-1] == '3':
                matrix_slice = np.matrix([[sudoku[0,6],sudoku[0,7],sudoku[0,8]],[sudoku[1,6],sudoku[1,7],sudoku[1,8]],[sudoku[2,6],sudoku[2,7],sudoku[2,8]]])
                matrices[matrix] = matrix_slice
                matrices_pos[matrix] = "012,678"
            elif matrix[-3] == '2' and matrix[-1] == '1':
                matrix_slice = np.matrix([[sudoku[3,0],sudoku[3,1],sudoku[3,2]],[sudoku[4,0],sudoku[4,1],sudoku[4,2]],[sudoku[5,0],sudoku[5,1],sudoku[5,2]]])
                matrices[matrix] = matrix_slice
                matrices_pos[matrix] = "345,012"
            elif matrix[-3] == '2' and matrix[-1] == '2':
                matrix_slice = np.matrix([[sudoku[3,3],sudoku[3,4],sudoku[3,5]],[sudoku[4,3],sudoku[4,4],sudoku[4,5]],[sudoku[5,3],sudoku[5,4],sudoku[5,5]]])
                matrices[matrix] = matrix_slice
                matrices_pos[matrix] = "345,345"
            elif matrix[-3] == '2' and matrix[-1] == '3':
                matrix_slice = np.matrix([[sudoku[3,6],sudoku[3,7],sudoku[3,8]],[sudoku[4,6],sudoku[4,7],sudoku[4,8]],[sudoku[5,6],sudoku[5,7],sudoku[5,8]]])
                matrices[matrix] = matrix_slice
                matrices_pos[matrix] = "345,678"
            elif matrix[-3] == '3' and matrix[-1] == '1':
                matrix_slice = np.matrix([[sudoku[6,0],sudoku[6,1],sudoku[6,2]],[sudoku[7,0],sudoku[7,1],sudoku[7,2]],[sudoku[8,0],sudoku[8,1],sudoku[8,2]]])
                matrices[matrix] = matrix_slice
                matrices_pos[matrix] = "678,012"
            elif matrix[-3] == '3' and matrix[-1] == '2':
                matrix_slice = np.matrix([[sudoku[6,3],sudoku[6,4],sudoku[6,5]],[sudoku[7,3],sudoku[7,4],sudoku[7,5]],[sudoku[8,3],sudoku[8,4],sudoku[8,5]]])
                matrices[matrix] = matrix_slice
                matrices_pos[matrix] = "678,345"
            elif matrix[-3] == '3' and matrix[-1] == '3':
                matrix_slice = np.matrix([[sudoku[6,6],sudoku[6,7],sudoku[6,8]],[sudoku[7,6],sudoku[7,7],sudoku[7,8]],[sudoku[8,6],sudoku[8,7],sudoku[8,8]]])
                matrices[matrix] = matrix_slice
                matrices_pos[matrix] = "678,678"

    return matrices, matrices_pos


def int_mis_submat(matrices,matrices_pos,dict_pos,dict_pos_name, inter_mis_pos,sudoku):

    # solving the sudoku by calculating the intersection between missing numbers
    # at the positions and in the submatrices or, if only on solution at a
    # position is possible inserting this one at the position

    keys_mat = list(matrices.keys())
    # itterating over the submatrices
    for key in keys_mat:
        numbers = str(matrices[key]).replace("[","").replace("]","").replace("\n","").split()
        matrix_pos = matrices_pos[key].split(",")

        # calculating the set of numbers which are in one sub_matrix
        for pos in dict_pos_name:
            position = dict_pos[pos]
            if str(position[0]) in matrix_pos[0] and str(position[1]) in matrix_pos[1]:
                print(position[0] , matrix_pos[0], position[1], matrix_pos[1])
                numbers_set = set()
                for number in numbers:
                    numbers_set.add(str(number))
                # set of possible numbers
                set_nums = set(['1','2','3','4','5','6','7','8','9'])
                # set of missing numbers in matrix
                mis_numbers = set_nums.difference(numbers_set)
                print("Numbers in Matrix")
                print(numbers_set)
                print("missing numbers")
                print(mis_numbers)
                print("missing numbers at position")
                print(inter_mis_pos[pos])
                # intersection between missing numbers at the position and in the matrix
                inter_mat_row_col = inter_mis_pos[pos].intersection(mis_numbers)
                print(inter_mat_row_col)
                inter_mat_row_col = list(inter_mat_row_col)
                position_missing = list(inter_mis_pos[pos])

                if len(inter_mat_row_col) == 1 :
                    print("before")
                    print(sudoku[position[0],position[1]])
                    sudoku[position[0],position[1]] = int(inter_mat_row_col.pop())
                    print("after")
                    print(sudoku[position[0],position[1]])
                elif len(position_missing) == 1:
                    print("before position")
                    print(sudoku[position[0],position[1]])
                    sudoku[position[0],position[1]] = int(position_missing.pop())
                    print("after position")


    return sudoku


count_zeros = 0
for line in sudoku:
    line = str(line).strip("[]")
    count_zeros += line.count("0")
    print(count_zeros)

while count_zeros != 0:
    count_zeros = 0
    for line in sudoku:
        line = str(line).strip("[]")
        count_zeros += line.count("0")
    print("new round")
    print(count_zeros)

    dict_pos, dict_pos_name = find_empty(sudoku)
    dict_line_num = find_how_many_empty_in_line(sudoku)

    rows,row_mis,row_names = row_missing(sudoku)
    coloumns, col_mis, col_names = coloumn_missing(sudoku)

    matrices, matrices_pos = submatrices(sudoku)

    inter_mis_pos = intersection_row_col(dict_pos,row_mis, col_mis,dict_pos_name)
    sudoku = int_mis_submat(matrices,matrices_pos, dict_pos, dict_pos_name, inter_mis_pos, sudoku)


save = open("sudoku_solved.txt","w")
for line in sudoku:
    save.write(str(line).strip("[]"))
    save.write("\n")
save.close()
