import solver as sv


sudoku = sv.sudoku_opener()

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
    lines = sv.get_lines(sudoku)
    coloumns = sv.get_coloumns(sudoku)
    matrices = sv.get_matrices(sudoku)
    mis_line = sv.missing_lines(lines)
    mis_col = sv.missing_coloumns(coloumns)
    mis_matrices = sv.missing_matrix(matrices)
    dict_pos = sv.position_zeros(sudoku)
    sudoku, mis_pos = sv.eval_zeros_intersection(sudoku,mis_line,mis_col,mis_matrices, lines, coloumns, dict_pos)
    if zeros == count_zeros:
        lines = sv.get_lines(sudoku)
        coloumns = sv.get_coloumns(sudoku)
        matrices = sv.get_matrices(sudoku)
        mis_line = sv.missing_lines(lines)
        mis_col = sv.missing_coloumns(coloumns)
        mis_matrices = sv.missing_matrix(matrices)
        dict_pos = sv.position_zeros(sudoku)
        sudoku = sv.eval_zeros_all_others(sudoku,dict_pos,mis_pos,lines,coloumns, matrices)
    zeros = count_zeros
    print(sudoku)

sudoku
save = open("sudoku_solved.txt","w")
for line in sudoku:
    save.write(str(line).strip("[]"))
    save.write("\n")
save.close()
