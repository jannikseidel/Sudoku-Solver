# script for solving sudokus, entered in a 9x9 Matrix
################################################################################
#
#   ToDo:   Checken ob eine Zelle so geblockt wird dass eindeutig bestimmbar ist
#           welche Zahl eingesetz werden kann
#
################################################################################
import numpy as np

sudoku = np.matrix([[2,3,1,0,0,5,9,0,0],[0,4,9,0,0,0,6,2,0],[0,0,0,0,1,0,0,0,3],[9,0,0,5,3,0,0,7,0],[0,0,8,9,7,4,1,0,0],[1,5,0,0,0,6,0,0,9],[7,0,0,0,6,0,0,0,0],[6,1,0,0,0,2,8,5,0],[0,0,2,1,0,0,0,9,6]])

matrix_1_1 = np.matrix([[sudoku[0,0],sudoku[0,1],sudoku[0,2]],[sudoku[1,0],sudoku[1,1],sudoku[1,2]],[sudoku[2,0],sudoku[2,1],sudoku[2,2]]])
matrix_1_2 = np.matrix([[sudoku[0,3],sudoku[0,4],sudoku[0,5]],[sudoku[1,3],sudoku[1,4],sudoku[1,5]],[sudoku[2,3],sudoku[2,4],sudoku[2,5]]])
matrix_1_3 = np.matrix([[sudoku[0,6],sudoku[0,7],sudoku[0,8]],[sudoku[1,6],sudoku[1,7],sudoku[1,8]],[sudoku[2,6],sudoku[2,7],sudoku[2,8]]])
matrix_2_1 = np.matrix([[sudoku[3,0],sudoku[3,1],sudoku[3,2]],[sudoku[4,0],sudoku[4,1],sudoku[4,2]],[sudoku[5,0],sudoku[5,1],sudoku[5,2]]])
matrix_2_2 = np.matrix([[sudoku[3,3],sudoku[3,4],sudoku[3,5]],[sudoku[4,3],sudoku[4,4],sudoku[4,5]],[sudoku[5,3],sudoku[5,4],sudoku[5,5]]])
matrix_2_3 = np.matrix([[sudoku[3,6],sudoku[3,7],sudoku[3,8]],[sudoku[4,6],sudoku[4,7],sudoku[4,8]],[sudoku[5,6],sudoku[5,7],sudoku[5,8]]])
matrix_3_1 = np.matrix([[sudoku[6,0],sudoku[6,1],sudoku[6,2]],[sudoku[7,0],sudoku[7,1],sudoku[7,2]],[sudoku[8,0],sudoku[8,1],sudoku[8,2]]])
matrix_3_2 = np.matrix([[sudoku[6,3],sudoku[6,4],sudoku[6,5]],[sudoku[7,3],sudoku[7,4],sudoku[7,5]],[sudoku[8,3],sudoku[8,4],sudoku[8,5]]])
matrix_3_3 = np.matrix([[sudoku[6,6],sudoku[6,7],sudoku[6,8]],[sudoku[7,6],sudoku[7,7],sudoku[7,8]],[sudoku[8,6],sudoku[8,7],sudoku[8,8]]])
# VERWENDE STRINGS UM DAS GANZE EFFIZIENTER UND SCHNELLER ZU MACHEN!!!

def solver_3x3(matrix):
    ''' Returns either a solved matrix if only one number is missing or
        'more than one' if more than one position is 0
    '''
    empty = 0
    pos_0_x = 0
    pos_0_y = 0

    pos_1 = False
    pos_2 = False
    pos_3 = False
    pos_4 = False
    pos_5 = False
    pos_6 = False
    pos_7 = False
    pos_8 = False
    pos_9 = False

    # find the position of missing number or quit if more than one number missing
    for x in range(0,3):
        for y in range(0,3):
            value = matrix[x,y]
            if value == 0:
                empty += 1
                if empty > 1:
                    return 'more than one'
                pos_0_x = x
                pos_0_y = y
            elif value == 1:
                pos_1 = True
            elif value == 2:
                pos_2 = True
            elif value == 3:
                pos_3 = True
            elif value == 4:
                pos_4 = True
            elif value == 5:
                pos_5 = True
            elif value == 5:
                pos_5 = True
            elif value == 6:
                pos_6 = True
            elif value == 7:
                pos_7 = True
            elif value == 8:
                pos_8 = True
            elif value == 9:
                pos_9 = True
            else:
                pass

    if not pos_1:
        matrix[pos_0_x,pos_0_y] = 1
    elif not pos_2:
        matrix[pos_0_x,pos_0_y] = 2
    elif not pos_3:
        matrix[pos_0_x,pos_0_y] = 3
    elif not pos_4:
        matrix[pos_0_x,pos_0_y] = 4
    elif not pos_5:
        matrix[pos_0_x,pos_0_y] = 5
    elif not pos_6:
        matrix[pos_0_x,pos_0_y] = 6
    elif not pos_7:
        matrix[pos_0_x,pos_0_y] = 7
    elif not pos_8:
        matrix[pos_0_x,pos_0_y] = 8
    elif not pos_9:
        matrix[pos_0_x,pos_0_y] = 9

    return matrix

