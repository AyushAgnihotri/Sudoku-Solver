from inputGrid import inputGrid
from outputGrid import outputGrid
from bruteForce import bruteForce
from constraintOptimisation import constraintOptimisation

grid = inputGrid('puzzle.txt')
#grid = bruteForce(grid)
grid = constraintOptimisation(grid)
outputGrid(grid,'solution.txt')