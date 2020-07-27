from lucky_winner import find_2_adjacent_largest, lucky_winner

shopee_grid = [
	[100, -9, -1],
	[-1, 3, 2],
	[-9, 2, 3],
	[2, 5, 1],
	[3, 3, 4]
]
def test_find_2():
	assert find_2_adjacent_largest(shopee_grid) == (99, (0, 0), (1, 0))

def test_lucky_winner():
	assert lucky_winner(shopee_grid) == 113

if __name__ == "__main__":
	test_find_2()
	test_lucky_winner()
	print("Everything passed!")