# Initializing counter for zeros
count_zero = 1

while count_zero > 0:
    # setting counter to zero
    count_zero = 0

    # concatinating the numbers in each coloumn to a string
    coloumn_1 = str(sudoku[0,0]) + str(sudoku[1,0]) + str(sudoku[2,0]) + str(sudoku[3,0]) + str(sudoku[4,0]) + str(sudoku[5,0]) + str(sudoku[6,0]) + str(sudoku[7,0]) + str(sudoku[8,0])
    coloumn_2 = str(sudoku[0,1]) + str(sudoku[1,1]) + str(sudoku[2,1]) + str(sudoku[3,1]) + str(sudoku[4,1]) + str(sudoku[5,1]) + str(sudoku[6,1]) + str(sudoku[7,1]) + str(sudoku[8,1])
    coloumn_3 = str(sudoku[0,2]) + str(sudoku[1,2]) + str(sudoku[2,2]) + str(sudoku[3,2]) + str(sudoku[4,2]) + str(sudoku[5,2]) + str(sudoku[6,2]) + str(sudoku[7,2]) + str(sudoku[8,2])
    coloumn_4 = str(sudoku[0,3]) + str(sudoku[1,3]) + str(sudoku[2,3]) + str(sudoku[3,3]) + str(sudoku[4,3]) + str(sudoku[5,3]) + str(sudoku[6,3]) + str(sudoku[7,3]) + str(sudoku[8,3])
    coloumn_5 = str(sudoku[0,4]) + str(sudoku[1,4]) + str(sudoku[2,4]) + str(sudoku[3,4]) + str(sudoku[4,4]) + str(sudoku[5,4]) + str(sudoku[6,4]) + str(sudoku[7,4]) + str(sudoku[8,4])
    coloumn_6 = str(sudoku[0,5]) + str(sudoku[1,5]) + str(sudoku[2,5]) + str(sudoku[3,5]) + str(sudoku[4,5]) + str(sudoku[5,5]) + str(sudoku[6,5]) + str(sudoku[7,5]) + str(sudoku[8,5])
    coloumn_7 = str(sudoku[0,6]) + str(sudoku[1,6]) + str(sudoku[2,6]) + str(sudoku[3,6]) + str(sudoku[4,6]) + str(sudoku[5,6]) + str(sudoku[6,6]) + str(sudoku[7,6]) + str(sudoku[8,6])
    coloumn_8 = str(sudoku[0,7]) + str(sudoku[1,7]) + str(sudoku[2,7]) + str(sudoku[3,7]) + str(sudoku[4,7]) + str(sudoku[5,7]) + str(sudoku[6,7]) + str(sudoku[7,7]) + str(sudoku[8,7])
    coloumn_9 = str(sudoku[0,8]) + str(sudoku[1,8]) + str(sudoku[2,8]) + str(sudoku[3,8]) + str(sudoku[4,8]) + str(sudoku[5,8]) + str(sudoku[6,8]) + str(sudoku[7,8]) + str(sudoku[8,8])

    coloumns = {'coloumn_1':coloumn_1, 'coloumn_2':coloumn_2 , 'coloumn_3':coloumn_3,'coloumn_4':coloumn_4, 'coloumn_5':coloumn_5, 'coloumn_6':coloumn_6,'coloumn_7':coloumn_7, 'coloumn_8':coloumn_8, 'coloumn_9':coloumn_9}
    rows = {'row_1': row_1, 'row_2': row_2, 'row_3': row_3,'row_4': row_4, 'row_5': row_5, 'row_6': row_6, 'row_7': row_7, 'row_8': row_8, 'row_9': row_9}

    # concatinating the numbers in each row to a string
    row_1 = str(sudoku[0,0]) + str(sudoku[0,1]) + str(sudoku[0,2]) + str(sudoku[0,3]) + str(sudoku[0,4]) + str(sudoku[0,5]) + str(sudoku[0,6]) + str(sudoku[0,7]) + str(sudoku[0,8])
    row_2 = str(sudoku[1,0]) + str(sudoku[1,1]) + str(sudoku[1,2]) + str(sudoku[1,3]) + str(sudoku[1,4]) + str(sudoku[1,5]) + str(sudoku[1,6]) + str(sudoku[1,7]) + str(sudoku[1,8])
    row_3 = str(sudoku[2,0]) + str(sudoku[2,1]) + str(sudoku[2,2]) + str(sudoku[2,3]) + str(sudoku[2,4]) + str(sudoku[2,5]) + str(sudoku[2,6]) + str(sudoku[2,7]) + str(sudoku[2,8])
    row_4 = str(sudoku[3,0]) + str(sudoku[3,1]) + str(sudoku[3,2]) + str(sudoku[3,3]) + str(sudoku[3,4]) + str(sudoku[3,5]) + str(sudoku[3,6]) + str(sudoku[3,7]) + str(sudoku[3,8])
    row_5 = str(sudoku[4,0]) + str(sudoku[4,1]) + str(sudoku[4,2]) + str(sudoku[4,3]) + str(sudoku[4,4]) + str(sudoku[4,5]) + str(sudoku[4,6]) + str(sudoku[4,7]) + str(sudoku[4,8])
    row_6 = str(sudoku[5,0]) + str(sudoku[5,1]) + str(sudoku[5,2]) + str(sudoku[5,3]) + str(sudoku[5,4]) + str(sudoku[5,5]) + str(sudoku[5,6]) + str(sudoku[5,7]) + str(sudoku[5,8])
    row_7 = str(sudoku[6,0]) + str(sudoku[6,1]) + str(sudoku[6,2]) + str(sudoku[6,3]) + str(sudoku[6,4]) + str(sudoku[6,5]) + str(sudoku[6,6]) + str(sudoku[6,7]) + str(sudoku[6,8])
    row_8 = str(sudoku[7,0]) + str(sudoku[7,1]) + str(sudoku[7,2]) + str(sudoku[7,3]) + str(sudoku[7,4]) + str(sudoku[7,5]) + str(sudoku[7,6]) + str(sudoku[7,7]) + str(sudoku[7,8])
    row_9 = str(sudoku[8,0]) + str(sudoku[8,1]) + str(sudoku[8,2]) + str(sudoku[8,3]) + str(sudoku[8,4]) + str(sudoku[8,5]) + str(sudoku[8,6]) + str(sudoku[8,7]) + str(sudoku[8,8])

    coloumn_names = ['coloumn_1', 'coloumn_2', 'coloumn_3','coloumn_4', 'coloumn_5', 'coloumn_6','coloumn_7', 'coloumn_8', 'coloumn_9']
    row_names = ['row_1', 'row_2', 'row_3','row_4', 'row_5', 'row_6','row_7', 'row_8', 'row_9']

    # looking for a single missing number in the coloumns

    for coloumn in coloumn_names:
        zeros = coloumns[coloumn].count('0')
        if zeros == 1:
            position_0 = coloumns[coloumn].find('0')
            sudoku_col = int(coloumn[-1])-1
            if '1' not in coloumn:
                sudoku[position_0,sudoku_col] = 1
            elif '2' not in coloumn:
                sudoku[position_0,sudoku_col] = 2
            elif '3' not in coloumn:
                sudoku[position_0,sudoku_col] = 3
            elif '4' not in coloumn:
                sudoku[position_0,sudoku_col] = 4
            elif '5' not in coloumn:
                sudoku[position_0,sudoku_col] = 5
            elif '6' not in coloumn:
                sudoku[position_0,sudoku_col] = 6
            elif '7' not in coloumn:
                sudoku[position_0,sudoku_col] = 7
            elif '8' not in coloumn:
                sudoku[position_0,sudoku_col] = 8
            elif '9' not in coloumn:
                sudoku[position_0,sudoku_col] = 9
        else:
            pass

    # looking for a single missing number in the rows

    for row in row_names:
        zeros = rows[row].count('0')
        print(zeros)
        if zeros == 1:
            position_0 = rows[rows].find('0')
            sudoku_row = int(row[-1])-1
            if '1' not in row:
                sudoku[sudoku_row, position_0] = 1
            elif '2' not in row:
                sudoku[sudoku_row, position_0] = 2
            elif '3' not in row:
                sudoku[sudoku_row, position_0] = 3
            elif '4' not in row:
                sudoku[sudoku_row, position_0] = 4
            elif '5' not in row:
                sudoku[sudoku_row, position_0] = 5
            elif '6' not in row:
                sudoku[sudoku_row, position_0] = 6
            elif '7' not in row:
                sudoku[sudoku_row, position_0] = 7
            elif '8' not in row:
                sudoku[sudoku_row, position_0] = 8
            elif '9' not in row:
                sudoku[sudoku_row, position_0] = 9
        else:
            pass


    break












    # counting the zeros in the matrix
    count_zero = coloumn_1.count('0') + coloumn_2.count('0') + coloumn_3.count('0') + coloumn_4.count('0') + coloumn_5.count('0') + coloumn_6.count('0') + coloumn_7.count('0') + coloumn_8.count('0') + coloumn_9.count('0')
