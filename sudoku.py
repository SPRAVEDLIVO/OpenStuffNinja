import sudokuengine, shittyleveling, random, utils
sudokus = []
diffs = {'easy':50,'normal':30,'hard':10}
def mainloop(args):
    assert args != []
    assert len(args) == 1
    diffi = args[0]
    if diffi in diffs.keys():
        diff = diffs.get(diffi)
    else:
        diff = random.randint(5,50)
        diffi = 'random'
    puzzle = sudokuengine.random_puzzle(diff)
    sudokus.append(puzzle)
    print(''.join(sudokuengine.solve(puzzle).values()))
    return 'Difficulty: '+diffi+'\n'+'\n'.join(sudokuengine.display(sudokuengine.grid_values(puzzle)))
def check(arg, author):
    if arg != [] and sudokus != []:
        sudoku = arg
        sudoku = ''.join([(i) for i in sudoku])
        if sudoku == ''.join(sudokuengine.solve(sudokus[-1]).values()):
            ath = shittyleveling.Leveling(author)
            vals = ath.ReadValues()
            crntxp = int(vals[1])
            ath.UpdateValues(crntxp+10, 'exp')
            del sudokus[-1]
            return {'result':'Correct!', 'colorize': utils.Colors.green, 'embedding': True}
        else:
            return {'result':'Incorrect', 'colorize': utils.Colors.red, 'embedding': True}
    else:
        return {'result':'Nothing to check!', 'colorize': utils.Colors.red, 'embedding': True}