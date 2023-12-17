

with open("input/day_2.input", "r") as f:

	lines = [line.strip() for line in f.readlines()]

	ans = 0

	for line in lines:
		l, w, h = list(map(int, line.split("x")))
		side_areas = [l*w, w*h, h*l]
		ans += (sum(side_areas) * 2) + min(side_areas)

	print(f"Resposta -> {ans}")

