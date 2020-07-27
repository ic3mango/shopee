def find_2_adjacent_largest(grid):
	largest = float("-inf")
	first = (0, 0)
	second = (0, 1)

	# find largest horizontally
	for i in range(len(grid)):
		for j in range(len(grid[0]) - 1):
			if grid[i][j] + grid[i][j+1] >= largest:
				largest = grid[i][j] + grid[i][j+1]
				first = (i, j)
				second = (i, j+1)

	# find largest vertically
	for i in range(len(grid) - 1):
		for j in range(len(grid[0])):
			if grid[i][j] + grid[i+1][j] >= largest:
				largest = grid[i][j] + grid[i+1][j]
				first = (i, j)
				second = (i+1, j)

	return largest, first, second

def lucky_winner(grid, n_token):
	worth = 0
	for _ in range(n_token):
		largest, first, second = find_2_adjacent_largest(grid)
		worth += largest
		print(largest)
		# clear taken items from grid by using -inf
		grid[first[0]][first[1]] = float('-inf')
		grid[second[0]][second[1]] = float('-inf')
	return worth

