

with open("input/day_1.input", "r") as f:

	line = (f.readline()).strip()

	i = None
	current_floor = 0
	for i in range(len(line)):
		current_floor += 1 if line[i] == "(" else -1
		if current_floor == -1: break

	ans = i + 1
	print(f"Resposta -> {ans}")