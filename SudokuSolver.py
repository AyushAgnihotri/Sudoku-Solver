from inputGrid import inputGrid
from outputGrid import outputGrid
from bruteForce import bruteForce
from constraintOptimisation import constraintOptimisation
from genAlgo import genAlgo
import time
import copy
import sys


class SudokuSolver :

	def run(self,choice) :

		solution = open('solution.txt','w')
		grid = inputGrid('puzzle.txt')
		t0 = time.clock()
		if(choice == 1) :
			method = "Brute Force (Exhaustive Search)"
			grid = bruteForce(grid)
		if(choice == 2) :
			method = "Constraint Optimisation (Backtracking)"
			grid = constraintOptimisation(grid)
		if(choice == 3) :
			method = "Genetic Algorithm"
			grid = genAlgo(grid)
		t1 = time.clock() - t0
		print("Method : " , method ,"\n",file = solution)
		outputGrid(grid,solution)
		print("time = " ,t1,file = solution)

	
SudokuSolver().run(int(sys.argv[1]))