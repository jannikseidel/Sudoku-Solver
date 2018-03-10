# script for solving sudokus, entered in a 9x9 Matrix
import numpy as np

sudoku = np.matrix([[2,3,1,0,0,5,9,0,0],[0,4,9,0,0,0,6,2,0],[0,0,0,0,1,0,0,0,3],[9,0,0,5,3,0,0,7,0],[0,0,8,9,7,4,1,0,0],[1,5,0,0,0,6,0,0,9],[7,0,0,0,6,0,0,0,0],[6,1,0,0,0,2,8,5,0],[0,0,2,1,0,0,0,9,6]])
matrix_1_1 = np.matrix([[2,3,1],[0,4,9],[0,0,0]])
matrix_1_2 = np.matrix([[0,0,5],[0,0,0],[0,1,0]])
matrix_1_3 = np.matrix([[9,0,0],[6,2,0],[0,0,3]])
matrix_2_1 = np.matrix([[9,0,0],[0,0,8],[1,5,0]])
matrix_2_2 = np.matrix([[5,3,0],[9,7,4],[0,0,6]])
matrix_2_3 = np.matrix([[0,7,0],[1,0,0],[0,0,9]])
matrix_3_1 = np.matrix([[7,0,0],[6,1,0],[0,0,2]])
matrix_3_2 = np.matrix([[0,6,0],[0,0,2],[1,0,0]])
matrix_3_3 = np.matrix([[0,0,0],[8,5,0],[0,9,6]])

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

def solver_row(matrix_1, matrix_2, matrix_3):
    # looks for single missing numbers in a row of 3 matrices
    '''Enter matrices in the correct order!!!'''
    for x in range(0,3):

        position_1 = matrix_1[x,0]
        position_2 = matrix_1[x,1]
        position_3 = matrix_1[x,2]
        position_4 = matrix_2[x,0]
        position_5 = matrix_2[x,1]
        position_6 = matrix_2[x,2]
        position_7 = matrix_3[x,0]
        position_8 = matrix_3[x,1]
        position_9 = matrix_3[x,2]

        string = str(position_1) + str(position_2) + str(position_3) + str(position_4) + str(position_5) + str(position_6) + str(position_7) + str(position_8) + str(position_9)
        number_zeros = string.count('0')

        if number_zeros == 1:
            position_0 = string.find('0')

            # add the missing number

            if '1' not in string:
                if position_0 == 0:
                    matrix_1[x,0] = 1
                elif position_0 == 1:
                    matrix_1[x,1] = 1
                elif position_0 == 2:
                    matrix_1[x,2] = 1
                elif position_0 == 3:
                    matrix_2[x,0] = 1
                elif position_0 == 4:
                    matrix_2[x,1] = 1
                elif position_0 == 5:
                    matrix_2[x,2] = 1
                elif position_0 == 6:
                    matrix_3[x,0] = 1
                elif position_0 == 7:
                    matrix_3[x,1] = 1
                elif position_0 == 8:
                    matrix_3[x,2] = 1

            elif '2' not in string:
                if position_0 == 0:
                    matrix_1[x,0] = 2
                elif position_0 == 1:
                    matrix_1[x,1] = 2
                elif position_0 == 2:
                    matrix_1[x,2] = 2
                elif position_0 == 3:
                    matrix_2[x,0] = 2
                elif position_0 == 4:
                    matrix_2[x,1] = 2
                elif position_0 == 5:
                    matrix_2[x,2] = 2
                elif position_0 == 6:
                    matrix_3[x,0] = 2
                elif position_0 == 7:
                    matrix_3[x,1] = 2
                elif position_0 == 8:
                    matrix_3[x,2] = 2

            elif '3' not in string:
                if position_0 == 0:
                    matrix_1[x,0] = 3
                elif position_0 == 1:
                    matrix_1[x,1] = 3
                elif position_0 == 2:
                    matrix_1[x,2] = 3
                elif position_0 == 3:
                    matrix_2[x,0] = 3
                elif position_0 == 4:
                    matrix_2[x,1] = 3
                elif position_0 == 5:
                    matrix_2[x,2] = 3
                elif position_0 == 6:
                    matrix_3[x,0] = 3
                elif position_0 == 7:
                    matrix_3[x,1] = 3
                elif position_0 == 8:
                    matrix_3[x,2] = 3

            elif '4' not in string:
                if position_0 == 0:
                    matrix_1[x,0] = 4
                elif position_0 == 1:
                    matrix_1[x,1] = 4
                elif position_0 == 2:
                    matrix_1[x,2] = 4
                elif position_0 == 3:
                    matrix_2[x,0] = 4
                elif position_0 == 4:
                    matrix_2[x,1] = 4
                elif position_0 == 5:
                    matrix_2[x,2] = 4
                elif position_0 == 6:
                    matrix_3[x,0] = 4
                elif position_0 == 7:
                    matrix_3[x,1] = 4
                elif position_0 == 8:
                    matrix_3[x,2] = 4

            elif '5' not in string:
                if position_0 == 0:
                    matrix_1[x,0] = 5
                elif position_0 == 1:
                    matrix_1[x,1] = 5
                elif position_0 == 2:
                    matrix_1[x,2] = 5
                elif position_0 == 3:
                    matrix_2[x,0] = 5
                elif position_0 == 4:
                    matrix_2[x,1] = 5
                elif position_0 == 5:
                    matrix_2[x,2] = 5
                elif position_0 == 6:
                    matrix_3[x,0] = 5
                elif position_0 == 7:
                    matrix_3[x,1] = 5
                elif position_0 == 8:
                    matrix_3[x,2] = 5

            elif '6' not in string:
                if position_0 == 0:
                    matrix_1[x,0] = 6
                elif position_0 == 1:
                    matrix_1[x,1] = 6
                elif position_0 == 2:
                    matrix_1[x,2] = 6
                elif position_0 == 3:
                    matrix_2[x,0] = 6
                elif position_0 == 4:
                    matrix_2[x,1] = 6
                elif position_0 == 5:
                    matrix_2[x,2] = 6
                elif position_0 == 6:
                    matrix_3[x,0] = 6
                elif position_0 == 7:
                    matrix_3[x,1] = 6
                elif position_0 == 8:
                    matrix_3[x,2] = 6


            elif '7' not in string:
                if position_0 == 0:
                    matrix_1[x,0] = 7
                elif position_0 == 1:
                    matrix_1[x,1] = 7
                elif position_0 == 2:
                    matrix_1[x,2] = 7
                elif position_0 == 3:
                    matrix_2[x,0] = 7
                elif position_0 == 4:
                    matrix_2[x,1] = 7
                elif position_0 == 5:
                    matrix_2[x,2] = 7
                elif position_0 == 6:
                    matrix_3[x,0] = 7
                elif position_0 == 7:
                    matrix_3[x,1] = 7
                elif position_0 == 8:
                    matrix_3[x,2] = 7

            elif '8' not in string:
                if position_0 == 0:
                    matrix_1[x,0] = 8
                elif position_0 == 1:
                    matrix_1[x,1] = 8
                elif position_0 == 2:
                    matrix_1[x,2] = 8
                elif position_0 == 3:
                    matrix_2[x,0] = 8
                elif position_0 == 4:
                    matrix_2[x,1] = 8
                elif position_0 == 5:
                    matrix_2[x,2] = 8
                elif position_0 == 6:
                    matrix_3[x,0] = 8
                elif position_0 == 7:
                    matrix_3[x,1] = 8
                elif position_0 == 8:
                    matrix_3[x,2] = 8

            elif '9' not in string:
                if position_0 == 0:
                    matrix_1[x,0] = 9
                elif position_0 == 1:
                    matrix_1[x,1] = 9
                elif position_0 == 2:
                    matrix_1[x,2] = 9
                elif position_0 == 3:
                    matrix_2[x,0] = 9
                elif position_0 == 4:
                    matrix_2[x,1] = 9
                elif position_0 == 5:
                    matrix_2[x,2] = 9
                elif position_0 == 6:
                    matrix_3[x,0] = 9
                elif position_0 == 7:
                    matrix_3[x,1] = 9
                elif position_0 == 8:
                    matrix_3[x,2] = 9

        return matrix_1, matrix_2, matrix_3

