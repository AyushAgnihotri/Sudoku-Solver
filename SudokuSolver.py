from inputGrid import inputGrid
from outputGrid import outputGrid
from bruteForce import bruteForce
from constraintOptimisation import constraintOptimisation
from genAlgo import genAlgo
import time
import copy
import sys


class SudokuSolver :

	def mean(self,t) :
		return sum(i for i in t)/len(t)

	def sd(self,t) :
		m = self.mean(t)
		return sum((i - m)**2 for i in t )

	def printStats(self,method,solution,t) :

		print("Method : ",method, file = solution)
		print(file = solution)
		for i in range(len(t)) :
			print("time ", i ," = " , t[i] , file = solution)
		print("Mean of ", len(t) ," runs = ", self.mean(t), file = solution)
		print("Standard deviation of ",len(t)," runs = ",self.sd(t), file = solution)


	def run(self,times,choice) :
		t = []
		solution = open('solution.txt','w')
		grid = inputGrid('puzzle.txt')
		gridtemp = copy.deepcopy(grid) 
		if(choice == 1) :
			method = "Brute Force (Exhaustive Search)"
			grid = bruteForce(grid)
		if(choice == 2) :
			method = "Constraint Optimisation (Backtracking)"
			grid = constraintOptimisation(grid)
		if(choice == 3) :
			method = "Genetic Algorithm"
			grid = genAlgo(grid)
		outputGrid(grid,solution)

		for i in range(times) :
			
			t0 = time.clock()
			grid = copy.deepcopy(gridtemp)

			if(choice == 1) :
				grid = bruteForce(grid)
			if(choice == 2) :
				grid = constraintOptimisation(grid)
			if(choice == 3) :
				grid = genAlgo(grid)
			
			t1 = time.clock() - t0
			t.append(t1)
		
		self.printStats(method,solution,t)

	
SudokuSolver().run(int(sys.argv[1]),int(sys.argv[2]))