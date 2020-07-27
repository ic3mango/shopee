def test_sum():
	assert sum([5, 2, 7, 1]) == 15, "Should be 15"

def test_sum_tuple():
	assert sum((3, 2, 1)) == 6, "Should be 6"

if __name__ == "__main__":
	test_sum()
	test_sum_tuple()
	print("Everything passed")