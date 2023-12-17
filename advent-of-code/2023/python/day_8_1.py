import re


with open("day_8.input", "r") as f:

	directions = None
	map_info = {}

	lines = [line.strip() for line in f.readlines()]

	for line in lines:
		if ("=" in line):
			labels = re.findall("[A-Z]{3}", line)
			map_info[labels[0]] = labels[1:]

		elif "R" in line or "L" in line:
			directions = line

	steps = 0
	current = "AAA"

	while current != "ZZZ":
		
		info = map_info[current]
		direction = directions[steps % len(directions)]
		current = info[0 if direction == 'L' else 1]
		steps += 1

	print(f"Resposta -> {steps}")

pass

