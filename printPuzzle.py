def pprint(grid) :
	for i in range(9) :
		for j in range(9) :
			print(grid[i][j],end = " ")
			if(j == 2 or j == 5) :
				print("|",end = " ")
		if(i == 2 or i == 5) :
			print()
			print("---------------------")
		else :
			print()