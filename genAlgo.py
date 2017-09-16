import random 
import copy
def individual(grid):
	
	for i in range(9):
		s = set()
		for j in range(9):
			if grid[i][j] != 0:
				s.add(grid[i][j])
		s = {1,2,3,4,5,6,7,8,9}.difference(s)
		l = []
		for j in s:
			l.append(j)
		random.shuffle(l)
		for j in range(9):
			if grid[i][j] == 0:
				grid[i][j] = l.pop()
	return grid

def population( grid, k ):
	pop=[]
	for i in range(k):
		temp = copy.deepcopy(grid)
		pop.append( individual(temp) )
	return pop

def getrow(i,j):
	return int((i/3))*3 + int(j/3)

def getcol(i,j):
 	return int((i%3))*3 + j%3

def fitness(grid):
	count = 0
	for j in range(9):
		for k in range(9):
			for i in range(9):
				if grid[getrow(j,i)][getcol(j,i)] == grid[getrow(j,k)][getcol(j,k)]:
					count = count +1
				if grid[getrow(i,k)][getcol(i,k)] == grid[getrow(j,k)][getcol(j,k)]:
					count = count + 1
	'''for i in range(9):
		for j in range(9):
			x = i, y = j
			for k in range(3):
				x = (x+3)%9
				for l in range(3):
					y = (y+3)%9
					if grid[i][j] == grid[x][y]:
						count = count+1'''
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

popu = population(change(grid),3)
'''for i in popu:
	for k in i:
		print (k)
	print (" ")'''
'''ind = individual( change(grid) )
print ( )'''
