import sudokuengine, MainExceptions
def mainloop(arg):
    if arg != [] and arg != '':
        sudoku = ''.join(arg)
        print(''.join(sudokuengine.solve(sudoku).values()))
        return '\n'.join(sudokuengine.display(sudokuengine.solve(sudoku)))
    else: raise MainExceptions.NoArgumentSet