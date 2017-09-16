
def getrange(x) :
	if(x >= 0 and x <= 2) :
		return (0,2)
	elif(x >= 3 and x <= 5) :
		return (3,5)
	else :
		return (6,8)


def fitness(grid, x,y):
	temp = grid[x][y]
	for i in range(9):
		if grid[x][i] == temp:
			count = count +1
		if grid[i][y] == temp:
			count = count + 1
	return count

def change(grid):
	mat = []
	for l in range(0,9,3):
		for k in range(0,9,3):
			temp = []
			for i in range(l,l+3):
				for j in range(k,k+3):
					temp.append(grid[i][j])
			mat.append(temp)
	return mat 


#def genAlgo(grid):
	
	
from inputGrid import inputGrid
grid = inputGrid('puzzle.txt')
mat = change(grid)
for i in mat :
	print (i)