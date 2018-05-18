# ein solver zum lösen von Sudokus mittels backtracking
# Enter Sudoku at the bottom

def row_missing(sudoku,pos):
    # Function for extraxting the missing numbers in a given row
    # pos = [y-pos,x-pos]
    numbers = set([1,2,3,4,5,6,7,8,9])
    row = set(sudoku[pos[0]])
    row_missing = numbers - row
    return row_missing


def coloumn_missing(sudoku,pos):
    # Function for extracting the missing numbers in a given coloumn
    # pos = [y-pos,x-pos]
    numbers = set([1,2,3,4,5,6,7,8,9])
    coloumn = [item[pos[1]]for item in sudoku]
    coloumn = set(coloumn)
    col_missing = numbers - coloumn
    return col_missing

def submatrix(sudoku,position):
    # slicing the sudoku in submatrices
    # position = [y-pos,x-pos]
    if position[0] in range(0,3) and position[1] in range(0,3):
        sub_mat = [sudoku[0][0:3],sudoku[1][0:3],sudoku[2][0:3]]
    elif position[0] in range(0,3) and position[1] in range(3,6):
        sub_mat = [sudoku[0][3:6],sudoku[1][3:6],sudoku[2][3:6]]
    elif position[0] in range(0,3) and position[1] in range(6,9):
        sub_mat = [sudoku[0][6:9],sudoku[1][6:9],sudoku[2][6:9]]
    elif position[0] in range(3,6) and position[1] in range(0,3):
        sub_mat = [sudoku[3][0:3],sudoku[4][0:3],sudoku[5][0:3]]
    elif position[0] in range(3,6) and position[1] in range(3,6):
        sub_mat = [sudoku[3][3:6],sudoku[4][3:6],sudoku[5][3:6]]
    elif position[0] in range(3,6) and position[1] in range(6,9):
        sub_mat = [sudoku[3][6:9],sudoku[4][6:9],sudoku[5][6:9]]
    elif position[0] in range(6,9) and position[1] in range(0,3):
        sub_mat = [sudoku[6][0:3],sudoku[7][0:3],sudoku[8][0:3]]
    elif position[0] in range(6,9) and position[1] in range(3,6):
        sub_mat = [sudoku[6][3:6],sudoku[7][3:6],sudoku[8][3:6]]
    elif position[0] in range(6,9) and position[1] in range(6,9):
        sub_mat = [sudoku[6][6:9],sudoku[7][6:9],sudoku[8][6:9]]
    return sub_mat

def sub_mat_missing(sub_mat):
    # Determining the missing numbers in a submatrix
    numbers = set([1,2,3,4,5,6,7,8,9])
    sub_mat_set = set()
    for item in sub_mat:
        for element in item:
            sub_mat_set.add(element)
    sub_mat_mis = numbers - sub_mat_set
    return sub_mat_mis

def check_solution(sudoku):
    # Function to check wether the sudoku is solved correctly or if there is a
    # problem

    # Check wether the rows contain each number only once
    for row in sudoku:
        one = row.count(1)
        two = row.count(2)
        three = row.count(3)
        four = row.count(4)
        five = row.count(5)
        six = row.count(6)
        seven = row.count(7)
        eight = row.count(8)
        nine = row.count(9)
        if one > 1 or two > 1 or three > 1 or four > 1 or five > 1 or six > 1 or seven > 1 or eight > 1 or nine > 1:
            return False
    # Check wether the coloums contain each number only once
    for i in range(0,9):
        coloumn = [item[i] for item in sudoku]
        one = coloumn.count(1)
        two = coloumn.count(2)
        three = coloumn.count(3)
        four = coloumn.count(4)
        five = coloumn.count(5)
        six = coloumn.count(6)
        seven = coloumn.count(7)
        eight = coloumn.count(8)
        nine = coloumn.count(9)
        if one > 1 or two > 1 or three > 1 or four > 1 or five > 1 or six > 1 or seven > 1 or eight > 1 or nine > 1:
            return False
    # Check wether the submatrices contain each number only once
    for i in range(0,9,3):
        for j in range(0,9,3):
            sub_mat = submatrix(sudoku,[i,j])
            one = sub_mat.count(1)
            two = sub_mat.count(2)
            three = sub_mat.count(3)
            four = sub_mat.count(4)
            five = sub_mat.count(5)
            six = sub_mat.count(6)
            seven = sub_mat.count(7)
            eight = sub_mat.count(8)
            nine = sub_mat.count(9)
            if one > 1 or two > 1 or three > 1 or four > 1 or five > 1 or six > 1 or seven > 1 or eight > 1 or nine > 1:
                return False
    if sudoku == False:
        return False
    return True

