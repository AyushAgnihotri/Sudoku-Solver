#this is static , try dynamic too
from random import shuffle
def getrange(x) :
	if(x >= 0 and x <= 2) :
		return (0,2)
	elif(x >= 3 and x <= 5) :
		return (3,5)
	else :
		return (6,8)

def calDomain(grid,x,y) :
	
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
	
	return s

def getGridRange(x) :
	return(getrange(int(x/3)*3),getrange(int(x%3)*3))
		
def getGridNo(x,y):
	return int(x/3)*3 + int(y/3)

def pref(grid,x,y) :
	
	(r0,r1) = getrange(x)
	(c0,c1) = getrange(y)
	
	s = set()
	ct = 0
	for i in range(r0,r1+1) :
		for j in range(c0,c1+1) :
			if(grid[i][j] != 0) :
				s.add(grid[i][j])
				ct += 20

	for i in range(9) :
		if(grid[x][i] != 0):
			s.add(grid[x][i])
			ct += 7
	for i in range(9) :
		if(grid[i][y] != 0) :
			s.add(grid[i][y])
			ct += 3
	return 9 - len(s) - ct
	
def variableOrder(grid) :
	l = []
	for i in range(9) :
		for j in range(9) :
			if(grid[i][j] == 0) :
				l.append((pref(grid,i,j),i,j))
	l = sorted(l,key = lambda x : x[0])
	l = [(i[1],i[2]) for i in l]
	return l

def solve(grid,l,index) :
	if(index >= len(l)) :
		return True	
	x,y = l[index][0],l[index][1]

	s = calDomain(grid,x,y)
	if(len(s) == 0) :
		return False
	for val in s :
		grid[x][y] = val
		if(solve(grid,l,index+1) == True) :
			return True
	grid[x][y] = 0
	return False
def constraintOptimisation(grid) :
	l = variableOrder(grid)
	solve(grid,l,0)
	return grid