def solver_coloumn(matrix_1, matrix_2, matrix_3):
        # looks for single missing numbers in a coloumn of 3 matrices
        '''Enter matrices in the correct order!!!'''
        for y in range(0,3):

            position_1 = matrix_1[0,y]
            position_2 = matrix_1[1,y]
            position_3 = matrix_1[2,]
            position_4 = matrix_2[0,y]
            position_5 = matrix_2[1,y]
            position_6 = matrix_2[2,y]
            position_7 = matrix_3[0,y]
            position_8 = matrix_3[1,y]
            position_9 = matrix_3[2,y]

            string = str(position_1) + str(position_2) + str(position_3) + str(position_4) + str(position_5) + str(position_6) + str(position_7) + str(position_8) + str(position_9)
            number_zeros = string.count('0')

            if number_zeros == 1:
                position_0 = string.find('0')

                # add the missing number

                if '1' not in string:
                    if position_0 == 0:
                        matrix_1[0,y] = 1
                    elif position_0 == 1:
                        matrix_1[1,y] = 1
                    elif position_0 == 2:
                        matrix_1[2,y] = 1
                    elif position_0 == 3:
                        matrix_2[0,y] = 1
                    elif position_0 == 4:
                        matrix_2[1,y] = 1
                    elif position_0 == 5:
                        matrix_2[2,y] = 1
                    elif position_0 == 6:
                        matrix_3[0,y] = 1
                    elif position_0 == 7:
                        matrix_3[1,y] = 1
                    elif position_0 == 8:
                        matrix_3[2,y] = 1

                elif '2' not in string:
                    if position_0 == 0:
                        matrix_1[0,y] = 2
                    elif position_0 == 1:
                        matrix_1[1,y] = 2
                    elif position_0 == 2:
                        matrix_1[2,y] = 2
                    elif position_0 == 3:
                        matrix_2[0,y] = 2
                    elif position_0 == 4:
                        matrix_2[1,y] = 2
                    elif position_0 == 5:
                        matrix_2[2,y] = 2
                    elif position_0 == 6:
                        matrix_3[0,y] = 2
                    elif position_0 == 7:
                        matrix_3[1,y] = 2
                    elif position_0 == 8:
                        matrix_3[2,y] = 2

                elif '3' not in string:
                    if position_0 == 0:
                        matrix_1[0,y] = 3
                    elif position_0 == 1:
                        matrix_1[1,y] = 3
                    elif position_0 == 2:
                        matrix_1[2,y] = 3
                    elif position_0 == 3:
                        matrix_2[0,y] = 3
                    elif position_0 == 4:
                        matrix_2[1,y] = 3
                    elif position_0 == 5:
                        matrix_2[2,y] = 3
                    elif position_0 == 6:
                        matrix_3[0,y] = 3
                    elif position_0 == 7:
                        matrix_3[1,y] = 3
                    elif position_0 == 8:
                        matrix_3[2,y] = 3

                elif '4' not in string:
                    if position_0 == 0:
                        matrix_1[0,y] = 4
                    elif position_0 == 1:
                        matrix_1[1,y] = 4
                    elif position_0 == 2:
                        matrix_1[2,y] = 4
                    elif position_0 == 3:
                        matrix_2[0,y] = 4
                    elif position_0 == 4:
                        matrix_2[1,y] = 4
                    elif position_0 == 5:
                        matrix_2[2,y] = 4
                    elif position_0 == 6:
                        matrix_3[0,y] = 4
                    elif position_0 == 7:
                        matrix_3[1,y] = 4
                    elif position_0 == 8:
                        matrix_3[2,y] = 4

                elif '5' not in string:
                    if position_0 == 0:
                        matrix_1[0,y] = 5
                    elif position_0 == 1:
                        matrix_1[1,y] = 5
                    elif position_0 == 2:
                        matrix_1[2,y] = 5
                    elif position_0 == 3:
                        matrix_2[0,y] = 5
                    elif position_0 == 4:
                        matrix_2[1,y] = 5
                    elif position_0 == 5:
                        matrix_2[2,y] = 5
                    elif position_0 == 6:
                        matrix_3[0,y] = 5
                    elif position_0 == 7:
                        matrix_3[1,y] = 5
                    elif position_0 == 8:
                        matrix_3[2,y] = 5

                elif '6' not in string:
                    if position_0 == 0:
                        matrix_1[0,y] = 6
                    elif position_0 == 1:
                        matrix_1[1,y] = 6
                    elif position_0 == 2:
                        matrix_1[2,y] = 6
                    elif position_0 == 3:
                        matrix_2[0,y] = 6
                    elif position_0 == 4:
                        matrix_2[1,y] = 6
                    elif position_0 == 5:
                        matrix_2[2,y] = 6
                    elif position_0 == 6:
                        matrix_3[0,y] = 6
                    elif position_0 == 7:
                        matrix_3[1,y] = 6
                    elif position_0 == 8:
                        matrix_3[2,y] = 6


                elif '7' not in string:
                    if position_0 == 0:
                        matrix_1[0,y] = 7
                    elif position_0 == 1:
                        matrix_1[1,y] = 7
                    elif position_0 == 2:
                        matrix_1[2,y] = 7
                    elif position_0 == 3:
                        matrix_2[0,y] = 7
                    elif position_0 == 4:
                        matrix_2[1,y] = 7
                    elif position_0 == 5:
                        matrix_2[2,y] = 7
                    elif position_0 == 6:
                        matrix_3[0,y] = 7
                    elif position_0 == 7:
                        matrix_3[1,y] = 7
                    elif position_0 == 8:
                        matrix_3[2,y] = 7

                elif '8' not in string:
                    if position_0 == 0:
                        matrix_1[0,y] = 8
                    elif position_0 == 1:
                        matrix_1[1,y] = 8
                    elif position_0 == 2:
                        matrix_1[2,y] = 8
                    elif position_0 == 3:
                        matrix_2[0,y] = 8
                    elif position_0 == 4:
                        matrix_2[1,y] = 8
                    elif position_0 == 5:
                        matrix_2[2,y] = 8
                    elif position_0 == 6:
                        matrix_3[0,y] = 8
                    elif position_0 == 7:
                        matrix_3[1,y] = 8
                    elif position_0 == 8:
                        matrix_3[2,y] = 8

                elif '9' not in string:
                    if position_0 == 0:
                        matrix_1[0,y] = 9
                    elif position_0 == 1:
                        matrix_1[1,y] = 9
                    elif position_0 == 2:
                        matrix_1[2,y] = 9
                    elif position_0 == 3:
                        matrix_2[0,y] = 9
                    elif position_0 == 4:
                        matrix_2[1,y] = 9
                    elif position_0 == 5:
                        matrix_2[2,y] = 9
                    elif position_0 == 6:
                        matrix_3[0,y] = 9
                    elif position_0 == 7:
                        matrix_3[1,y] = 9
                    elif position_0 == 8:
                        matrix_3[2,y] = 9

            return matrix_1, matrix_2, matrix_3
