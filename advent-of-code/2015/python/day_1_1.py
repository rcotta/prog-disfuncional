

with open("input/day_1.input", "r") as f:

	line = (f.readline()).strip()
	ans = line.count("(") - line.count(")")
	print(f"Resposta -> {ans}")