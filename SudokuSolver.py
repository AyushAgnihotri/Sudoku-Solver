from inputGrid import inputGrid
from outputGrid import outputGrid
from bruteForce import bruteForce
from constraintOptimisation import constraintOptimisation
from genAlgo import genAlgo
grid = inputGrid('puzzle.txt')
#grid = bruteForce(grid)
#grid = constraintOptimisation(grid)
grid = genAlgo(grid)
outputGrid(grid,'solution.txt')