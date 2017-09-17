from inputGrid import inputGrid
from outputGrid import outputGrid
from bruteForce import bruteForce
from constraintOptimisation import constraintOptimisation
from genAlgo import genAlgo
import time
grid = inputGrid('puzzle.txt')
t0 = time.clock()
grid = bruteForce(grid)
#grid = constraintOptimisation(grid)
#grid = genAlgo(grid)
t1 = time.clock() - t0
outputGrid(grid,t1,'solution.txt')