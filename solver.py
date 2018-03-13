# script for solving sudokus, entered in a 9x9 Matrix
################################################################################
#
#   ToDo:   Checken ob eine Zelle so geblockt wird dass eindeutig bestimmbar ist
#           welche Zahl eingesetz werden kann
#
################################################################################
import numpy as np

sudoku = np.matrix([[2,3,1,0,0,5,9,0,0],[0,4,9,0,0,0,6,2,0],[0,0,0,0,1,0,0,0,3],[9,0,0,5,3,0,0,7,0],[0,0,8,9,7,4,1,0,0],[1,5,0,0,0,6,0,0,9],[7,0,0,0,6,0,0,0,0],[6,1,0,0,0,2,8,5,0],[0,0,2,1,0,0,0,9,6]])


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


def intersectio_mis_submat(matrices,matrices_pos,dict_pos,dict_pos_name, inter_mis_pos):
    keys_mat = list(matrices.keys())
    # itterating over the submatrices
    for key in keys_mat:
        numbers = str(matrices[key]).replace("[","").replace("]","").replace("\n","").split()
        matrix_pos = matrices_pos[key].split(",")
        for pos in dict_pos_name:
            position = dict_pos[pos]
            if str(position[0]) in matrix_pos[0] and str(position[1]) in matrix_pos[1]:
                numbers_set = set()
                for number in numbers:
                    numbers_set.add(int(number))
                inter_mat_row_col = inter_mis_pos[pos].intersection(numbers_set)
                inter_mat_row_col = list(inter_mat_row_col)
                if len(inter_mat_row_col) == 1:
                    sudoku[dict_pos[pos][1],dict_pos[pos][0]] = inter_mat_row_col[0]


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
    print(count_zeros)

    dict_pos, dict_pos_name = find_empty(sudoku)
    dict_line_num = find_how_many_empty_in_line(sudoku)

    rows,row_mis,row_names = row_missing(sudoku)
    coloumns, col_mis, col_names = coloumn_missing(sudoku)

    matrices, matrices_pos = submatrices(sudoku)

    inter_mis_pos = intersection_row_col(dict_pos,row_mis, col_mis,dict_pos_name)
    intersectio_mis_submat(matrices,matrices_pos, dict_pos, dict_pos_name, inter_mis_pos)

#------------------------------------------------------------------------------#
# Wie bekomme ich es hin die "Constraints" klar zu machen?!



##################################################################
# filling in the last missing numbers in the lines of the sudoku #
##################################################################
for line in dict_line_num:
    if dict_line_num[line] == 1:
        line_sudoku = str(sudoku[int(line)]).strip("[]")
        set_nums_line = set(line_sudoku.replace("0","").split())
        set_nums = set(['1','2','3','4','5','6','7','8','9'])
        missing_num = set_nums - set_nums_line
        missing_num = int(missing_num.pop())
        line_sudoku = line_sudoku.replace(" ","")
        pos_0 = line_sudoku.find("0")
        sudoku[int(line),pos_0] = missing_num


print(sudoku)

# Initializing counter for zeros
zeros = 1

