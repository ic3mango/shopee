import numpy as np

def lowest_cost(servers, num_servers):
	servers = np.array(servers, dtype=np.float)
	chosen = set()
	cost = 0
	# termination condition
	while len(chosen) < num_servers:
		lowest = np.argmin(servers)
		if lowest == 0:
			free = lowest + 1
		elif lowest == len(servers) - 1:
			free = lowest - 1
		elif np.isinf(servers[lowest - 1]):
			free = lowest + 1
		elif np.isinf(servers[lowest + 1]):
			free = lowest - 1
		else:
			# take adjacent server with largest cost
			free = lowest - 1 if servers[lowest - 1] > servers[lowest + 1] else lowest + 1
		
		# trick to handle edge case
		if np.isinf(free):
			free = lowest

		cost += servers[lowest]
		chosen_this_iter = [lowest, free]
		chosen.update(chosen_this_iter)

		servers[lowest] = np.inf
		servers[free] = np.inf	
		
	return int(cost)
