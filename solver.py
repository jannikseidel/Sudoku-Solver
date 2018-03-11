# script for solving sudokus, entered in a 9x9 Matrix
################################################################################
#
#   ToDo:   Checken ob eine Zelle so geblockt wird dass eindeutig bestimmbar ist
#           welche Zahl eingesetz werden kann
#
################################################################################
import numpy as np

sudoku = np.matrix([[2,3,1,0,0,5,9,0,0],[0,4,9,0,0,0,6,2,0],[0,0,0,0,1,0,0,0,3],[9,0,0,5,3,0,0,7,0],[0,0,8,9,7,4,1,0,0],[1,5,0,0,0,6,0,0,9],[7,0,0,0,6,0,0,0,0],[6,1,0,0,0,2,8,5,0],[0,0,2,1,0,0,0,9,6]])


# Initializing counter for zeros
zeros = 1

while zeros > 0:
    # setting counter to zero
    zeros = 0

    coloumns = {}
    coloumn_names = ['coloumn_1', 'coloumn_2', 'coloumn_3','coloumn_4', 'coloumn_5', 'coloumn_6','coloumn_7', 'coloumn_8', 'coloumn_9']

    # for loop over the coloumns extracting the numbers as strings
    for col_num in range(0,9):
        coloumn = ''
        for col_pos in range(0,9):
             coloumn = coloumn + str(sudoku[col_pos, col_num])

        coloumns[coloumn_names[col_num]] = coloumn

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
    matrix_names = ['matrix_1_1', 'matrix_1_2', 'matrix_1_3', 'matrix_2_1', 'matrix_2_2', 'matrix_2_3', 'matrix_3_1', 'matrix_3_2', 'matrix_3_3']
    matrices = {}

    for matrix in matrix_names:
            if matrix[-3] == '1' and matrix[-1] == '1':
                matrix_slice = np.matrix([[sudoku[0,0],sudoku[0,1],sudoku[0,2]],[sudoku[1,0],sudoku[1,1],sudoku[1,2]],[sudoku[2,0],sudoku[2,1],sudoku[2,2]]])
                matrices[matrix] = matrix_slice
            elif matrix[-3] == '1' and matrix[-1] == '2':
                matrix_slice = np.matrix([[sudoku[0,3],sudoku[0,4],sudoku[0,5]],[sudoku[1,3],sudoku[1,4],sudoku[1,5]],[sudoku[2,3],sudoku[2,4],sudoku[2,5]]])
                matrices[matrix] = matrix_slice
            elif matrix[-3] == '1' and matrix[-1] == '3':
                matrix_slice = np.matrix([[sudoku[0,6],sudoku[0,7],sudoku[0,8]],[sudoku[1,6],sudoku[1,7],sudoku[1,8]],[sudoku[2,6],sudoku[2,7],sudoku[2,8]]])
                matrices[matrix] = matrix_slice
            elif matrix[-3] == '2' and matrix[-1] == '1':
                matrix_slice = np.matrix([[sudoku[3,0],sudoku[3,1],sudoku[3,2]],[sudoku[4,0],sudoku[4,1],sudoku[4,2]],[sudoku[5,0],sudoku[5,1],sudoku[5,2]]])
                matrices[matrix] = matrix_slice
            elif matrix[-3] == '2' and matrix[-1] == '2':
                matrix_slice = np.matrix([[sudoku[3,3],sudoku[3,4],sudoku[3,5]],[sudoku[4,3],sudoku[4,4],sudoku[4,5]],[sudoku[5,3],sudoku[5,4],sudoku[5,5]]])
                matrices[matrix] = matrix_slice
            elif matrix[-3] == '2' and matrix[-1] == '3':
                matrix_slice = np.matrix([[sudoku[3,6],sudoku[3,7],sudoku[3,8]],[sudoku[4,6],sudoku[4,7],sudoku[4,8]],[sudoku[5,6],sudoku[5,7],sudoku[5,8]]])
                matrices[matrix] = matrix_slice
            elif matrix[-3] == '3' and matrix[-1] == '1':
                matrix_slice = np.matrix([[sudoku[6,0],sudoku[6,1],sudoku[6,2]],[sudoku[7,0],sudoku[7,1],sudoku[7,2]],[sudoku[8,0],sudoku[8,1],sudoku[8,2]]])
                matrices[matrix] = matrix_slice
            elif matrix[-3] == '3' and matrix[-1] == '2':
                matrix_slice = np.matrix([[sudoku[6,3],sudoku[6,4],sudoku[6,5]],[sudoku[7,3],sudoku[7,4],sudoku[7,5]],[sudoku[8,3],sudoku[8,4],sudoku[8,5]]])
                matrices[matrix] = matrix_slice
            elif matrix[-3] == '3' and matrix[-1] == '3':
                matrix_slice = np.matrix([[sudoku[6,6],sudoku[6,7],sudoku[6,8]],[sudoku[7,6],sudoku[7,7],sudoku[7,8]],[sudoku[8,6],sudoku[8,7],sudoku[8,8]]])
                matrices[matrix] = matrix_slice

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

    # check if a submatrix is missing a single number, if yes enter this in the
    # sudoku matrix

    for matrix in matrix_names:
        sub_matrix = matrices[matrix]
        numbers_in_matrix = ''

        for line in sub_matrix:
            numbers_in_matrix = numbers_in_matrix + str(line).strip('[]')

        numbers_in_matrix = numbers_in_matrix.replace('0','')
        numbers_in_matrix = numbers_in_matrix.replace(' ','')
        print(numbers_in_matrix)


    break
