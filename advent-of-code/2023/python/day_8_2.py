import re
import numpy as np

def count_steps(origin, destinations, map_info, directions):

	l_current = [origin for i in destinations]
	steps = 0

	while True:
		d = directions[steps % len(directions)]
		l_current = [map_info[(current, d)] for current in l_current]
		steps += 1
		if len([found for found in l_current if found[2] == 'Z']) > 0:
			break

	return steps


with open("day_8.input", "r") as f:

	directions = None
	map_info = {}

	lines = [line.strip() for line in f.readlines()]

	counter = {}

	for line in lines:
		if ("=" in line):
			labels = re.findall("[A-Z]{3}", line)
			map_info[(labels[0], 'L')] = labels[1]
			map_info[(labels[0], 'R')] = labels[2]

		elif "R" in line or "L" in line:
			directions = line


	# search for nodes ending in 'A'
	origins = [node_id for node_id in set([v[0] for v in map_info.keys()]) if node_id[2] == "A"]
	destinations = [node_id for node_id in set([v[0] for v in map_info.keys()]) if node_id[2] == "Z"]

	num_steps = [count_steps(origin, destinations, map_info, directions) for origin in origins]
	ans = np.lcm.reduce(num_steps)

	print(f"Resposta -> {ans}")

pass

