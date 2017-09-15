def pprint(grid) :
	for i in range(9) :
		for j in range(9) :
			print(grid[i][j],end = " ")
			if(j == 2 or j == 5) :
				print("|",end = " ")
		if(i == 2 or i == 5) :
			print()
			print("---------------------")
		else :
			print()
def getrange(x) :
	if(x >= 0 and x <= 2) :
		return (0,2)
	elif(x >= 3 and x <= 5) :
		return (3,5)
	else :
		return (6,8)

def next(grid,x,y) :
	if(y == 8) :
		return solve(grid,x+1,0)
	else :
		return solve(grid,x,y+1)

def solve(grid,x,y) :
	if(x > 8) :
		pprint(grid)
		return True
	
	if(grid[x][y] != 0) :
		return next(grid,x,y)
		
	(r0,r1) = getrange(x)
	(c0,c1) = getrange(y)
	s = set()
	for i in range(r0,r1+1) :
		for j in range(c0,c1+1) :
			if(grid[i][j] != 0) :
				s.add(grid[i][j])
	for i in range(9) :
		if(grid[x][i] != 0):
			s.add(grid[x][i])
	for i in range(9) :
		if(grid[i][y] != 0) :
			s.add(grid[i][y])
	s = {1,2,3,4,5,6,7,8,9}.difference(s)
	if(len(s) == 0) :
		return False
	for val in s :
		grid[x][y] = val
		if(next(grid,x,y) == True) :
			return True
	grid[x][y] = 0
	return False
 
grid = [list(map(int,input().split())) for i in range(9)]
print("\nInput puzzle\n")
pprint(grid)
x,y = -1,-1
for i in range(9) :
	for j in range(9) :
		if(grid[i][j] == 0) :
			x,y = i,j
			break
	if((x,y) != (-1,-1)) :
			break
print("\noutput puzzle\n")
solve(grid,x,y)
"""
sample input 1. -- source (http://www.puzzles.ca/sudoku_puzzles/sudoku_easy_327.html)
	
	0 0 1 0 0 0 8 0 4
	0 9 7 2 6 0 0 3 0
	0 5 0 0 0 1 0 0 7
	7 0 0 0 0 0 9 0 1
	0 0 0 0 0 5 2 0 0
	2 0 5 0 3 0 0 6 0
	0 0 0 4 0 8 0 7 0
	0 0 9 0 0 0 3 0 0
	0 0 8 0 0 6 0 0 0

sample output 1.-- source(http://www.puzzles.ca/sudoku_puzzles/sudoku_easy_327_solution.html)

	INPUT PUZZLE

	0 0 1 | 0 0 0 | 8 0 4 
	0 9 7 | 2 6 0 | 0 3 0 
	0 5 0 | 0 0 1 | 0 0 7 
	----------------------
	7 0 0 | 0 0 0 | 9 0 1 
	0 0 0 | 0 0 5 | 2 0 0 
	2 0 5 | 0 3 0 | 0 6 0 
	----------------------
	0 0 0 | 4 0 8 | 0 7 0 
	0 0 9 | 0 0 0 | 3 0 0 
	0 0 8 | 0 0 6 | 0 0 0 

	OUTPUT PUZZLE

	6 2 1 | 7 5 3 | 8 9 4 
	8 9 7 | 2 6 4 | 1 3 5 
	3 5 4 | 9 8 1 | 6 2 7 
	----------------------
	7 8 3 | 6 4 2 | 9 5 1 
	9 1 6 | 8 7 5 | 2 4 3 
	2 4 5 | 1 3 9 | 7 6 8 
	----------------------
	1 3 2 | 4 9 8 | 5 7 6 
	4 6 9 | 5 1 7 | 3 8 2 
	5 7 8 | 3 2 6 | 4 1 9 

sample input 2. -- source (http://www.puzzles.ca/sudoku_puzzles/sudoku_hard_261.html)

	8 0 0 0 6 0 3 9 7
	9 1 0 2 0 0 0 0 0
	0 0 0 4 0 0 0 0 0
	0 0 7 9 0 0 0 0 0
	0 0 4 0 0 0 0 2 5
	2 0 0 6 7 0 0 0 0
	0 0 0 0 9 1 0 0 0
	4 0 0 0 0 0 0 3 0
	0 0 0 0 0 0 6 1 0

sample output 2. -- source(http://www.puzzles.ca/sudoku_puzzles/sudoku_hard_261_solution.html)

Input puzzle

8 0 0 | 0 6 0 | 3 9 7 
9 1 0 | 2 0 0 | 0 0 0 
0 0 0 | 4 0 0 | 0 0 0 
---------------------
0 0 7 | 9 0 0 | 0 0 0 
0 0 4 | 0 0 0 | 0 2 5 
2 0 0 | 6 7 0 | 0 0 0 
---------------------
0 0 0 | 0 9 1 | 0 0 0 
4 0 0 | 0 0 0 | 0 3 0 
0 0 0 | 0 0 0 | 6 1 0 

output puzzle

8 4 2 | 1 6 5 | 3 9 7 
9 1 5 | 2 3 7 | 8 4 6 
7 3 6 | 4 8 9 | 1 5 2 
---------------------
1 8 7 | 9 5 2 | 4 6 3 
6 9 4 | 3 1 8 | 7 2 5 
2 5 3 | 6 7 4 | 9 8 1 
---------------------
3 6 8 | 5 9 1 | 2 7 4 
4 7 1 | 8 2 6 | 5 3 9 
5 2 9 | 7 4 3 | 6 1 8 
"""