while zeros > 0:
    # setting counter to zero
    zeros = 0


    row_names = ['row_1', 'row_2', 'row_3','row_4', 'row_5', 'row_6','row_7', 'row_8', 'row_9']
    rows = {}

    # for loop over the rows extracting the numbers as strings and counting the
    # 0s in them

    for row_num in range(0,9):
        row = ''
        for row_pos in range(0,9):
             row = row + str(sudoku[row_num, row_pos])
        zeros = zeros + row.count('0')
        row = row.replace('0','')
        print(row)
        rows[row_names[row_num]] = row

    # Matrixes are ordered in the following way: Matrix_row_coloumn, the sudoku matrix is composed of 3x3 submatrices


    # looking for a single missing number in the coloumns and adding if only
    # one is missing

    for coloumn_name in coloumn_names:
        coloumn = coloumns[coloumn_name]
        if len(coloumn) == 8:
            value = 0
            if '1' not in coloumn:
                value = 1
            elif '2' not in coloumn:
                value = 2
            elif '3' not in coloumn:
                value = 3
            elif '4' not in coloumn:
                value = 4
            elif '5' not in coloumn:
                value = 5
            elif '6' not in coloumn:
                value = 6
            elif '7' not in coloumn:
                value = 7
            elif '8' not in coloumn:
                value = 8
            elif '9' not in coloumn:
                value = 9

            col_num = coloumn_name[-1]

            if col_num == '1':
                row_position = 0
                col_values = ''
                for position in range(0,8):
                    col_values += str(sudoku[postion ,0])
                row_position = col_values.find('0')
                sudoku[row_position, 0] = 1
            elif col_num == '2':
                row_position = 0
                col_values = ''
                for position in range(0,8):
                    col_values += str(sudoku[postion ,1])
                row_position = col_values.find('0')
                sudoku[row_position, 1] = 2
            elif col_num == '3':
                row_position = 0
                col_values = ''
                for position in range(0,8):
                    col_values += str(sudoku[postion ,2])
                row_position = col_values.find('0')
                sudoku[row_position, 2] = 3
            elif col_num == '4':
                row_position = 0
                col_values = ''
                for position in range(0,8):
                    col_values += str(sudoku[postion ,3])
                row_position = col_values.find('0')
                sudoku[row_position, 3] = 4
            elif col_num == '5':
                row_position = 0
                col_values = ''
                for position in range(0,8):
                    col_values += str(sudoku[postion ,4])
                row_position = col_values.find('0')
                sudoku[row_position, 4] = 5
            elif col_num == '6':
                row_position = 0
                col_values = ''
                for position in range(0,8):
                    col_values += str(sudoku[postion ,5])
                row_position = col_values.find('0')
                sudoku[row_position, 5] = 6
            elif col_num == '7':
                row_position = 0
                col_values = ''
                for position in range(0,8):
                    col_values += str(sudoku[postion ,6])
                row_position = col_values.find('0')
                sudoku[row_position, 6] = 7
            elif col_num == '8':
                row_position = 0
                col_values = ''
                for position in range(0,8):
                    col_values += str(sudoku[postion ,7])
                row_position = col_values.find('0')
                sudoku[row_position, 7] = 8
            elif col_num == '9':
                row_position = 0
                col_values = ''
                for position in range(0,8):
                    col_values += str(sudoku[postion ,8])
                row_position = col_values.find('0')
                sudoku[row_position, 8] = 9

    # looking for a single missing number in the rows and adding if only
    # one is missing

    for row_name in row_names:
        row = rows[row_name]
        if len(row) == 8:
            value = 0
            if '1' not in row:
                value = 1
            elif '2' not in row:
                value = 2
            elif '3' not in row:
                value = 3
            elif '4' not in row:
                value = 4
            elif '5' not in row:
                value = 5
            elif '6' not in row:
                value = 6
            elif '7' not in row:
                value = 7
            elif '8' not in row:
                value = 8
            elif '9' not in row:
                value = 9

            row_num = row_name[-1]

            if row_num == '1':
                col_position = 0
                row_values = ''
                for position in range(0,8):
                    row_values += str(sudoku[0,postion])
                col_position = row_values.find('0')
                sudoku[0, col_position] = 1
            elif row_num == '2':
                col_position = 0
                row_values = ''
                for position in range(0,8):
                    row_values += str(sudoku[1,postion])
                col_position = row_values.find('0')
                sudoku[1, col_position] = 2
            elif col_num == '3':
                col_position = 0
                row_values = ''
                for position in range(0,8):
                    row_values += str(sudoku[2,postion])
                col_position = row_values.find('0')
                sudoku[2, col_position] = 3
            elif col_num == '4':
                col_position = 0
                row_values = ''
                for position in range(0,8):
                    row_values += str(sudoku[3,postion])
                col_position = row_values.find('0')
                sudoku[3, col_position] = 4
            elif col_num == '5':
                col_position = 0
                row_values = ''
                for position in range(0,8):
                    row_values += str(sudoku[4,postion])
                col_position = row_values.find('0')
                sudoku[4, col_position] = 5
            elif col_num == '6':
                col_position = 0
                row_values = ''
                for position in range(0,8):
                    row_values += str(sudoku[5,postion])
                col_position = row_values.find('0')
                sudoku[5, col_position] = 6
            elif col_num == '7':
                col_position = 0
                row_values = ''
                for position in range(0,8):
                    row_values += str(sudoku[6,postion])
                col_position = row_values.find('0')
                sudoku[6, col_position] = 7
            elif col_num == '8':
                col_position = 0
                row_values = ''
                for position in range(0,8):
                    row_values += str(sudoku[7,postion])
                col_position = row_values.find('0')
                sudoku[7, col_position] = 8
            elif col_num == '9':
                col_position = 0
                row_values = ''
                for position in range(0,8):
                    row_values += str(sudoku[8,postion])
                col_position = row_values.find('0')
                sudoku[8, col_position] = 9

    # check which numbers are missing in the submatrices

    for matrix in matrix_names:
        sub_matrix = matrices[matrix]
        numbers_in_matrix = ''

        for line in sub_matrix:
            numbers_in_matrix = numbers_in_matrix + str(line).strip('[]')
        positions_matrix = numbers_in_matrix
        numbers_in_matrix = numbers_in_matrix.replace('0','')
        numbers_in_matrix = numbers_in_matrix.replace(' ','')



        print(numbers_in_matrix)


    break
