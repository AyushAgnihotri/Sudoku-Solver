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

def findBlank(grid) :
	x,y = -1,-1
	for i in range(9) :
		for j in range(9) :
			if(grid[i][j] == 0) :
				x,y = i,j
				break
		if((x,y) != (-1,-1)) :
				break
	return (x,y)

def bruteForce(grid) :

	(x,y) = findBlank(grid)
	solve(grid,x,y)
	return grid