from judging_servers import lowest_cost

test_case_1 = [1000, 560, 30, 85, 100]
test_case_2 = [1000, 1, 5, 80, 0]

def test_lowest_cost_1():
	assert lowest_cost(test_case_1, 3) == 115

def test_lowest_cost_2():
	assert lowest_cost(test_case_2, 3) == 1

if __name__ == "__main__":
	test_lowest_cost_1()
	test_lowest_cost_2()
	print("Everything passed!")