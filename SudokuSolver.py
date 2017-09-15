from inputGrid import inputGrid
from outputGrid import outputGrid
from bruteForce import bruteForce

grid = inputGrid('puzzle.txt')
grid = bruteForce(grid)
outputGrid(grid,'solve.txt')