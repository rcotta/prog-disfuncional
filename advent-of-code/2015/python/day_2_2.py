

with open("input/day_2.input", "r") as f:

	lines = [line.strip() for line in f.readlines()]

	ans = 0

	for line in lines:
		d = sorted(list(map(int, line.split("x"))))
		size = 2 * (d[0] + d[1]) + (d[0] * d[1] * d[2])
		ans += size

	print(f"Resposta -> {ans}")