# counting the empty fields in the sudoku
def count_zero(sudoku):
    counter = 0
    for line in sudoku:
        counting = line.count(0)
        counter += counting

    return counter



###########################################################################
# Rekursion, die versucht über ausprobieren die richtige Lösung zu finden #
###########################################################################
def solver_recursion(sudoku,pos):
    # Creating a copy of the sudoku
    sudoku_memory = sudoku.copy()
    sudoku_copy = sudoku.copy()
    # check if the solution at the end of the sudoku is valid
    if pos[0] == 8 and pos[1] == 8 and check_solution(sudoku_copy) == True:
        if sudoku_copy[8][8] == 0:
            row_mis = row_missing(sudoku_copy,pos)
            col_mis = coloumn_missing(sudoku_copy,pos)
            sub_mat = submatrix(sudoku_copy,pos)
            sub_mat_mis = sub_mat_missing(sub_mat)
            missing_pos = sub_mat_mis.intersection(row_mis,col_mis)
            sudoku_copy[pos[0]][pos[1]] = missing_pos.pop()
        return sudoku_copy
    elif pos[0] == 8 and pos[1] == 8 and check_solution(sudoku_copy) == False:
        return False
    # COntinue deeper into the recursion if Place is already taken
    if sudoku_copy[pos[0]][pos[1]] != 0:
        if pos[0] != 8 and pos[1] == 8:
            return solver_recursion(sudoku_copy,[pos[0]+1,0])
        elif pos[1]< 8:
            return solver_recursion(sudoku_copy,[pos[0],pos[1]+1])
    # calculate the posible solutions at this position
    row_mis = row_missing(sudoku_copy,pos)
    col_mis = coloumn_missing(sudoku_copy,pos)
    sub_mat = submatrix(sudoku_copy,pos)
    sub_mat_mis = sub_mat_missing(sub_mat)
    missing_pos = sub_mat_mis.intersection(row_mis,col_mis)
    if len(missing_pos) == 0:
        return False
    elif len(missing_pos) == 1:
        sudoku_copy[pos[0]][pos[1]] = missing_pos.pop()
        if pos[0] != 8 and pos[1] == 8:
                solv = solver_recursion(sudoku_copy,[pos[0]+1,0])
                if solv == False:
                    sudoku_copy[pos[0]][pos[1]] = 0
                    return False
                return sudoku_copy
        elif pos[1]< 8:
            solv = solver_recursion(sudoku_copy,[pos[0],pos[1]+1])
            if solv == False:
                sudoku_copy[pos[0]][pos[1]] = 0
                return False
            return sudoku_copy
    else:
        for element in missing_pos:
            sudoku_copy[pos[0]][pos[1]] = element
            if pos[0] != 8 and pos[1] == 8:
                    solv = solver_recursion(sudoku_copy,[pos[0]+1,0])
                    if solv == False:
                        sudoku_copy[pos[0]][pos[1]] = 0
                    elif solv != False:
                        return sudoku_copy
            elif pos[1]< 8:
                solv = solver_recursion(sudoku_copy,[pos[0],pos[1]+1])
                if solv == False:
                    sudoku_copy[pos[0]][pos[1]] = 0
                elif solv != False:
                    return sudoku_copy
        return False









# Funktion zur Lösung des Sudokus
def solver(sudoku):
    sudoku_copy = sudoku.copy()

    return solver_recursion(sudoku_copy,[0,0])

# Sudoku
sudo = [[0,1,0,2,4,0,6,9,0],
            [7,0,0,5,0,9,0,4,0],
            [0,0,0,0,3,0,0,0,0],
            [2,0,5,0,0,0,0,0,0],
            [0,0,4,0,0,0,5,0,0],
            [0,0,0,0,0,0,7,0,9],
            [0,0,0,0,1,0,0,0,0],
            [0,4,0,9,0,3,0,0,8],
            [0,2,3,0,7,6,0,5,0]]

solver(sudo)
sudo
