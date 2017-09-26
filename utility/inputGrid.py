
def inputGrid(puzzleFile) :
	with open(puzzleFile,'r') as mypuzzle :
		puzzle = mypuzzle.readlines()
	puzzle = [list(map(int,i.replace('\n',"").split())) for i in puzzle]
	return puzzle