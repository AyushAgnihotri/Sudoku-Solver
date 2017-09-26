
from random import randint,random,shuffle 
import copy
from utility.printPuzzle import pprint
#from constraintOptimisation import calDomain

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
		shuffle(l)
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
	return int(i/3)*3 + int(j/3)

def getcol(i,j):
 	return int(i%3)*3 + j%3

def fitness(grid):
	count = 0
	for j in range(9):
		for k in range(9):
			for i in range(9):
				if grid[getrow(j,i)][getcol(j,i)] == grid[getrow(j,k)][getcol(j,k)]:
					count = count +1
				if grid[getrow(i,k)][getcol(i,k)] == grid[getrow(j,k)][getcol(j,k)]:
					count = count + 1
			count -= 2
	return count
def invertChange(grid) :
	mat = [[0]*9 for i in range(9)]
	for i in range(9) :
		for j in range(9) :
			mat[getrow(i,j)][getcol(i,j)] = grid[i][j]
	return mat 

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

def crossover(parent,grid,pop_size):
	children = []
	pop_size = pop_size - len(parent)
	for i in range(pop_size) :
		father = parent[randint(0,len(parent)-1)]
		mother = parent[randint(0,len(parent)-1)]
		cross = randint(0,8)
		child = father[ :cross] + mother[cross :]
		children.append(child)
	
	parent.extend(children)
	return parent


def mutate(parent,grid) :
	mutation = 0.02
	for i in parent:
		if(mutation > random()) :
			for subgrid in range(9) :
				for count in range(3) :
					pos1 = randint(0,8)
					pos2 = randint(0,8)
					if(grid[subgrid][pos2] == 0 and grid[subgrid][pos1] == 0) :
						i[subgrid][pos1],i[subgrid][pos2] = i[subgrid][pos2],i[subgrid][pos1]

def evolve(pop,grid) :

	pop = [(fitness(i),i) for i in pop]
	pop = sorted(pop, key = lambda x : x[0])
	#print("output")
	#print(pop[0][0])
	#pprint(invertChange(pop[0][1]))
	#print()
	pop = [i[1] for i in pop ]
	pop_size = len(pop)
	parent = pop[:int(0.2*pop_size)]
	#fine_len = len(parent)
	random_select = 0.2
	for i in pop[int(0.2*pop_size) : ] :
		if(random_select > random()) :
			parent.append(i)

	mutate(parent,grid)
	return crossover(parent,grid,pop_size)

def grade(pop) :
	grade = 0
	for i in pop :
		grade += fitness(i)
	return grade/len(pop)

def genAlgo(grid) :

	mat = change(grid)
	pop = population(mat,10)
	for i in range(100) :
		pop = evolve(pop,mat)
		#print("fitnes of gen ",i," : ",grade(pop))
	return pop[0]